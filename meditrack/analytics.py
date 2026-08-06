from . import vitals
from functools import reduce



def high_risk_patients(patients, threshold=60):
    return list(
        filter(
            lambda patient:
            vitals.risk_score(patient) >= threshold,
            patients
        )
    )

def summarise(patients):
    return list(
        map(
            lambda patient: {
                "id": patient["id"],
                "name": patient["name"],
                "risk": vitals.risk_score(patient),
                "label": vitals.risk_label(
                    vitals.risk_score(patient)
                )
            },
            patients
        )
    )




def average_age(patients, calculate_age):

    if not patients:
        return 0

    ages = list(
        map(
            lambda patient:
            calculate_age(patient["dob"]),
            patients
        )
    )
    total = reduce(
        lambda total, age:
        total + age,
        ages
    )
    return round(total / len(ages), 1)