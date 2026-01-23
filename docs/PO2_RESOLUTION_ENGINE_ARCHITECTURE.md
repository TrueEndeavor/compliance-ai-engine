# PO2 Resolution Engine
**Status:** PROPOSED | **Date:** 2026-01-23

---

## The Problem (30 seconds)

```
Same snippet flagged by 3 agents:

"Fund returned 12% annually"
  ├── Performance Agent  → Theme 2
  ├── Disclosure Agent   → Theme 3
  └── Misleading Agent   → Theme 1

PO2 Requirement: ONE theme per snippet.
```

---

## Proposed Solution (60 seconds)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   COLLECT    │ ──► │   CLUSTER    │ ──► │   RESOLVE    │
│  (parallel)  │     │   (fuzzy)    │     │ (precedence) │
└──────────────┘     └──────────────┘     └──────────────┘
   9 agents           Group similar        First gate
   run async          snippets             match wins
```

**Output:** One theme per finding, with audit trail of what was suppressed.

---

## Tech Stack & Why

| Tech | What | Why This |
|------|------|----------|
| **Pydantic** | Data models | Validation + JSON schema auto-gen. Industry standard. |
| **rapidfuzz** | Fuzzy matching | C++ backend = 10x faster than difflib. MIT license. |
| **asyncio** | Parallel agents | Built-in Python. LLM calls are I/O bound. 5-9x speedup. |

### Alternatives Considered

| Instead of | Could use | Why not |
|------------|-----------|---------|
| rapidfuzz | difflib | 10x slower |
| rapidfuzz | sentence-transformers | Overkill, adds GPU dependency |
| asyncio | threading | GIL issues, harder to debug |
| asyncio | multiprocessing | Memory overhead for I/O-bound tasks |
| Pydantic | dataclasses | No validation, no JSON schema |

---

## The Code

### 1. Precedence Enum

```python
from enum import IntEnum

class ThemePrecedence(IntEnum):
    """Lower = higher priority = wins."""
    PERFORMANCE   = 1   # Gate 1
    RANKINGS      = 2   # Gate 2
    TESTIMONIALS  = 3   # Gate 3
    DIGITAL       = 4   # Gate 4
    THIRD_PARTY   = 5   # Gate 5
    MISLEADING    = 6   # Gate 6
    COMPARISONS   = 7   # Gate 6
    DISCLOSURES   = 8   # Gate 6
    EDITORIAL     = 9   # Gate 7
```

**Why IntEnum:** Sortable. `sorted(findings, key=lambda f: f.theme)` just works.

---

### 2. Data Models

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class RawFinding(BaseModel):
    """What each agent outputs."""
    theme: ThemePrecedence
    theme_name: str
    snippet: str
    snippet_normalized: Optional[str] = None
    page_number: Optional[int] = None
    char_start: Optional[int] = None
    char_end: Optional[int] = None
    bucket: str
    rationale: str
    recommendation: str
    confidence: float = Field(default=1.0, ge=0, le=1)

class ResolvedFinding(BaseModel):
    """Final output. ONE theme."""
    theme: ThemePrecedence
    theme_name: str
    snippet: str
    bucket: str
    rationale: str
    recommendation: str
    # Audit trail
    competing_themes: List[str] = []
    resolution_reason: str = ""
```

**Why Pydantic:**
- Validates at runtime (confidence must be 0-1)
- Auto-generates OpenAPI schema if we need an API later
- IDE autocomplete works

---

### 3. Fuzzy Matcher

```python
from rapidfuzz import fuzz

class SnippetMatcher:
    def __init__(self, threshold: float = 0.75):
        self.threshold = threshold

    def is_similar(self, a: RawFinding, b: RawFinding) -> bool:
        # Layer 1: Character overlap (if we have offsets)
        if self._has_offsets(a, b):
            if self._overlap_ratio(a, b) > 0.5:
                return True

        # Layer 2: Fuzzy text match
        ratio = fuzz.ratio(a.snippet_normalized, b.snippet_normalized) / 100
        if ratio >= self.threshold:
            return True

        # Layer 3: One contains the other
        if a.snippet_normalized in b.snippet_normalized:
            return True
        if b.snippet_normalized in a.snippet_normalized:
            return True

        return False

    def cluster(self, findings: List[RawFinding]) -> List[List[RawFinding]]:
        """Group similar findings."""
        clusters, used = [], set()
        for i, f in enumerate(findings):
            if i in used:
                continue
            cluster = [f]
            used.add(i)
            for j, other in enumerate(findings):
                if j not in used and self.is_similar(f, other):
                    cluster.append(other)
                    used.add(j)
            clusters.append(cluster)
        return clusters
```

**Why 75% threshold:** Catches "Fund returned 12%" vs "Fund returned 12% annually". Tunable.

**Why 3-layer matching:**
1. Char offsets are most reliable (if available)
2. Fuzzy catches rephrasing
3. Containment catches partial captures

