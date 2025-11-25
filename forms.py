userDict = {}

userDict["1234567890"] = {"name": "John Smith"}
userDict["2345678901"] = {"name": "Emily Johnson"}
userDict["3456789012"] = {"name": "Michael Brown"}
userDict["4567890123"] = {"name": "Sarah Davis"}
userDict["5678901234"] = {"name": "David Wilson"}
userDict["6789012345"] = {"name": "Olivia Martinez"}
userDict["7890123456"] = {"name": "James Taylor"}
userDict["8901234567"] = {"name": "Sophia Anderson"}
userDict["9012345678"] = {"name": "Daniel Thomas"}
userDict["0123456789"] = {"name": "Ava Hernandez"}

formDict = {}

# Page 2

formDict[1] = {
  "questionnaire": {
    "name": "Personal Information",
    "items": [
      {
        "id": "firstName",
        "t": "First Name",
        "type": "string",
        "req": True
      },
      {
        "id": "lastName",
        "t": "Last Name",
        "type": "string",
        "req": True
      },
      {
        "id": "biologicalSex",
        "t": "Biological Sex",
        "type": "select",
        "options": ["Male", "Female"],
        "req": True
      },
      {
        "id": "dateOfBirth",
        "t": "Date of Birth",
        "type": "string",
        "req": True
      },
      {
        "id": "ssn",
        "t": "Social Security Number",
        "type": "string",
        "req": False
      }
    ]
  }
}

formDict[2] = {
  "questionnaire": {
  "name": "contact_details",
  "items": [
    {
      "id": "emailAddress",
      "t": "Email Address",
      "type": "string",
      "req": True
    },
    {
      "id": "phoneNumber",
      "t": "Phone Number",
      "type": "string",
      "req": True
    },
    {
      "id": "numberType",
      "t": "Number Type",
      "type": "select",
      "options": ["Cell", "Home"],
      "default": "Cell",
      "req": True
    },
    {
      "id": "drugAllergies",
      "t": "Drug Allergies",
      "type": "string",
      "req": False
    },
    {
      "id": "preferredPackaging",
      "t": "Preferred Packaging Type",
      "type": "multiselect",
      "options": [
        "Vial in Multi-Pack (VIMP)",
        "Bottles",
        "Spanish Label",
        "EZ Caps"
      ],
      "req": False
    }
  ]
}
}

formDict[3] = {
  "questionnaire": {
  "name": "shipping_address",
  "items": [
    {
      "id": "streetName",
      "t": "Street Name",
      "type": "string",
      "req": True
    },
    {
      "id": "city",
      "t": "City",
      "type": "string",
      "req": True
    },
    {
      "id": "state",
      "t": "State",
      "type": "string",
      "req": True
    },
    {
      "id": "zipCode",
      "t": "Zip Code",
      "type": "string",
      "req": True
    },

    {
      "id": "hasPOBox",
      "t": "Do you have a PO Box?",
      "type": "select",
      "options": ["Yes", "No"],
      "default": "No"
    },
    {
      "id": "poBox",
      "t": "PO Box",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "hasPOBox",
        "equals": "Yes"
      }
    },

    {
      "id": "billingSameAsShipping",
      "t": "Is billing address the same as shipping address?",
      "type": "select",
      "options": ["Yes", "No"],
      "default": "No"
    },

    {
      "id": "billingStreetName",
      "t": "Billing Street Name",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "billingSameAsShipping",
        "equals": "Yes"
      }
    },
    {
      "id": "billingCity",
      "t": "Billing City",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "billingSameAsShipping",
        "equals": "Yes"
      }
    },
    {
      "id": "billingState",
      "t": "Billing State",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "billingSameAsShipping",
        "equals": "Yes"
      }
    },
    {
      "id": "billingZipCode",
      "t": "Billing Zip Code",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "billingSameAsShipping",
        "equals": "Yes"
      }
    },

    {
      "id": "managesOwnMedications",
      "t": "Do you manage your own medications?",
      "type": "select",
      "options": ["Yes", "No"],
      "default": "Yes"
    },

    {
      "id": "medManagerName",
      "t": "Medication Manager Name",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "managesOwnMedications",
        "equals": "No"
      }
    },
    {
      "id": "medManagerRelationship",
      "t": "Medication Manager Relationship",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "managesOwnMedications",
        "equals": "No"
      }
    },
    {
      "id": "medManagerPhone",
      "t": "Medication Manager Phone",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "managesOwnMedications",
        "equals": "No"
      }
    },
    {
      "id": "medManagerEmail",
      "t": "Medication Manager Email",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "managesOwnMedications",
        "equals": "No"
      }
    }
  ]
}

}

