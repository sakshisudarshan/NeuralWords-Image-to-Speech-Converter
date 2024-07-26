# Neural Words - Image to Speech Converter

Neural Words is a project designed to assist visually impaired individuals by converting images into audible descriptions. This application leverages advanced image processing and machine learning techniques to analyze and interpret visual content, translating it into speech.

## Features
- Image-to-speech conversion
- Detailed description of visual content
- User-friendly interface for easy interaction
- Support for various image formats

## Technology Stack
- **Frontend:** Kivy (for the application interface)
- **Backend:** Flask
- **Image Processing:** pytesseract, OpenCV, PIL
- **Machine Learning:** Transformers (BLIP)
- **Speech Synthesis:** gTTS (Google Text-to-Speech)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Git
- Kivy dependencies (refer to the Kivy [installation guide](https://kivy.org/doc/stable/gettingstarted/installation.html))

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sakshisudarshan/NeuralWords-Image-to-Speech-Converter.git
   cd NeuralWords-Image-to-Speech-Converter

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install backend dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**
   ```bash
   python backend.py
   ```

5. **Run the frontend application**
   ```bash
   python main.py
   ```

<img width="797" alt="Untitled 3" src="https://github.com/user-attachments/assets/6d70a638-d904-480a-88d3-83b067e2ff4a">
<img width="797" alt="Untitled 4" src="https://github.com/user-attachments/assets/e12a5efa-3edb-484f-81f4-d25db386ba68">
<img width="797" alt="Untitled 5" src="https://github.com/user-attachments/assets/85846643-492b-40bf-a7b8-c562f8e65661">


## Code Overview

### Backend (`backend.py`)
- Flask application to handle image processing requests.
- Uses pytesseract to extract text from images.
- Uses a pre-trained BLIP model to generate image captions.

### Models (`models.py`)
- Contains functions for preprocessing images and generating captions using the BLIP model.

### Frontend (`main.py`)
- Kivy application to create a user interface.
- Allows users to select images, send them to the backend for processing, and receive audible descriptions.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Sakshi Sudarshan](mailto:sakshisudarshan4@gmail.com).
