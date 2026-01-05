# pillaiyar suzhii
from dotenv import load_dotenv; load_dotenv()
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.workflow import run_workflow

app = FastAPI()

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):

    try:
        pdf_bytes = await file.read()

        

        #TODO: implement workflow and return the output from gemini
        gemini_output = run_workflow(pdf_bytes)

        return gemini_output

    except Exception as e:
        print(f"Error processing PDF upload: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
        
    finally:
        await file.close()