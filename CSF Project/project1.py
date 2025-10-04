# Hospital Appointment Booking System
# Author: Sanchit upneja
# Date: 04-10-2025

import random

def check_availability(doctor, date):
    """
    Checks whether the doctor is available on the given date.
    For simplicity, we hardcode one unavailable slot.
    """
    if doctor.lower() == "Dr.Rajesh" and date == "05-10-2025":
        return False
    return True

def book_appointment(name, doctor, date):
    """
    Books an appointment and generates a unique appointment ID.
    """
    appointment_id = f"APT-{random.randint(1000, 9999)}"
    # In a real system, we'd save this data to a database
    return appointment_id

# ---- Main Program ----
print(" Welcome to Hospital Appointment Booking System")

patient_name =input("Enter your full name: ")
patient_contact = int(input ("Enter your contact number: "))
preferred_doctor = input("Enter preferred doctor name: ")
preferred_date =int(input("Enter appointment date (DD-MM-YYYY): "))

# Step 1: Check availability
if check_availability(preferred_doctor, preferred_date):
    # Step 2: Book appointment
    appointment_id = book_appointment(patient_name, preferred_doctor, preferred_date)
    print(f"Appointment confirmed! Your Appointment ID is {appointment_id}")
else:
    print(" Sorry, no available slots for the selected doctor and date.")