formDict[4] = {
  "questionnaire": {
  "name": "monthly_contact_information",
  "items": [
    {
      "id": "monthlyContact",
      "t": "Monthly Contact",
      "type": "select",
      "options": ["Patient (yourself)", "Family Member", "Caregiver"]
    },

    {
      "id": "contactAware",
      "t": "Contact is aware we must speak with them monthly and understands service may be interrupted if we are unable to contact them",
      "type": "select",
      "options": ["Yes", "No"]
    },

    {
      "id": "contactName",
      "t": "Contact Name",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "monthlyContact",
        "notEquals": "Patient (yourself)"
      }
    },

    {
      "id": "contactPhoneType",
      "t": "Preferred Contact Number Type",
      "type": "select",
      "options": ["Cell", "Home"],
      "req": True,
      "conditional": {
        "field": "monthlyContact",
        "notEquals": "Patient (yourself)"
      }
    },

    {
      "id": "contactPhone",
      "t": "Contact Phone Number",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "monthlyContact",
        "notEquals": "Patient (yourself)"
      }
    },

    {
      "id": "contactEmail",
      "t": "Contact Email Address",
      "type": "string",
      "req": True,
      "conditional": {
        "field": "monthlyContact",
        "notEquals": "Patient (yourself)"
      }
    }
  ]
}

}

# PAGE 3 compared to website
formDict[5] = {
"questionnaire": {
"name": "insurance_information",
"items": [
{
"id": "medicareNumber",
"t": "Medicare Number (if applicable)",
"type": "string"
},
{
"id": "medicaidNumber",
"t": "Medicaid Number (if applicable)",
"type": "string"
},
{
"id": "hasInsurance1",
"t": "Do you have insurance coverage?",
"type": "select",
"options": ["Yes", "No"]
},
{
"id": "insurance1Name",
"t": "Insurance Company Name",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance1Id",
"t": "Insurance ID number",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance1RxBin",
"t": "RX BIN Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance1RxPcn",
"t": "RX PCN Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance1RxGroup",
"t": "RX Group Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance1CustomerService",
"t": "Insurance Company Customer Service Phone Number",
"type": "string",
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "hasInsurance2",
"t": "Do you have a second insurance coverage?",
"type": "select",
"options": ["Yes", "No"],
"conditional": {
"field": "hasInsurance1",
"equals": "Yes"
}
},
{
"id": "insurance2Name",
"t": "Insurance Company Name",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
},
{
"id": "insurance2Id",
"t": "Insurance ID / Member Number",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
},
{
"id": "insurance2RxBin",
"t": "RX BIN Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
},
{
"id": "insurance2RxPcn",
"t": "RX PCN Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
},
{
"id": "insurance2RxGroup",
"t": "RX Group Number (found on your insurance card)",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
},
{
"id": "insurance2CustomerService",
"t": "Insurance Company Customer Service Phone Number",
"type": "string",
"conditional": {
"field": "hasInsurance2",
"equals": "Yes"
}
}
]
}
}


