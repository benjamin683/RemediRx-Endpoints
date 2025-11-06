from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()

pageNumber = 0
formDict = { 1 : {}, 2 : {}}
formDict[1] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "initial_information_form_1",
        "items": [
            {"id": "patientName", "t": "Patient Name", "type": "string", "req": True, "value": ""},
            {"id": "gender", "t": "Gender", "type": "checkbox", "options": ["Male", "Female"], "req": True},
            {"id": "dob", "t": "DOB", "type": "string", "req": True, "value": ""},
            {"id": "ssn", "t": "SSN", "type": "string", "req": True, "value": ""},
            {"id": "phone", "t": "Phone", "type": "string", "req": True, "value": ""},
            {"id": "email", "t": "Email", "type": "string", "req": True, "value": ""}
        ]
    }
}

formDict[2] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "initial_information_form_2",
        "items": [
            {"id": "patientName", "t": "Patient Name", "type": "string", "req": True, "value": ""},
            {"id": "gender", "t": "Gender", "type": "checkbox", "options": ["Male", "Female"], "req": True},
            {"id": "dob", "t": "DOB", "type": "string", "req": True, "value": ""},
            {"id": "ssn", "t": "SSN", "type": "string", "req": True, "value": ""},
            {"id": "phone", "t": "Phone", "type": "string", "req": True, "value": ""},
            {"id": "email", "t": "Email", "type": "string", "req": True, "value": ""}
        ]
    }
}

@app.post("/begin_session")
def tool_a():
    global pageNumber
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
def tool_b(data: dict[Any, Any]):
    global pageNumber
    # write information to database
    if len(formDict) == pageNumber:
        return {"message": "All information has been submitted."}
    pageNumber += 1
    return formDict[pageNumber]
