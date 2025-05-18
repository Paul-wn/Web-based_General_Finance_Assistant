import pytesseract
from PIL import Image
from pathlib import Path

# กรณีใช้บน Windows ให้ระบุ path ของ tesseract.exe ด้วย เช่น:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# เปิดภาพ
# image_path = Path('image/receipt5.jpg')
img = Image.open('image/receipt7.jpg')
# ใช้ OCR ภาษาไทย
text = pytesseract.image_to_string(img, lang='tha')

print(text)