import os
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo

# โหลดค่า .env ทับ environment เดิม (force override)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

RELATIVE_TIME_WORDS = {
    "future": [
        "พรุ่งนี้", "มะรืนนี้", "วันถัดไป", "อีกสองวัน", "อีกสามวัน",
        "วันจันทร์หน้า", "ศุกร์หน้า", "สัปดาห์หน้า", "เดือนหน้า", "ปีหน้า",
        "อีก {N} วัน", "อีก {N} สัปดาห์", "อีก {N} เดือน", "อีก {N} ปี"
    ],
    "past": [
        "เมื่อวาน", "วานนี้", "เมื่อวานซืน", "สัปดาห์ที่แล้ว",
        "เดือนที่แล้ว", "ปีที่แล้ว", "เมื่อ {N} วันก่อน"
    ],
    "time_of_day": [
        "เช้า", "ตอนเช้า", "ตอนสาย", "เที่ยง", "บ่าย", "ตอนบ่าย",
        "เย็น", "ค่ำ", "กลางคืน", "เช้ามืด"
    ]
}

def summarize_text(text):
    reference_date = datetime.now(ZoneInfo("Asia/Bangkok")).isoformat()
    prompt = f"""
You are an assistant that extracts calendar events from natural Thai text.

Today's UTC datetime is: {reference_date}
If the message includes relative time (e.g.{RELATIVE_TIME_WORDS}), resolve it to an absolute ISO 8601 datetime in Asia/Bangkok timezone.

Output JSON for Google Calendar API (values in Thai where appropriate):

Input message:
{text}

Return format:
{{
  "summary": "...",
  "description": "...",
  "location": "...",
  "start": {{
    "dateTime": "...",
    "timeZone": "Asia/Bangkok"
  }},
  "end": {{
    "dateTime": "...",
    "timeZone": "Asia/Bangkok"
  }},
  "status": "confirmed"
}}
"""



    response = client.chat.completions.create(
        model="gpt-4.1-2025-04-14",
        messages=[{"role": "system", "content": "You are a smart assistant that extracts event data from input text. Output a compact JSON object in English keys, but preserve original Thai content in values, suitable for the Google Calendar API."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
