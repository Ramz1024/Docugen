import requests

def generate_description(code_snippet, api_token):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    payload = {
        "inputs": f"Summarize the purpose of this code: {code_snippet}",
        "parameters": {"max_length": 50, "min_length": 10}
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        return "Description not available."
