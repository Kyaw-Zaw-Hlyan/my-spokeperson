import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Enable CORS for React frontend - MUST be first middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Define data storage folder path
DATA_STORAGE_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data storage")

# Create folder if it doesn't exist
os.makedirs(DATA_STORAGE_FOLDER, exist_ok=True)


# Pydantic model for request validation
class ContentRequest(BaseModel):
    subject: str
    content: str


def count_words(text):
    """
    Count the number of words in a text string
    """
    return len(text.strip().split())


def save_content_to_file(subject: str, content: str):
    """
    Save subject and content to a text file in data storage folder
    Returns: (success: bool, message: str)
    """
    try:
        filename = f"{subject}.txt"
        filepath = os.path.join(DATA_STORAGE_FOLDER, filename)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return True, f"Content saved successfully to: {filepath}"
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
    
    # Save to file
    success, message = save_content_to_file(subject, content)
    
    if success:
        return {
            "message": message,
            "word_count": word_count,
            "subject": subject
        }
    else:
        raise HTTPException(status_code=500, detail=f"Failed to save: {message}")


if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
