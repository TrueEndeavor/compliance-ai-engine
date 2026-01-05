from app.nodes.nodeConfig import AgentState
from google import genai
from google.genai import types
from app.utility import load_json_file, load_text_file
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

REGULATORY_CONTEXT = load_text_file(
    BASE_DIR / "prompts/cluster_claims/sec/MisleadingUnsubstantiatedClaims_v1.0.txt"
)

GROUND_TRUTH = load_json_file(
    BASE_DIR / "prompts/ground_truth/sec/sec_misleading_examples.json"
)

def sec_misleading(state:AgentState)->AgentState:
    
  
    SYSTEM_PROMPT = f"""
    You are a SEC compliance examiner. Your sole purpose is to detect misleading, unsubstantiated, or promissory statements in narrative text.

    REGULATORY STANDARDS:
    {REGULATORY_CONTEXT}

    KNOWN VIOLATION PATTERNS:
    {GROUND_TRUTH}

    - SKIP general educational content with no specific recommendation.
    - SKIP factual statements of past contribution (e.g., "Tech sector contributed 5%").
    - SKIP statements immediately qualified by proximate risk language (e.g., "may", "could").
    - DO NOT flag performance data issues (handled by a separate agent).
    - DO NOT flag missing footers (handled by a separate agent).

    DETECTION INSTRUCTIONS:
    1. Scan the text for statements matching the "Known Violation Patterns" or violating "Regulatory Standards".
    2. Focus on:
    - Universal/Blanket Recommendations ("all investors should...").
    - Guaranteed Outcomes ("will ensure...", "risk-free").
    - Prescriptive Product Pushing ("must reinvest in JPM...").
    - Factual Errors in Disclaimers ("Past performance IS a guarantee").
    3. Perform a PROXIMITY CHECK for every hit:
    - Does a risk disclosure or qualifier exist in the immediate sentence before/after?
    - IF YES: Ignore (False Positive).
    - IF NO: Flag as violation.

    OUTPUT FORMAT (JSON ONLY):
    Return a single JSON object. No markdown formatting. 

    {{
        "misleading_claims": [
            {{
            "section_title": "Section Header or 'Unknown'",
            "page_number": "Page #",
            "violating_text": "Exact quote of the misleading sentence.",
            "observations": "Why is this misleading? (e.g., 'Universal suitability claim without individual assessment')",
            "recommendations": "How to fix it (e.g., 'Add: This strategy may not be suitable for all investors')."
            }}
        ]
    }}

    """
    pdf_config = types.Part.from_bytes(
        data=state['marketing_file_bytes'],
        mime_type ='application/pdf'
    )
    client  = genai.Client()
    llm_config=types.GenerateContentConfig(
        temperature=0.1,
        thinking_config =None
    )
    llm_contents =SYSTEM_PROMPT

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents = [llm_contents,pdf_config],
            config = llm_config
        )

        artifact = response.text 

    except Exception as e:
        return {**state, 'sec_misleading_artifact': f"Error: {str(e)}"}
    return {
        **state,'sec_misleading_artifact':artifact
    }
