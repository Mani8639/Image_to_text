# Image to Text Converter

This project converts images into readable text using Python, Streamlit, and Tesseract OCR.  
You can upload an image, and the app will extract the text from it.

---

## Features

- Upload image files (JPG, PNG, JPEG)
- Extract text from images using OCR
- Simple and clean Streamlit interface
- Easy to use for beginners

---

## Technologies Used

- Python
- Streamlit
- Pytesseract (OCR)
- Pillow

---

## Project Structure

Image_to_text/
- app.py  
- requirements.txt  
- README.md  

---

## How to Install and Run

1. Clone the project:
  git clone https://github.com/Mani8639/Image_to_text.git

  cd Image_to_text

2. Install the required libraries:
  pip install -r requirements.txt


3. Install Tesseract OCR  
Windows users can download it from:  
https://github.com/UB-Mannheim/tesseract/wiki

After installing, add the path inside app.py (if needed):
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

4. Run the application:
 streamlit run app.py

---

## How It Works

1. Run the app  
2. Upload an image  
3. The app reads the text from the image  
4. The extracted text will be shown on the screen  

---

## Future Improvements

- Support for PDF files  
- Better text accuracy  
- Multi-language OCR

---

## Author

Manikanta Addala  
GitHub: https://github.com/Mani8639