formDict[6] = {
  "questionnaire": {
  "name": "financially_responsible_person",
  "items": [
    {
      "id": "responsibleName",
      "t": "Name",
      "type": "string"
    },
    {
      "id": "responsibleRelationship",
      "t": "What is the financially responsible person's relationship to yourself",
      "type": "select",
      "options": ["Self", "Spouse/Partner", "Power of Attorney (POA)", "Guardian/Family", "Other"]
    },
    {
      "id": "responsibleRelationshipOther",
      "t": "Please list the relationship",
      "type": "string",
      "conditional": {
        "field": "responsibleRelationship",
        "equals": "Other"
      }
    },
    {
      "id": "responsibleAddress",
      "t": "Address",
      "type": "string"
    },
    {
      "id": "responsiblePhone",
      "t": "Phone Number",
      "type": "string",
      "req": True
    },
    {
      "id": "responsiblePhoneType",
      "t": "Phone Number Type",
      "type": "select",
      "options": ["Cell", "Home"],
      "default": "Cell",
      "req": True
    }
  ]
}

}

# page 4 on the website
formDict[7]= {
  "questionnaire": {
    "name": "current_pharmacy_information",
    "items": [
      {
        "id": "has_pharmacy",
        "t": "Do you have a pharmacy that currently dispenses your medications?",
        "type": "select",
        "options": ["Yes", "No"]
      },
      {
        "id": "pharmacy_1_name",
        "t": "Pharmacy 1 Name",
        "type": "string",
        "conditional": { "field": "has_pharmacy", "equals": "Yes" }
      },
      {
        "id": "pharmacy_1_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "has_pharmacy", "equals": "Yes" }
      },
      {
        "id": "pharmacy_1_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "has_pharmacy", "equals": "Yes" }
      },
      {
        "id": "another_pharmacy_1",
        "t": "Do you have another pharmacy that currently dispenses your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "has_pharmacy", "equals": "Yes" }
      },
      {
        "id": "pharmacy_2_name",
        "t": "Pharmacy 2 Name",
        "type": "string",
        "conditional": { "field": "another_pharmacy_1", "equals": "Yes" }
      },
      {
        "id": "pharmacy_2_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_1", "equals": "Yes" }
      },
      {
        "id": "pharmacy_2_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_1", "equals": "Yes" }
      },
      {
        "id": "another_pharmacy_2",
        "t": "Do you have another pharmacy that currently dispenses your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_pharmacy_1", "equals": "Yes" }
      },
      {
        "id": "pharmacy_3_name",
        "t": "Pharmacy 3 Name",
        "type": "string",
        "conditional": { "field": "another_pharmacy_2", "equals": "Yes" }
      },
      {
        "id": "pharmacy_3_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_2", "equals": "Yes" }
      },
      {
        "id": "pharmacy_3_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_2", "equals": "Yes" }
      },
      {
        "id": "another_pharmacy_3",
        "t": "Do you have another pharmacy that currently dispenses your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_pharmacy_2", "equals": "Yes" }
      },
      {
        "id": "pharmacy_4_name",
        "t": "Pharmacy 4 Name",
        "type": "string",
        "conditional": { "field": "another_pharmacy_3", "equals": "Yes" }
      },
      {
        "id": "pharmacy_4_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_3", "equals": "Yes" }
      },
      {
        "id": "pharmacy_4_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_pharmacy_3", "equals": "Yes" }
      }
    ]
  }
}

