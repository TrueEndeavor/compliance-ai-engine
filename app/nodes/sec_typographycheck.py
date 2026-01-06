from app.nodes.nodeConfig import AgentState
from google import genai
from google.genai import types
from app.utility import load_json_file, load_text_file
from pathlib import Path



def sec_typographycheck(state:AgentState)->AgentState:
    SYSTEM_PROMPT = f""" 
system prompt:
You are an expert document analyst specializing in financial reporting. Your task is to analyze the extracted text from a PDF (which includes page markers such as ""Page 3:"") and detect every instance where a ""%"" symbol is expected but missing.

Instructions:
- Focus on detecting numeric values that, based on context, are intended to represent percentages. This may include figures related to performance metrics, allocation ratios, growth rates, or any other financial metrics typically expressed as a percentage.
- Use contextual clues and your domain expertise to decide whether a number should be accompanied by a ""%"" symbol. This may include numbers immediately followed or preceded by words indicating proportion, rate, or yield. Flag it if the ""%"" is absent.
- Extract the full context around the numeric value—such as the complete sentence or group of sentences—to ensure there is enough information to determine whether the ""%"" symbol is missing. If the % symbol is in another line for same context then capture it along with that.
- **Before flagging, verify that within the extracted context (even if it spans multiple lines) there is NO ""%"" symbol appropriately adjacent to the numeric value OR in the table heading/label. If % exists anywhere in table context, SKIP completely - do not output any finding.**
- **Do not flag numbers that are clearly identifiers, serial numbers, or values that are not typically expressed as percentages.**
- If the ""%"" symbol is present in the label then its not required to have the symbols for the values present in the table, Also if its not present then make sure you suggest user to add in the Label and not the values 
- **Validate all table and chart labels (headers, axis labels, legends) for percentage notation. If a table or chart displays percentage-based values but the corresponding label does not include “%”, flag it and recommend: “Insert % in the label ‘EXACT_LABEL_NAME’ to become ‘EXACT_LABEL_NAME (%)’.”**
-**For tables WITHOUT % in header (like ""Sector Allocation"", ""Rating Distribution""), recommend: ""Insert % in the label 'EXACT_HEADER_NAME' to become 'EXACT_HEADER_NAME (%)'"**
-**Validate all table headers for percentage notation. For any table where values represent percentages but the header lacks “%”, flag it and recommend: “Insert % in the label ‘EXACT_HEADER_NAME’ to become ‘EXACT_HEADER_NAME (%)’.”**
-**[11:26 PM, 1/5/2026] Anitha Sivasubramanian: Validate all tables for percentage consistency. If all values in a specific column are percentages (e.g., each row contains a % value or represents a proportional share), and the column header does not include “%”, flag it as a compliance issue and recommend renaming the header to “EXACT_COLUMN_NAME (%)”**.
-** For any table column where the majority or all values are expressed as percentages, if an individual row value is missing the “%” symbol, flag it as inconsistent and recommend adding “%” to that value.**

OUTPUT FORMAT (JSON ONLY):
Return a single JSON object. No markdown formatting.

{{
  "sections": [
    {{
      "section_title": "Section Header",
      "page_number": "Page #",
      "observations": "a short snippet of text around the detected missing '%' symbol",   
      "violating_text": "Exact quote of the missing percentage symbol sentence.",
      "recommendations": "Detailed instruction indicating the exact position to insert '%' (e.g., 'Insert % after the value' or 'Insert % in the label X to become X (%)')"
      "category": "Missing Percentage Details"
    }}
  ]
}}

Do not output any extra text or commentary outside of the JSON object.
"
User prompt:
Analyze the provided text content for potential missing '%' symbols.
Apply the instructions detailed in the system prompt rigorously.
Return only the JSON object adhering precisely to the schema defined in the system prompt.


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
        return {**state, 'sec_typography_artifact': f"Error: {str(e)}"}
    return {
        **state,'sec_typography_artifact':artifact
    }
    