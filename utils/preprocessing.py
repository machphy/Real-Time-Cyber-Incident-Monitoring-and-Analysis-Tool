import re

def clean_text(text):
    """
    Removes HTML tags, special characters, and extra whitespace from text.
    """
    text = re.sub(r'<.*?>', '', text)  
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)  
    text = re.sub(r'\s+', ' ', text) 
    return text.strip()
