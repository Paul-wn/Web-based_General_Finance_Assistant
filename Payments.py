import requests
import re
import os
import pytesseract
from PIL import Image
from datetime import datetime

def convert_thai_to_english_date(thai_date):
    # แมปปิ้งชื่อเดือน
    months_thai_to_english = {
        'ม.ค.': 'Jan',
        'ก.พ.': 'Feb',
        'มี.ค.': 'Mar',
        'เม.ย.': 'Apr',
        'พ.ค.': 'May',
        'มิ.ย.': 'Jun',
        'ก.ค.': 'Jul',
        'ส.ค.': 'Aug',
        'ก.ย.': 'Sep',
        'ต.ค.': 'Oct',
        'พ.ย.': 'Nov',
        'ธ.ค.': 'Dec'
    }
    
    # แยกวันที่ออกมา
    day, month_thai, year = thai_date.split()
    
    # แปลงชื่อเดือนภาษาไทยเป็นภาษาอังกฤษ
    month_english = months_thai_to_english.get(month_thai, month_thai)
    # แปลงเป็นวันที่ในรูปแบบใหม่
    new_date = f"{day} {month_english} {int(year)-543}"  # เพิ่ม 543 สำหรับปีไทย
    return new_date


class Payment:

    def __init__(self, amount: float = None, date: str = None, time: str = None):
        self.amount = amount
        self.date = date
        self.time = time 

    def __repr__(self):
        return f"<Payment amount={self.amount} date='{self.date}' time='{self.time}'>"

    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "time": self.time
        }


    @classmethod
    def from_receipt(cls, file_path: str):
        """สร้าง Payment object จาก receipt ด้วย OCR API"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'rb') as f:
            files = [('file', (os.path.basename(file_path), f, 'application/pdf'))]
            # headers = {'apikey': cls.API_KEY}
            # response = requests.post(cls.OCR_API_URL, headers=headers, files=files)

            img = Image.open(file_path)
            text = pytesseract.image_to_string(img, lang='tha')

        # print(response.text)
        date_re = re.findall(r'\d{1,2}\s\D{1,2}\.\D\.\s\d{4}' , text)
        time_re = re.findall(r'\d{2}:\d{2}' , text)
        amount_re = re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}\b' , text)
        date = convert_thai_to_english_date(date_re[0])

        return cls(date=date , time = time_re[0] +' น.' , amount = amount_re[0]+' บาท' )

# filepath = ['receipt.jpg','receipt3.jpg','receipt4.jpg']
# for i in filepath:
#     payment = Payment.from_receipt(i)
#     print(payment.date)
#     print(payment.time)
#     print(payment.amount)

# payment = Payment.from_receipt('receipt.jpg')
# print(payment.date)
# print(payment.time)
# print(payment.amount)
