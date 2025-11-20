import smtplib
from email.message import EmailMessage
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from forms import formDict, userDict

app = FastAPI()

pageNumber = 0

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "benjaminwang42@gmail.com"       
EMAIL_PASSWORD = "vvmppsbyysncebnv"
RECIPIENT_EMAIL = ""

def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Agreement Form"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content("Please fill out the pharmacy agreement at your earliest convenience. Thank you!")

    with open(f"PharmacyAgreement.pdf", "rb") as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    return

@app.post("/get_details")
def get_name(data: dict[Any, Any]):
    patient_id = data["patient_id"]

    patient_details = userDict[patient_id]
    return patient_details

@app.post("/begin_session")
def begin_session():
    global pageNumber, RECIPIENT_EMAIL
    RECIPIENT_EMAIL = ""
    pageNumber = 0
    return {
        "bookingId": "1234567890",
        "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
        "questionnaire": {
            "name": "initial_information",
            "items": [
                {
                    "id": "admissionDate",
                    "t": "Date",
                    "type": "string",
                    "req": True,
                    "value": ""         
                },
                {
                    "id": "admittedBy",
                    "t": "Admitted by",
                    "type": "string",
                    "req": True,
                    "value": ""       
                },
                {
                    "id": "admissionType",
                    "t": "Admission Type",
                    "type": "checkbox",
                    "options": ["Re-Admit", "New Admit"],
                    "req": True
                },
                {
                    "id": "admissionMethod",
                    "t": "Admission was",
                    "type": "checkbox",
                    "options": ["In Person", "Virtual", "Phone"],
                    "req": True
                }
            ]
        }
    }

@app.post("/information_advance")
def information_advance(data: dict[Any, Any]):
    global pageNumber, RECIPIENT_EMAIL
    # write information to database
    if len(formDict) == pageNumber:
        if RECIPIENT_EMAIL:
            send_email()
            return { "message": f"All information has been submitted. Agreement form has been sent to {RECIPIENT_EMAIL}"}
        else:
            return { "message": "All information has been submitted, but no recipient email was provided so no agreement form was sent."}
    elif pageNumber == 1:
        if data['patientUpdates']['email']:
            RECIPIENT_EMAIL = data['patientUpdates']['email']
            
    pageNumber += 1
    return formDict[pageNumber]

@app.post("/end_session")
def end_session():
    global pageNumber
    pageNumber = len(formDict)

    if RECIPIENT_EMAIL:
        send_email()
        return { "message": f"All information has been submitted. Agreement form has been sent to {RECIPIENT_EMAIL}"}
    else:
        return { "message": "All information has been submitted, but no recipient email was provided so no agreement form was sent."}