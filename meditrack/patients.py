# Create `meditrack/patients.py`. At the top, import your own modules:
#   `from . import data` and `from . import utils`.

# In `patients.py`, write:
#   ```python
#   def add_patient(name, dob, gender, blood_group, *allergies, **extra):
#   ```
#   It should:
#   - reject invalid blood groups (raise `ValueError`)
#   - clean the name and generate a fresh id
#   - turn `*allergies` into a **set**
#   - read optional vitals from `**extra` using `.get(key, default)`
#   - append the new dict to `data.PATIENTS` and return it


from . import data
from . import utils

def add_patient(name, dob, gender, blood_group, *allergies, **extra):
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"Invalid blood group: {blood_group}")

    patient = {
        "id": utils.generate_patient_id(),
        "name": "Aarav Sharma",
        "dob": "1990-05-14",
        "gender": "M",
        "blood_group": "O+",
        "allergies": set(allergies),          # set
        "vitals": {                                    # nested dict
            "height_cm": extra.get("height_cm", 0.0),
            "weight_kg": 82.0,
            "systolic": 128,
            "diastolic": 84,
            "heart_rate": 78,
            "temperature_c": 37.0,
        },
        "visits": [],                                  # list of tuples       
    }
    data.PATIENTS.append(patient)
    return patient

# ==========================================================================================================================================

# In `patients.py`, write:
#   - `find_by_id(patient_id)` → loop through patients, `return` on the first match,
#     else return `None`.
#   - `search_by_name(keyword)` → loop through patients, `continue` when the name
#     doesn't contain the keyword (case-insensitive), collect the rest into a list.


def find_by_id(patient_id):
    for patient in data.PATIENTS:
        if patient["id"] == patient_id:
            return patient
    return None

def search_by_name(keyword):
    keyword = keyword.lower().strip()
    matches = []
    for patient in data.PATIENTS:
        if keyword not in patient["name"].lower():
            continue
        matches.append(patient)
    return matches   

# ==========================================================================================================================================

# Write `add_visit(patient_id, date=None, *reasons)` that:
#   - finds the patient (return `False` if missing)
#   - defaults `date` to today's date when not given
#   - joins the `*reasons` into one string
#   - appends a `(date, reason)` **tuple** to that patient's `visits`

def add_visit(patient_id, date=None, *reasons):
    patient = find_by_id(patient_id)
    if patient is None:
        return False
    date = date or utils.today_str()   
    reason = ", ".join(reasons) if reasons else "General consultation"   
    patient["visits"].append((date, reason))   
    return True

# ==========================================================================================================================================

# Write `all_allergies()` that loops over every patient and returns
#   the **union** of all their allergy sets.

def all_allergies():
    combined = set()
    for patient in data.PATIENTS:
        combined |= patient["allergies"]
    return combined


def add_patient(name, dob, gender, blood_group, *allergies, **extra):
    """Create a patient record and store it.

    Shows EVERY parameter kind
    - name, dob, gender, blood_group : positional/keyword
    - *allergies                     : arbitrary positional args -> tuple -> set
    - **extra                        : arbitrary keyword args -> dict
    """
    if not utils.is_valid_blood_group(blood_group):
        raise ValueError(f"Invalid blood group: {blood_group}")

    patient = {
        "id": utils.generate_patient_id(),
        "name": utils.clean_name(name),
        "dob": dob,
        "gender": gender.upper(),
        "blood_group": blood_group.strip().upper(),
        "allergies": set(a.lower() for a in allergies),
        "vitals": {
            "height_cm": extra.get("height_cm", 0.0),
            "weight_kg": extra.get("weight_kg", 0.0),
            "systolic": extra.get("systolic", 120),
            "diastolic": extra.get("diastolic", 80),
            "heart_rate": extra.get("heart_rate", 72),
            "temperature_c": extra.get("temperature_c", 36.6),
        },
        "visits": [],
    }
    data.PATIENTS.append(patient)
    return patient