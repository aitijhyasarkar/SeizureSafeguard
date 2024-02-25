# implementing AI voive facility [if needed in future]


import time
patient_features = {
    "High pressure": False,
    "High altitude brain wavelength": False,
    "Fast body movement": False,
    "High heart beat": False
}

family_contacts = ["Family Member 1", "Family Member 2", "Family Member 3"]

def activate_voice():
    """Activate voice"""
    response = input("Voice: Are you okay? (Yes/No): ").lower().strip()
    if response == "no":
        for contact in family_contacts:
            print(f"Sending beep sound to {contact}...")
            time.sleep(2)
        print("Notification sent to family members.")
    elif response == "yes":
        print("AI Voice: Please take care.")
        time.sleep(300) 
        activate_voice()

def check_patient_status():
    """Check if patient meets 2 out of 4 major features"""
    major_features_count = sum(1 for value in patient_features.values() if value)
    if major_features_count >= 2:
        activate_voice()


patient_features["High pressure"] = True
patient_features["High heart beat"] = True

check_patient_status()
