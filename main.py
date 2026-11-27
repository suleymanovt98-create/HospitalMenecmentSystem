from models.hospital import Hospital
from models.doctor import Doctor
from models.pasient import Patient

hospital = Hospital("Central Hospital")

while True:
    print("\n===== Hospital Management System =====")
    print("1. Add doctor")
    print("2. Add patient")
    print("3. Show doctors")
    print("4. Show patients")
    print("5. Create appointment")
    print("6. Show appointments")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        try:
            doctorID = int(input("Doctor ID: "))

            exists = False
            for d in hospital.doctors:
                if d.doctorID == doctorID:
                    exists = True

            if exists:
                print("This doctor ID already exists.")
            else:
                name = input("Name: ")
                surname = input("Surname: ")
                age = int(input("Age: "))
                phone = input("Phone: ")
                specialization = input("Specialization: ")
                experience = int(input("Experience (years): "))

                doctor = Doctor(name, surname, age, phone, doctorID, specialization, experience)
                hospital.addDoctor(doctor)
                print("Doctor added.")
        except ValueError:
            print("Error: ID, age and experience must be numbers.")
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "2":
        try:
            patientID = int(input("Patient ID: "))

            exists = False
            for p in hospital.patients:
                if p.patientID == patientID:
                    exists = True

            if exists:
                print("This patient ID already exists.")
            else:
                name = input("Name: ")
                surname = input("Surname: ")
                age = int(input("Age: "))
                phone = input("Phone: ")
                bloodGroup = input("Blood group: ")
                medicalHistory = input("Medical history: ")

                patient = Patient(name, surname, age, phone, patientID, bloodGroup, medicalHistory)
                hospital.addPatient(patient)
                print("Patient added.")
        except ValueError:
            print("Error: ID and age must be numbers.")
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "3":
        try:
            if len(hospital.doctors) == 0:
                print("No doctors yet.")
            else:
                hospital.showDoctors()
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "4":
        try:
            if len(hospital.patients) == 0:
                print("No patients yet.")
            else:
                hospital.showPatients()
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "5":
        try:
            if len(hospital.doctors) == 0 or len(hospital.patients) == 0:
                print("You need at least one doctor and one patient first.")
            else:
                doctorID = int(input("Doctor ID: "))
                patientID = int(input("Patient ID: "))
                date = input("Date (YYYY-MM-DD HH:MM): ")

                before = len(hospital.appointments)
                hospital.createAppointment(doctorID, patientID, date)
                if len(hospital.appointments) > before:
                    print("Appointment created.")
        except ValueError:
            print("Error: IDs must be numbers.")
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "6":
        try:
            if len(hospital.appointments) == 0:
                print("No appointments yet.")
            else:
                hospital.showAppointments()
        except Exception as e:
            print("Something went wrong:", e)

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Wrong choice, try again.")