from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows all domains, you can restrict it later if needed

DEEPSEEK_API_URL = "https://deepseek-v31.p.rapidapi.com/"
RAPIDAPI_KEY = "261984842dmshdb0a4b39e8b25a7p14e388jsn4b1f991a04c9"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "deepseek-v31.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
}

@app.route('/correct-grammar', methods=['POST'])
def correct_grammar():
    text = request.json.get('text')

    payload = {
        "model": "deepseek-v3",
        "messages": [{"role": "user", "content": text}]
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            corrected_text = data.get("choices", [{}])[0].get("message", {}).get("content", "Error correcting text")
            return jsonify({"corrected_text": corrected_text})

        else:
            return jsonify({"error": "Unable to process the request", "status_code": response.status_code}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
