import random
from datetime import datetime, timedelta


VALID_BLOOD_GROUPS = frozenset(
    {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
)

# Converting raw name into a better format
def clean_name(raw_name):
    return " ".join(raw_name.strip().split()).title()

# print(clean_name("   john  DOE"))


# Check wheter the bloodgroup exists in VALID_BLOOD_GROUPS
def is_valid_blood_group(bg):
    return bg.strip().upper() in VALID_BLOOD_GROUPS


_id_counter = 1000
def generate_patient_id():
    global _id_counter
    _id_counter += 1
    suffix = random.randint(1000, 9999)
    return f"PAT-{_id_counter}-{suffix}"





def today_str():
    return datetime.now().strftime("%Y-%m-%d")

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.now()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


print(clean_name("john DOE"))
print (is_valid_blood_group('o-'))
print(generate_patient_id())
print(type(today_str()))
print(calculate_age('2000-08-04'))