---

### 4. Resolver (The Core Logic)

```python
class SequentialResolver:
    GATE_6 = {ThemePrecedence.MISLEADING,
              ThemePrecedence.COMPARISONS,
              ThemePrecedence.DISCLOSURES}

    def resolve(self, cluster: List[RawFinding]) -> ResolvedFinding:
        if len(cluster) == 1:
            return self._to_resolved(cluster[0], [], "No conflict")

        # Sort by precedence (lower = wins)
        ranked = sorted(cluster, key=lambda f: f.theme.value)
        winner = ranked[0]
        losers = ranked[1:]

        # Gate 6 sub-resolution
        if winner.theme in self.GATE_6:
            g6 = [f for f in cluster if f.theme in self.GATE_6]
            if len(g6) > 1:
                winner = sorted(g6, key=lambda f: f.theme.value)[0]
                losers = [f for f in cluster if f != winner]

        return self._to_resolved(
            winner,
            losers,
            f"Gate {winner.theme.value} > Gates {[l.theme.value for l in losers]}"
        )
```

**Why this logic:** Mirrors PO2 SOW exactly. First gate match wins.

---

### 5. Parallel Agents

```python
import asyncio

class AgentPool:
    def __init__(self, agents: list):
        self.agents = agents

    async def run_all(self, doc: str, meta: dict) -> List[RawFinding]:
        tasks = [agent.analyze(doc, meta) for agent in self.agents]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        findings = []
        for r in results:
            if not isinstance(r, Exception):
                findings.extend(r)
        return findings
```

**Why asyncio.gather:**
- LLM API calls = waiting on network
- 9 agents × 3 sec each = 27 sec sequential
- With gather = ~3-5 sec parallel
- `return_exceptions=True` = one failure doesn't kill all

---

### 6. Pipeline (Putting It Together)

```python
class Pipeline:
    def __init__(self):
        self.agents = AgentPool([...])  # 9 agents
        self.matcher = SnippetMatcher(threshold=0.75)
        self.resolver = SequentialResolver()

    async def run(self, doc: str, meta: dict) -> List[ResolvedFinding]:
        # Phase 1: Parallel detection
        raw = await self.agents.run_all(doc, meta)

        # Phase 2: Cluster similar snippets
        clusters = self.matcher.cluster(raw)

        # Phase 3: Resolve each cluster
        return [self.resolver.resolve(c) for c in clusters]
```

---

## Gate Logic (Visual)

```
Cluster enters: {Theme 2, Theme 3, Theme 1}

Gate 1: Theme 2 present? → YES → STOP → Winner: Theme 2
        (Performance wins, others suppressed)

─────────────────────────────────────────────────

Cluster enters: {Theme 3, Theme 1}

Gate 1: Theme 2? NO
Gate 2: Theme 7? NO
Gate 3: Theme 4? NO
Gate 4: Theme 5? NO
Gate 5: Theme 8? NO
Gate 6: Theme 1,6,3? → YES → Sub-resolve: Theme 1 > Theme 3
        Winner: Theme 1 (Misleading)
```

**Rule:** First gate match wins. Period.

---

## Output Example

```json
{
  "theme": "PERFORMANCE",
  "theme_name": "Performance Presentation & Reporting",
  "snippet": "Fund returned 12% annually",
  "bucket": "Net vs. Gross Presentation Errors",
  "rationale": "Returns shown without net/gross designation",
  "recommendation": "Add 'Net of fees' labeling",
  "competing_themes": ["Disclosures", "Misleading"],
  "resolution_reason": "Gate 1 > Gates [6, 8]"
}
```

---

## Open Questions for Discussion

| Question | Options | Trade-off |
|----------|---------|-----------|
| **Fuzzy threshold** | 0.75 default | Lower = more merging, risk of false positives |
| **Gate 6 sub-resolution** | Fixed precedence vs confidence-weighted | Simplicity vs accuracy |
| **Char offsets** | Require from agents? | More reliable clustering vs agent complexity |

---

## Metrics to Validate

| Metric | How to Measure |
|--------|----------------|
| **Speed** | Time parallel vs sequential (expect 5-9x) |
| **Accuracy** | Manual review of 100 clustered snippets |
| **False merges** | Snippets incorrectly grouped |
| **Missed merges** | Same snippet not grouped |

---

## Dependencies

```txt
pydantic>=2.0.0
rapidfuzz>=3.0.0
```

No GPU. No heavy ML models. Pure Python + one C++ extension.

---

## TL;DR

1. **Agents run in parallel** (asyncio) → N raw findings
2. **Fuzzy cluster** similar snippets (rapidfuzz) → M clusters
3. **First gate match wins** (sort by precedence) → M resolved findings
4. **Audit trail** shows what was suppressed and why

Total new code: ~200 lines.
