
def calculate_bmi(weight_kg, height_cm):
    if height_cm <= 0 or weight_kg <= 0:
        return 0.0
    height_m = height_cm / 100      # Convert cm to metres
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

print(calculate_bmi(90, 175))


def bmi_category(bmi):
    if bmi <= 0:
        return "N/A"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def bp_category(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic < 130 and diastolic < 80:
        return "Elevated"
    elif systolic < 140 and diastolic < 90:
        return "Hypertension Stage 1"
    else:
        return "Hypertension Stage 2"


def has_fever(temperature_c):
    return temperature_c >= 38.0


def risk_score(patient):
    v = patient["vitals"]
    bmi = calculate_bmi(v["weight_kg"], v["height_cm"])
    score = 0

    if bmi >= 30:
        score += 30
    elif bmi >= 25:
        score += 15

    stage = bp_category(patient["systolic"], patient["diastolic"])

    if stage == "Hypertension Stage 2":
        score += 35
    elif stage == "Hypertension Stage 1":
        score += 20
    elif stage == "Elevated":
        score += 10

    if v["heart_rate"] > 100 or v["heart_rate"] < 50:
        score += 15

    if has_fever(v["temperature_c"]):
        score += 10

    return min((score, 100))


def risk_label(score):
    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MODERATE"
    else:
        return "LOW"






if __name__ == '__main__':
    PATIENTS = [
    {
        "id": "PAT-1001-4821",
        "name": "Aarav Sharma",
        "dob": "1990-05-14",
        "gender": "M",
        "blood_group": "O+",
        "allergies": {"penicillin", "dust"},          # set
        "vitals": {                                    # nested dict
            "height_cm": 175.0,
            "weight_kg": 82.0,
            "systolic": 128,
            "diastolic": 84,
            "heart_rate": 78,
            "temperature_c": 37.0,
        },
        "visits": [                                    # list of tuples
            ("2026-06-10", "Routine checkup"),
            ("2026-07-02", "Fever"),
        ],
    },
    {
        "id": "PAT-1002-7734",
        "name": "Diya Patel",
        "dob": "1985-11-22",
        "gender": "F",
        "blood_group": "A+",
        "allergies": set(),                            # empty set
        "vitals": {
            "height_cm": 162.0,
            "weight_kg": 55.0,
            "systolic": 118,
            "diastolic": 76,
            "heart_rate": 70,
            "temperature_c": 36.6,
        },
        "visits": [("2026-07-15", "Migraine")],
    },
    {
        "id": "PAT-1003-9012",
        "name": "Kabir Nair",
        "dob": "1972-02-08",
        "gender": "M",
        "blood_group": "B-",
        "allergies": {"sulfa"},
        "vitals": {
            "height_cm": 168.0,
            "weight_kg": 95.0,
            "systolic": 148,
            "diastolic": 96,
            "heart_rate": 88,
            "temperature_c": 37.4,
        },
        "visits": [
            ("2026-05-30", "High BP follow-up"),
            ("2026-06-28", "Chest discomfort"),
            ("2026-07-20", "Medication review"),
        ],
    },
]
    

# print(risk_score(patient))
