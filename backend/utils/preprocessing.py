def clean_text(text):
 
    text = text.lower()   #clean crne ke liye
    text = re.sub(r'[^a-z0-9 ]', '', text)
    return text

def preprocess_data(data):
   
    data['description'] = clean_text(data['description'])    #incident cleaning
    return data