formDict[8] = {
  "questionnaire": {
    "name": "current_prescriber_information",
    "items": [
      {
        "id": "has_prescriber",
        "t": "Do you have a prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"]
      },
      {
        "id": "prescriber_1_name",
        "t": "Prescriber 1 Name",
        "type": "string",
        "conditional": { "field": "has_prescriber", "equals": "Yes" }
      },
      {
        "id": "prescriber_1_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "has_prescriber", "equals": "Yes" }
      },
      {
        "id": "prescriber_1_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "has_prescriber", "equals": "Yes" }
      },
      {
        "id": "prescriber_1_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "has_prescriber", "equals": "Yes" }
      },
      {
        "id": "another_prescriber_1",
        "t": "Do you have another prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "has_prescriber", "equals": "Yes" }
      },
      {
        "id": "prescriber_2_name",
        "t": "Prescriber 2 Name",
        "type": "string",
        "conditional": { "field": "another_prescriber_1", "equals": "Yes" }
      },
      {
        "id": "prescriber_2_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "another_prescriber_1", "equals": "Yes" }
      },
      {
        "id": "prescriber_2_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_1", "equals": "Yes" }
      },
      {
        "id": "prescriber_2_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_1", "equals": "Yes" }
      },
      {
        "id": "another_prescriber_2",
        "t": "Do you have another prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_prescriber_1", "equals": "Yes" }
      },
      {
        "id": "prescriber_3_name",
        "t": "Prescriber 3 Name",
        "type": "string",
        "conditional": { "field": "another_prescriber_2", "equals": "Yes" }
      },
      {
        "id": "prescriber_3_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "another_prescriber_2", "equals": "Yes" }
      },
      {
        "id": "prescriber_3_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_2", "equals": "Yes" }
      },
      {
        "id": "prescriber_3_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_2", "equals": "Yes" }
      },
      {
        "id": "another_prescriber_3",
        "t": "Do you have another prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_prescriber_2", "equals": "Yes" }
      },
      {
        "id": "prescriber_4_name",
        "t": "Prescriber 4 Name",
        "type": "string",
        "conditional": { "field": "another_prescriber_3", "equals": "Yes" }
      },
      {
        "id": "prescriber_4_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "another_prescriber_3", "equals": "Yes" }
      },
      {
        "id": "prescriber_4_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_3", "equals": "Yes" }
      },
      {
        "id": "prescriber_4_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_3", "equals": "Yes" }
      },
      {
        "id": "another_prescriber_4",
        "t": "Do you have another prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_prescriber_3", "equals": "Yes" }
      },
      {
        "id": "prescriber_5_name",
        "t": "Prescriber 5 Name",
        "type": "string",
        "conditional": { "field": "another_prescriber_4", "equals": "Yes" }
      },
      {
        "id": "prescriber_5_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "another_prescriber_4", "equals": "Yes" }
      },
      {
        "id": "prescriber_5_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_4", "equals": "Yes" }
      },
      {
        "id": "prescriber_5_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_4", "equals": "Yes" }
      },
      {
        "id": "another_prescriber_5",
        "t": "Do you have another prescriber that currently manages your medications?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "another_prescriber_4", "equals": "Yes" }
      },
      {
        "id": "prescriber_6_name",
        "t": "Prescriber 6 Name",
        "type": "string",
        "conditional": { "field": "another_prescriber_5", "equals": "Yes" }
      },
      {
        "id": "prescriber_6_specialty",
        "t": "Specialty",
        "type": "string",
        "conditional": { "field": "another_prescriber_5", "equals": "Yes" }
      },
      {
        "id": "prescriber_6_phone",
        "t": "Phone Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_5", "equals": "Yes" }
      },
      {
        "id": "prescriber_6_fax",
        "t": "Fax Number",
        "type": "string",
        "conditional": { "field": "another_prescriber_5", "equals": "Yes" }
      }
    ]
  }
}

