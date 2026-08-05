from . import data
from . import utils


def add_patient(name, dob, gender, blood_group, *allergies, **extra):
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"Invalid blood group: {blood_group}")

    patient = {
        "id": utils.generate_patient_id(),
        "name": name,
        "dob": dob,
        "gender": gender,
        "blood_group": blood_group,
        "allergies": set(allergies),
        "vitals": {
            "height_cm": extra.get("height cm",0.0),
            "weight_kg": 82.0,
            "systolic": 128,
            "diastolic": 84,
            "heart_rate": 78,
            "temperature_c": 37.0,
        },
        "visits": [],
        **extra,
    }
    data.PATIENTS.append(patient)
    return patient
