import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Enable CORS for React frontend - MUST be first middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BUCKET_NAME = "Business Contents"

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables are required")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# Pydantic model for request validation
class ContentRequest(BaseModel):
    subject: str
    content: str


def count_words(text):
    """
    Count the number of words in a text string
    """
    return len(text.strip().split())


def save_content_to_supabase(subject: str, content: str):
    """
    Save subject and content to Supabase storage
    Returns: (success: bool, message: str)
    """
    try:
        filename = f"{subject}.txt"
        
        # Upload to Supabase
        response = supabase.storage.from_(BUCKET_NAME).upload(
            filename,
            content.encode('utf-8'),
            {"content-type": "text/plain"}
        )
        
        return True, f"Content saved successfully to Supabase: {filename}"
    except Exception as e:
        return False, str(e)


def read_content_from_supabase(subject: str):
    """
    Read subject content from Supabase storage
    Returns: (success: bool, content: str or error_message: str)
    """
    try:
        filename = f"{subject}.txt"
        
        # Download from Supabase
        response = supabase.storage.from_(BUCKET_NAME).download(filename)
        
        return True, response.decode('utf-8')
    except Exception as e:
        return False, str(e)


@app.get("/")
def read_root():
    """
    Root endpoint - check if API is running
    """
    return {"message": "FastAPI server is running"}


@app.post("/api/save")
def save_content(request: ContentRequest):
    """
    API endpoint to save subject and content to file
    - Validates subject is not empty
    - Validates content is not empty
    - Validates word count is not more than 150
    """
    # Strip whitespace
    subject = request.subject.strip()
    content = request.content.strip()
    
    # Validate subject
    if not subject:
        raise HTTPException(status_code=400, detail="Subject cannot be empty")
    
    # Validate content
    if not content:
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    
    # Count words in content
    word_count = count_words(content)
    
    # Validate word count - maximum 150 words
    if word_count > 150:
        raise HTTPException(
            status_code=400, 
            detail=f"Content exceeds 150 words. Current: {word_count} words"
        )
    
    # Save to Supabase
    success, message = save_content_to_supabase(subject, content)
    
    if success:
        return {
            "message": message,
            "word_count": word_count,
            "subject": subject
        }
    else:
        raise HTTPException(status_code=500, detail=f"Failed to save: {message}")


@app.get("/api/read/{subject}")
def read_content(subject: str):
    """
    API endpoint to read subject content from Supabase storage
    """
    # Validate subject
    subject = subject.strip()
    if not subject:
        raise HTTPException(status_code=400, detail="Subject cannot be empty")
    
    # Read from Supabase
    success, result = read_content_from_supabase(subject)
    
    if success:
        return {
            "subject": subject,
            "content": result,
            "word_count": count_words(result)
        }
    else:
        raise HTTPException(status_code=404, detail=f"File not found: {result}")


if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