formDict[9] = {
  "questionnaire": {
    "name": "upcoming_appointments",
    "items": [
      {
        "id": "has_appointment_1",
        "t": "Do you have an upcoming appointment?",
        "type": "select",
        "options": ["Yes", "No"]
      },
      {
        "id": "appointment_1_prescriber",
        "t": "Prescriber for Appointment 1",
        "type": "string",
        "conditional": { "field": "has_appointment_1", "equals": "Yes" }
      },
      {
        "id": "appointment_1_date",
        "t": "Date for Appointment 1",
        "type": "string",
        "conditional": { "field": "has_appointment_1", "equals": "Yes" }
      },
      {
        "id": "has_appointment_2",
        "t": "Do you have another upcoming appointment?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "has_appointment_1", "equals": "Yes" }
      },
      {
        "id": "appointment_2_prescriber",
        "t": "Prescriber for Appointment 2",
        "type": "string",
        "conditional": { "field": "has_appointment_2", "equals": "Yes" }
      },
      {
        "id": "appointment_2_date",
        "t": "Date for Appointment 2",
        "type": "string",
        "conditional": { "field": "has_appointment_2", "equals": "Yes" }
      },
      {
        "id": "has_appointment_3",
        "t": "Do you have another upcoming appointment?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "has_appointment_2", "equals": "Yes" }
      },
      {
        "id": "appointment_3_prescriber",
        "t": "Prescriber for Appointment 3",
        "type": "string",
        "conditional": { "field": "has_appointment_3", "equals": "Yes" }
      },
      {
        "id": "appointment_3_date",
        "t": "Date for Appointment 3",
        "type": "string",
        "conditional": { "field": "has_appointment_3", "equals": "Yes" }
      },
      {
        "id": "has_appointment_4",
        "t": "Do you have another upcoming appointment?",
        "type": "select",
        "options": ["Yes", "No"],
        "conditional": { "field": "has_appointment_3", "equals": "Yes" }
      },
      {
        "id": "appointment_4_prescriber",
        "t": "Prescriber for Appointment 4",
        "type": "string",
        "conditional": { "field": "has_appointment_4", "equals": "Yes" }
      },
      {
        "id": "appointment_4_date",
        "t": "Date for Appointment 4",
        "type": "string",
        "conditional": { "field": "has_appointment_4", "equals": "Yes" }
      },
      {
        "id": "appointment_notes",
        "t": "Additional Notes for Appointments",
        "type": "string",
        "conditional": { "field": "has_appointment_1", "equals": "Yes" }
      }
    ]
  }
}

