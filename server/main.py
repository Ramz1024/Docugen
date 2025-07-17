from flask import Flask, request, jsonify
from generate_docs import generate_documentation
import os

app = Flask(__name__)

TOKEN = os.environ.get("HF_API_TOKEN")

# --- Place your parser function here ---
def parse_code(file_path):
    pass

# --- Place your summarize function here ---
def summarize(parsed_data):
    pass

# --- Upload Endpoint ---
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    os.makedirs("uploaded", exist_ok=True)
    file_path = f"uploaded/{file.filename}"
    file.save(file_path)

    parsed_json_file_path = parse_code(file_path)
    documentation = generate_documentation(parsed_json_file_path, "docs", TOKEN)

    os.remove(file_path)

    return jsonify({"documentation": documentation})

if __name__ == '__main__':
    app.run(debug=True)
