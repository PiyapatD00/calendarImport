from summarizer import summarize_text
import authenAPI as authen
from file_parser import extract_from_text, extract_from_pdf, extract_from_image
import json

def main():

    file_path = "sample_files/sample.txt"  # เปลี่ยนได้

    # เลือกประเภท
    if file_path.endswith(".txt"):
        raw_text = extract_from_text(file_path)
    elif file_path.endswith(".pdf"):
        raw_text = extract_from_pdf(file_path)
    elif file_path.endswith((".jpg", ".png")):
        raw_text = extract_from_image(file_path)

    print("Extracted Text:\n", raw_text)

    summary = summarize_text(raw_text)
    print("\nSummarized:\n", summary)
    event = json.loads(summary)
    creds = authen.authenticate_google_api()
    service = authen.build('calendar', 'v3', credentials=creds)
    event_result = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Event created: {event_result.get('htmlLink')}")


if __name__ == '__main__':
    main()
    