formDict[10] = {
"questionnaire": {
"name": "medication_information",
"items": [
{
"id": "has_medication_1",
"t": "Do you have a current home medication to enter?",
"type": "select",
"options": ["Yes", "No"]
},
{
"id": "medication_1_pharmacy",
"t": "Pharmacy",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_prescriber",
"t": "Prescriber",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_prescription_number",
"t": "Prescription Number",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_name",
"t": "Medication (Name, Strength, Form, Release Type)",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_directions",
"t": "Directions",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_refills",
"t": "Number of Refills",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_last_refill",
"t": "Last Refill Date",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_dose_time",
"t": "Dose Time",
"type": "select",
"options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_quantity",
"t": "Quantity of Medications on Hand",
"type": "string",
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
{
"id": "medication_1_refill_by_request",
"t": "Is this medication refilled by request only?",
"type": "select",
"options": ["Yes", "No"],
"conditional": { "field": "has_medication_1", "equals": "Yes" }
},
  {
    "id": "has_medication_2",
    "t": "Do you have another current home medication?",
    "type": "select",
    "options": ["Yes", "No"],
    "conditional": { "field": "has_medication_1", "equals": "Yes" }
  },
  {
    "id": "medication_2_pharmacy",
    "t": "Pharmacy",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_prescriber",
    "t": "Prescriber",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_prescription_number",
    "t": "Prescription Number",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_name",
    "t": "Medication (Name, Strength, Form, Release Type)",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_directions",
    "t": "Directions",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_refills",
    "t": "Number of Refills",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_last_refill",
    "t": "Last Refill Date",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_dose_time",
    "t": "Dose Time",
    "type": "select",
    "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_quantity",
    "t": "Quantity of Medications on Hand",
    "type": "string",
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
    "id": "medication_2_refill_by_request",
    "t": "Is this medication refilled by request only?",
    "type": "select",
    "options": ["Yes", "No"],
    "conditional": { "field": "has_medication_2", "equals": "Yes" }
  },
  {
  "id": "has_medication_3",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_2",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_3_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_4",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_3",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_4_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_5",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_4",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_5_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_6",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_5",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_6_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_7",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_6",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_7_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_8",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_7",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_8_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_9",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_8",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_9_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "has_medication_10",
  "t": "Do you have another current home medication?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_9",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_pharmacy",
  "t": "Pharmacy",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_prescriber",
  "t": "Prescriber",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_prescription_number",
  "t": "Prescription Number",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_name",
  "t": "Medication (Name, Strength, Form, Release Type)",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_directions",
  "t": "Directions",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_refills",
  "t": "Number of Refills",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_last_refill",
  "t": "Last Refill Date",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_dose_time",
  "t": "Dose Time",
  "type": "select",
  "options": ["Morning (A.M.)", "Noon", "Evening (P.M.)", "Bedtime"],
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_quantity",
  "t": "Quantity of Medications on Hand",
  "type": "string",
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
},
{
  "id": "medication_10_refill_by_request",
  "t": "Is this medication refilled by request only?",
  "type": "select",
  "options": ["Yes", "No"],
  "conditional": {
    "field": "has_medication_10",
    "equals": "Yes"
  }
}
]
}
}




# formDict[1] = {
#     "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#     "questionnaire": {
#         "name": "patient_information_form",
#         "items": [
#   "Patient Information",
#   {
#     "id": "patientName",
#     "t": "Patient Name",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "gender",
#     "t": "Gender",
#     "type": "checkbox",
#     "options": ["Male", "Female"],
#     "req": True
#   },
#   {
#     "id": "dob",
#     "t": "Date of Birth",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "ssn",
#     "t": "SSN",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "phone",
#     "t": "Phone",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "email",
#     "t": "Email",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },

#   "Allergies",
#   {
#     "id": "drugAllergies",
#     "t": "Drug Allergies",
#     "type": "checkbox",
#     "options": ["No Known Drug Allergies", "Drug Allergies"],
#     "req": False
#   },

#   "Packaging Preferences",
#   {
#     "id": "packagingType",
#     "t": "Packaging Type",
#     "type": "checkbox",
#     "options": ["VIMP", "Bottles", "Spanish"],
#     "req": False
#   },
#   {
#     "id": "ezCaps",
#     "t": "Patient requests EZ caps",
#     "type": "checkbox",
#     "options": ["Yes", "No"],
#     "req": False
#   },

#   "Shipping Address",
#   {
#     "id": "shippingStreet",
#     "t": "Street",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "shippingCounty",
#     "t": "County",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "shippingCity",
#     "t": "City",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "shippingState",
#     "t": "State",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "shippingZip",
#     "t": "ZIP Code",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },

#   "Billing Address",
#   {
#     "id": "billingStreet",
#     "t": "Street",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "billingCounty",
#     "t": "County",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "billingCity",
#     "t": "City",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "billingState",
#     "t": "State",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "billingZip",
#     "t": "ZIP Code",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },

#   "Medication Management",
#   {
#     "id": "manageOwnMedications",
#     "t": "Do you manage your own medications?",
#     "type": "checkbox",
#     "options": ["Yes", "No"],
#     "req": True
#   },
#   {
#     "id": "medManagerName",
#     "t": "Medication Manager Name",
#     "type": "string",
#     "req": True,
#     "value": "",
#     "when": [
#       {
#         "operator": "=",
#         "question": "manageOwnMedications",
#         "answerString": "No"
#       }
#     ]
#   },
#   {
#     "id": "medManagerRelationship",
#     "t": "Relationship to Patient",
#     "type": "string",
#     "req": True,
#     "value": "",
#     "when": [
#       {
#         "operator": "=",
#         "question": "manageOwnMedications",
#         "answerString": "No"
#       }
#     ]
#   },
#   {
#     "id": "medManagerPhone",
#     "t": "Medication Manager Phone",
#     "type": "string",
#     "req": True,
#     "value": "",
#     "when": [
#       {
#         "operator": "=",
#         "question": "manageOwnMedications",
#         "answerString": "No"
#       }
#     ]
#   },
#   {
#     "id": "medManagerEmail",
#     "t": "Medication Manager Email",
#     "type": "string",
#     "req": False,
#     "value": "",
#     "when": [
#       {
#         "operator": "=",
#         "question": "manageOwnMedications",
#         "answerString": "No"
#       }
#     ]
#   }
# ]

#     }
# }

# formDict[2] = {
#     "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#     "questionnaire": {
#         "name": "monthly_contact_information_form",
#         "items": [
#   "Monthly Contact Information",
#   {
#     "id": "monthlyContactType",
#     "t": "Monthly Contact is",
#     "type": "checkbox",
#     "options": ["Patient", "Family Member", "Other Caregiver"],
#     "req": True
#   },
#   {
#     "id": "contactAware",
#     "t": "Contact is aware we must speak with them monthly and understands service may be interrupted if we are unable to contact them",
#     "type": "checkbox",
#     "options": ["Yes", "No"],
#     "req": True
#   },
#   {
#     "id": "contactName",
#     "t": "Contact Name (if other than Patient)",
#     "type": "string",
#     "req": False,
#     "value": "",
#     "when": [
#       {
#         "operator": "!=",
#         "question": "monthlyContactType",
#         "answerString": "Patient"
#       }
#     ]
#   },

#   "Contact Phone Numbers",
#   {
#     "id": "contactHomePhone",
#     "t": "Home Phone",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "contactCellPhone",
#     "t": "Cell Phone",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "preferredContactPhone",
#     "t": "Preferred Contact Phone",
#     "type": "checkbox",
#     "options": ["Home Phone", "Cell Phone"],
#     "req": True
#   },

#   {
#     "id": "contactEmail",
#     "t": "Email Address",
#     "type": "string",
#     "req": False,
#     "value": ""
#   }
# ]
#     }
# }

# formDict[3] = {
#     "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#     "questionnaire": {
#         "name": "insurance_information_form",
#         "items": [
#   "Insurance Information",
#   {
#     "id": "medicareNumber",
#     "t": "Medicare #",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "medicaidNumber",
#     "t": "Medicaid #",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },

#   "Primary Insurance (Insurance 1)",
#   {
#     "id": "insurance1Name",
#     "t": "Insurance 1 - Name",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "insurance1Id",
#     "t": "Insurance 1 - ID #",
#     "type": "string",
#     "req": True,
#     "value": ""
#   },
#   {
#     "id": "insurance1RxBin",
#     "t": "Insurance 1 - RX BIN",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance1RxPcn",
#     "t": "Insurance 1 - RX PCN",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance1RxGroup",
#     "t": "Insurance 1 - RX GROUP",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance1Phone",
#     "t": "Insurance 1 - Customer Service Phone Number",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },

#   "Secondary Insurance (Insurance 2)",
#   {
#     "id": "insurance2Name",
#     "t": "Insurance 2 - Name",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance2Id",
#     "t": "Insurance 2 - ID #",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance2RxBin",
#     "t": "Insurance 2 - RX BIN",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance2RxPcn",
#     "t": "Insurance 2 - RX PCN",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance2RxGroup",
#     "t": "Insurance 2 - RX GROUP",
#     "type": "string",
#     "req": False,
#     "value": ""
#   },
#   {
#     "id": "insurance2Phone",
#     "t": "Insurance 2 - Customer Service Phone Number",
#     "type": "string",
#     "req": False,
#     "value": ""
#   }
# ]

#     }    
# }

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
#         "req": True,
#         "value": ""
#       },
#       {
#         "id": "responsibleRelationship",
#         "t": "Relationship",
#         "type": "coding",
#         "req": True,
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
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "responsiblePhone",
#         "t": "Phone",
#         "type": "string",
#         "req": True,
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
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy1Phone",
#         "t": "Pharmacy 1 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy1Fax",
#         "t": "Pharmacy 1 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "pharmacy2Name",
#         "t": "Pharmacy 2 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy2Phone",
#         "t": "Pharmacy 2 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy2Fax",
#         "t": "Pharmacy 2 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "pharmacy3Name",
#         "t": "Pharmacy 3 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy3Phone",
#         "t": "Pharmacy 3 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy3Fax",
#         "t": "Pharmacy 3 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "pharmacy4Name",
#         "t": "Pharmacy 4 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy4Phone",
#         "t": "Pharmacy 4 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "pharmacy4Fax",
#         "t": "Pharmacy 4 - Fax",
#         "type": "string",
#         "req": False,
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
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Specialty",
#         "t": "Prescriber 1 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Phone",
#         "t": "Prescriber 1 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber1Fax",
#         "t": "Prescriber 1 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "prescriber2Name",
#         "t": "Prescriber 2 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Specialty",
#         "t": "Prescriber 2 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Phone",
#         "t": "Prescriber 2 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber2Fax",
#         "t": "Prescriber 2 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "prescriber3Name",
#         "t": "Prescriber 3 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Specialty",
#         "t": "Prescriber 3 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Phone",
#         "t": "Prescriber 3 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber3Fax",
#         "t": "Prescriber 3 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "prescriber4Name",
#         "t": "Prescriber 4 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Specialty",
#         "t": "Prescriber 4 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Phone",
#         "t": "Prescriber 4 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber4Fax",
#         "t": "Prescriber 4 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "prescriber5Name",
#         "t": "Prescriber 5 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Specialty",
#         "t": "Prescriber 5 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Phone",
#         "t": "Prescriber 5 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber5Fax",
#         "t": "Prescriber 5 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       {
#         "id": "prescriber6Name",
#         "t": "Prescriber 6 - Name",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Specialty",
#         "t": "Prescriber 6 - Specialty",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Phone",
#         "t": "Prescriber 6 - Phone",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "prescriber6Fax",
#         "t": "Prescriber 6 - Fax",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },

#       "Upcoming Appointments",
#       {
#         "id": "upcomingAppointment1",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment2",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment3",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": False,
#         "value": ""
#       },
#       {
#         "id": "upcomingAppointment4",
#         "t": "Prescriber # ____ on ___________",
#         "type": "string",
#         "req": False,
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
#         "req": False,
#         "value": ""
#       }
#     ]
#   }
# }

# formDict[8] = {
#     "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
#     "questionnaire": {
#         "name": "active_medication_list_form",
#         "items": [
#             "Active Medication List",
#             {
#                 "id": "patientName",
#                 "t": "Patient Name",
#                 "type": "string",
#                 "req": True,
#                 "value": ""
#             },
#             {
#                 "id": "dob",
#                 "t": "Date of Birth",
#                 "type": "string",
#                 "req": True,
#                 "value": ""
#             },
#             {
#                 "id": "signUpDate",
#                 "t": "Sign Up Date",
#                 "type": "string",
#                 "req": True,
#                 "value": ""
#             },
#             {
#                 "id": "noKnownDrugAllergies",
#                 "t": "No Known Drug Allergies",
#                 "type": "boolean",
#                 "req": False
#             },
#             {
#                 "id": "drugAllergies",
#                 "t": "Drug Allergies",
#                 "type": "string",
#                 "req": False,
#                 "value": ""
#             },
#             "Medications (Pharm # to Req Only)"
#         ] + [
#             {
#                 "id": f"medication{n}",
#                 "t": f"Medication {n}",
#                 "type": "group",
#                 "req": False,
#                 "items": [
#                     {"id": f"med{n}PharmNumber", "t": "Pharm #", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}DrNumber", "t": "Dr #", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}RxNumber", "t": "Rx #", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}Name", "t": "Medication (name, strength, form, IR/ER/etc.)", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}SigNumber", "t": "SIG #", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}LastRF", "t": "R/F Last", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}QtyOnHand", "t": "R/F Qty on Hand", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}DoseTime", "t": "Dose Time (A, N, P, B)", "type": "string", "req": False, "value": ""},
#                     {"id": f"med{n}ReqOnly", "t": "Req Only?", "type": "boolean", "req": False}
#                 ]
#             } for n in range(1, 11)
#         ]
#     }
# }