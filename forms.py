from pydantic.types import T


formDict = {}
formDict[1] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "patient_information_form",
        "items": [
  "Patient Information",
  {
    "id": "patientName",
    "t": "Patient Name",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "gender",
    "t": "Gender",
    "type": "checkbox",
    "options": ["Male", "Female"],
    "req": True
  },
  {
    "id": "dob",
    "t": "Date of Birth",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "ssn",
    "t": "SSN",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "phone",
    "t": "Phone",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "email",
    "t": "Email",
    "type": "string",
    "req": True,
    "value": ""
  },

  "Allergies",
  {
    "id": "drugAllergies",
    "t": "Drug Allergies",
    "type": "checkbox",
    "options": ["No Known Drug Allergies", "Drug Allergies"],
    "req": False
  },

  "Packaging Preferences",
  {
    "id": "packagingType",
    "t": "Packaging Type",
    "type": "checkbox",
    "options": ["VIMP", "Bottles", "Spanish"],
    "req": False
  },
  {
    "id": "ezCaps",
    "t": "Patient requests EZ caps",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": False
  },

  "Shipping Address",
  {
    "id": "shippingStreet",
    "t": "Street",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "shippingCounty",
    "t": "County",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "shippingCity",
    "t": "City",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "shippingState",
    "t": "State",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "shippingZip",
    "t": "ZIP Code",
    "type": "string",
    "req": True,
    "value": ""
  },

  "Billing Address",
  {
    "id": "billingStreet",
    "t": "Street",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "billingCounty",
    "t": "County",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "billingCity",
    "t": "City",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "billingState",
    "t": "State",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "billingZip",
    "t": "ZIP Code",
    "type": "string",
    "req": True,
    "value": ""
  },

  "Medication Management",
  {
    "id": "manageOwnMedications",
    "t": "Do you manage your own medications?",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": True
  },
  {
    "id": "medManagerName",
    "t": "Medication Manager Name",
    "type": "string",
    "req": True,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerRelationship",
    "t": "Relationship to Patient",
    "type": "string",
    "req": True,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerPhone",
    "t": "Medication Manager Phone",
    "type": "string",
    "req": True,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerEmail",
    "t": "Medication Manager Email",
    "type": "string",
    "req": False,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  }
]

    }
}

formDict[2] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "monthly_contact_information_form",
        "items": [
  "Monthly Contact Information",
  {
    "id": "monthlyContactType",
    "t": "Monthly Contact is",
    "type": "checkbox",
    "options": ["Patient", "Family Member", "Other Caregiver"],
    "req": True
  },
  {
    "id": "contactAware",
    "t": "Contact is aware we must speak with them monthly and understands service may be interrupted if we are unable to contact them",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": True
  },
  {
    "id": "contactName",
    "t": "Contact Name (if other than Patient)",
    "type": "string",
    "req": False,
    "value": "",
    "when": [
      {
        "operator": "!=",
        "question": "monthlyContactType",
        "answerString": "Patient"
      }
    ]
  },

  "Contact Phone Numbers",
  {
    "id": "contactHomePhone",
    "t": "Home Phone",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "contactCellPhone",
    "t": "Cell Phone",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "preferredContactPhone",
    "t": "Preferred Contact Phone",
    "type": "checkbox",
    "options": ["Home Phone", "Cell Phone"],
    "req": True
  },

  {
    "id": "contactEmail",
    "t": "Email Address",
    "type": "string",
    "req": False,
    "value": ""
  }
]
    }
}

formDict[3] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "initial_information_form_2",
        "items": [
  "Insurance Information",
  {
    "id": "medicareNumber",
    "t": "Medicare #",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "medicaidNumber",
    "t": "Medicaid #",
    "type": "string",
    "req": False,
    "value": ""
  },

  "Primary Insurance (Insurance 1)",
  {
    "id": "insurance1Name",
    "t": "Insurance 1 - Name",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "insurance1Id",
    "t": "Insurance 1 - ID #",
    "type": "string",
    "req": True,
    "value": ""
  },
  {
    "id": "insurance1RxBin",
    "t": "Insurance 1 - RX BIN",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance1RxPcn",
    "t": "Insurance 1 - RX PCN",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance1RxGroup",
    "t": "Insurance 1 - RX GROUP",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance1Phone",
    "t": "Insurance 1 - Customer Service Phone Number",
    "type": "string",
    "req": False,
    "value": ""
  },

  "Secondary Insurance (Insurance 2)",
  {
    "id": "insurance2Name",
    "t": "Insurance 2 - Name",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance2Id",
    "t": "Insurance 2 - ID #",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance2RxBin",
    "t": "Insurance 2 - RX BIN",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance2RxPcn",
    "t": "Insurance 2 - RX PCN",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance2RxGroup",
    "t": "Insurance 2 - RX GROUP",
    "type": "string",
    "req": False,
    "value": ""
  },
  {
    "id": "insurance2Phone",
    "t": "Insurance 2 - Customer Service Phone Number",
    "type": "string",
    "req": False,
    "value": ""
  }
]

    }    
}

