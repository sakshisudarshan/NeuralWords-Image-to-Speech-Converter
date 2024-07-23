from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract
from model import get_image_caption

app = Flask(__name__)
CORS(app)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    img = Image.open(file.stream).convert('RGB')

    extracted_text = pytesseract.image_to_string(img).strip()

    caption = get_image_caption(img)

    return jsonify({'text_result': extracted_text, 'caption_result': caption})

if __name__ == '__main__':
    app.run(debug=True)