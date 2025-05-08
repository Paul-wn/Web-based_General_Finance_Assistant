import pytesseract
from PIL import Image

# กรณีใช้บน Windows ให้ระบุ path ของ tesseract.exe ด้วย เช่น:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# เปิดภาพ
img = Image.open('receipt4.jpg')

# ใช้ OCR ภาษาไทย
text = pytesseract.image_to_string(img, lang='tha')

print(text)