# formDict[4] = {
#   "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#   "questionnaire": {
#     "name": "financially_responsible_person_form",
#     "items": [
#       "Financially Responsible Person Information",
#       {
#         "id": "responsibleName",
#         "t": "Name",
#         "type": "string",
#         "req": true,
#         "value": ""
#       },
#       {
#         "id": "responsibleRelationship",
#         "t": "Relationship",
#         "type": "coding",
#         "req": true,
#         "opts": [
#           {
#             "code": "self",
#             "display": "Self"
#           },
#           {
#             "code": "spouse_partner",
#             "display": "Spouse/Partner"
#           },
#           {
#             "code": "poa",
#             "display": "Power of Attorney (POA)"
#           },
#           {
#             "code": "guardian_family",
#             "display": "Guardian/Family"
#           },
#           {
#             "code": "other",
#             "display": "Other"
#           }
#         ]
#       },
#       {
#         "id": "responsibleAddress",
#         "t": "Address",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "responsiblePhone",
#         "t": "Phone",
#         "type": "string",
#         "req": true,
#         "value": ""
#       }
#     ]
#   }
# }

# formDict[5] = {
#   "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#   "questionnaire": {
#     "name": "current_pharmacy_information_form",
#     "items": [
#       "Current Pharmacy Information",
#       "Note: The numbers (1–4) are used to identify which pharmacy your medications are from on the medication list page.",

#       {
#         "id": "pharmacy1Name",
#         "t": "Pharmacy 1 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy1Phone",
#         "t": "Pharmacy 1 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy1Fax",
#         "t": "Pharmacy 1 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "pharmacy2Name",
#         "t": "Pharmacy 2 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy2Phone",
#         "t": "Pharmacy 2 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy2Fax",
#         "t": "Pharmacy 2 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "pharmacy3Name",
#         "t": "Pharmacy 3 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy3Phone",
#         "t": "Pharmacy 3 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy3Fax",
#         "t": "Pharmacy 3 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "pharmacy4Name",
#         "t": "Pharmacy 4 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy4Phone",
#         "t": "Pharmacy 4 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "pharmacy4Fax",
#         "t": "Pharmacy 4 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       }
#     ]
#   }
# }

# formDict[6] = {
#   "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#   "questionnaire": {
#     "name": "prescriber_information_form",
#     "items": [
#       "Prescriber Information",
#       "Note: The numbers (1–6) are used to identify which prescriber your medications are from on the medication list page.",

#       {
#         "id": "prescriber1Name",
#         "t": "Prescriber 1 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Specialty",
#         "t": "Prescriber 1 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Phone",
#         "t": "Prescriber 1 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Fax",
#         "t": "Prescriber 1 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "prescriber2Name",
#         "t": "Prescriber 2 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Specialty",
#         "t": "Prescriber 2 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Phone",
#         "t": "Prescriber 2 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Fax",
#         "t": "Prescriber 2 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "prescriber3Name",
#         "t": "Prescriber 3 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Specialty",
#         "t": "Prescriber 3 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Phone",
#         "t": "Prescriber 3 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Fax",
#         "t": "Prescriber 3 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "prescriber4Name",
#         "t": "Prescriber 4 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Specialty",
#         "t": "Prescriber 4 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Phone",
#         "t": "Prescriber 4 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Fax",
#         "t": "Prescriber 4 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "prescriber5Name",
#         "t": "Prescriber 5 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Specialty",
#         "t": "Prescriber 5 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Phone",
#         "t": "Prescriber 5 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Fax",
#         "t": "Prescriber 5 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       {
#         "id": "prescriber6Name",
#         "t": "Prescriber 6 - Name",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Specialty",
#         "t": "Prescriber 6 - Specialty",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Phone",
#         "t": "Prescriber 6 - Phone",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Fax",
#         "t": "Prescriber 6 - Fax",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },

#       "Upcoming Appointments",
#       {
#         "id": "upcomingAppointment1",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment2",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment3",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment4",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": false,
#         "value": ""
#       }
#     ]
#   }
# }

# formDict[7] = {
#   "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#   "questionnaire": {
#     "name": "additional_notes_form",
#     "items": [
#       "Notes",
#       {
#         "id": "userNotes",
#         "t": "Please enter any additional notes here",
#         "type": "string",
#         "req": false,
#         "value": ""
#       }
#     ]
#   }
# }


# formDict[8] = {
#   "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#   "questionnaire": {
#     "name": "active_medication_list_form",
#     "items": [
#       "Active Medication List",
#       "Patient: ___________   DOB: ___________   Sign Up Date: ___________",
#       {
#         "id": "noKnownDrugAllergies",
#         "t": "No Known Drug Allergies",
#         "type": "boolean",
#         "req": false
#       },
#       {
#         "id": "drugAllergies",
#         "t": "Drug Allergies",
#         "type": "string",
#         "req": false,
#         "value": ""
#       },
#       "Medications (Pharm # to Req Only)"
#     ].concat(
#       Array.from({length: 10}, (_, i) => {
#         const n = i + 1;
#         return {
#           "id": `medication${n}`,
#           "t": `Medication ${n}`,
#           "type": "group",
#           "req": false,
#           "items": [
#             {"id": `med${n}PharmNumber`, "t": "Pharm #", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}DrNumber`, "t": "Dr #", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}RxNumber`, "t": "Rx #", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}Name`, "t": "Medication (name, strength, form, IR/ER/etc.)", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}SigNumber`, "t": "SIG #", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}LastRF`, "t": "R/F Last", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}QtyOnHand`, "t": "R/F Qty on Hand", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}DoseTime`, "t": "Dose Time (A, N, P, B)", "type": "string", "req": false, "value": ""},
#             {"id": `med${n}ReqOnly`, "t": "Req Only?", "type": "boolean", "req": false}
#           ]
#         };
#       })
#     )
#   }
# }