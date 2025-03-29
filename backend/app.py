from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# DeepSeek API endpoint and key
DEEPSEEK_API_URL = 'https://api.deepseek.ai/grammar-correction'  # Replace with actual endpoint
DEEPSEEK_API_KEY = 'sk-20be3205108248d19cdacb850d679b43'  # Replace with your DeepSeek API key

@app.route('/correct', methods=['POST'])
def correct_grammar():
    text = request.json.get('text', '')  # Extract text from the request

    # Prepare DeepSeek API request
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',  # Pass API key in header
        'Content-Type': 'application/json'
    }
    
    payload = {
        'text': text  # Text to be corrected
    }
    
    # Make the POST request to DeepSeek API
    response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        corrected_text = response.json().get('corrected_text', '')
        return jsonify({"corrected_text": corrected_text})
    else:
        return jsonify({"error": "Unable to process the request."}), 400

if __name__ == '__main__':
    app.run(debug=True)
