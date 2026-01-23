import os

def save_user_input():
    """
    Collects subject and content from user input and saves to a text file.
    File is saved as 'subject.txt' in the 'data storage' folder.
    """
    # Get user input by deleting leading/trailing whitespace
    subject = input("Enter subject: ").strip()
    
    #check if subject is empty
    if not subject:
        print("Error: Subject cannot be empty.")
        return
    
    content = input("Enter content: ").strip()
    
    if not content:
        print("Error: Content cannot be empty.")
        return
    
    # Define the data storage folder path
    data_storage_folder = os.path.join(os.path.dirname(__file__), "..", "data storage")
    
    # Create the folder if it doesn't exist
    os.makedirs(data_storage_folder, exist_ok=True)
    
    # Create the filename from subject
    filename = f"{subject}.txt"
    filepath = os.path.join(data_storage_folder, filename)
    
    # Save content to file
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✓ Content saved successfully to: {filepath}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    save_user_input()
