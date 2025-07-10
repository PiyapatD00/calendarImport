import pytesseract
from PIL import Image
import pdfplumber

def extract_from_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_from_image(path):
    return pytesseract.image_to_string(Image.open(path), lang='eng+tha')
