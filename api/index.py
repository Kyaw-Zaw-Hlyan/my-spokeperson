from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase = None

class ContentRequest(BaseModel):
    subject: str
    content: str

def count_words(text):
    return len(text.strip().split())

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/save")
def save_content(request: ContentRequest):
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    
    subject = request.subject.strip()
    content = request.content.strip()
    
    if not subject:
        raise HTTPException(status_code=400, detail="Subject required")
    if not content:
        raise HTTPException(status_code=400, detail="Content required")
    
    word_count = count_words(content)
    if word_count > 150:
        raise HTTPException(status_code=400, detail=f"Exceeds 150 words: {word_count}")
    
    try:
        supabase.storage.from_("Business Contents").upload(
            f"{subject}.txt",
            content.encode('utf-8'),
            {"content-type": "text/plain"}
        )
        return {
            "message": f"Saved to Supabase: {subject}.txt",
            "word_count": word_count,
            "subject": subject
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/read/{subject}")
def read_content(subject: str):
    if not supabase:
        raise HTTPException(status_code=500, detail="Supabase not configured")
    
    try:
        content = supabase.storage.from_("Business Contents").download(f"{subject}.txt")
        return {
            "subject": subject,
            "content": content.decode('utf-8'),
            "word_count": count_words(content.decode('utf-8'))
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Not found: {str(e)}")
