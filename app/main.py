# pillaiyar suzhii
from dotenv import load_dotenv; load_dotenv()
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.workflow import run_workflow
from app.utility import clean_and_parse_json
import json
app = FastAPI()

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    try:
        pdf_bytes = await file.read()

        workflow_result = run_workflow(pdf_bytes)

        raw_artifact = workflow_result.get("sec_misleading_artifact")
        typo_artifact = workflow_result.get('sec_typography_artifact')

        # ✅ Convert JSON string → Python dict
        try:
            parsed_artifact = clean_and_parse_json(raw_artifact)
            parsed_typo_artifact = clean_and_parse_json(typo_artifact)
        except json.JSONDecodeError:
            parsed_artifact = {
                "error": "LLM returned invalid JSON",
                "raw_output": raw_artifact
            }
            parsed_typo_artifact ={
                "error": "LLM returned invalid JSON",
                "raw_output": typo_artifact
            }
            

        return {
            "sec_misleading_artifact": parsed_artifact,
            "sec_typography_artifact":parsed_typo_artifact
        }
        
    finally:
        await file.close()