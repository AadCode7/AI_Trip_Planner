import os
import datetime

def save_to_document(response_text: str, directory: str = "./output"):
    """Save the response text to a document with a timestamped filename."""
    
    os.makedirs(directory, exist_ok = True)

    markdown_content = f"""AI Travel Plan

    # **Generated:** {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}
    # **Created By:** AI Travel Planner

    ---

    {response_text}

    """

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{directory}/AI_Travel_Plan_{timestamp}.md"

        print(f"Saving response to {filename}...")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        return filename
    
    except Exception as e:
        print(f"Error saving document: {e}")
        return None
    

