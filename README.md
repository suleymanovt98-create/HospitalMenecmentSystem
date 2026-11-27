Hospital Management System

A console-based hospital management system written in Python using Object-Oriented Programming (OOP). The project is split into separate modules, each with one clear responsibility. You can add doctors and patients, and book appointments that connect them.

Features
Add new doctors (ID, name, surname, age, phone, specialization, experience)
Add new patients (ID, name, surname, age, phone, blood group, medical history)
View all doctors and all patients
Create appointments between a doctor and a patient on a given date
View all appointments
Input validation with try / except (the program does not crash on wrong input)
Duplicate ID protection for doctors and patients
Project Structure
HospitalMenecmentSystem/
│
├── main.py                # Console menu, the entry point of the program
│
└── models/
    ├── person.py          # Base class: Person
    ├── doctor.py          # Doctor (inherits from Person)
    ├── pasient.py         # Patient (inherits from Person)
    ├── appointment.py     # Appointment (connects Doctor and Patient)
    └── hospital.py        # Hospital (stores and manages everything)
How the modules depend on each other
Person
  ├── Doctor
  └── Patient
         \       /
        Appointment
             |
          Hospital
             |
           main.py

Each module only depends on the ones above it, so the code stays clean and easy to extend.

OOP Concepts Used
Concept	Where it is used
Inheritance	Doctor and Patient inherit name, surname, age, phone from Person
super()	super().__init__(...) and super().showInfo() reuse the parent class code
Method overriding	Doctor and Patient override showInfo() from Person
Encapsulation	Patient uses a protected attribute _bloodGroup and a private attribute __medicalHistory with a getter
Composition	Appointment holds a Doctor object and a Patient object
Modularity	Every class lives in its own file inside the models package
Requirements
Python 3.8 or newer
No external libraries are needed
How to Run
Download or clone the project.
Open a terminal in the main project folder (the one that contains main.py and the models folder).
Run:
python main.py

Important: Always run main.py from the main folder. If you run files inside models/ directly, Python will not find the models package and you will get ModuleNotFoundError.

Usage

When the program starts, you will see this menu:

===== Hospital Management System =====
1. Add doctor
2. Add patient
3. Show doctors
4. Show patients
5. Create appointment
6. Show appointments
0. Exit
Example session
Choose 1 and add a doctor, for example: ID 1, Ali Hasanov, specialization Cardiologist.
Choose 2 and add a patient, for example: ID 1, Aysel Guliyeva, blood group A+.
Choose 5 and create an appointment using doctor ID 1, patient ID 1 and a date like 2025-01-15 10:00.
Choose 6 to see the appointment:
AppointmentID:1
Doctor:Ali Hasanov
Patient:Aysel Guliyeva
Date:2025-01-15 10:00
Error Handling
Typing letters where a number is expected (ID, age, experience) shows an error message instead of crashing the program.
Adding a doctor or patient with an ID that already exists is rejected.
Creating an appointment with a non-existing doctor or patient ID is rejected.
Creating an appointment before any doctor or patient exists shows a helpful message.
Known Limitations
Data is stored in memory only. When the program closes, all data is lost.
Patient.updateMedicalHistory() is not finished yet.
There is no option to edit or delete doctors, patients or appointments.
Future Improvements
Save and load data using a file (JSON) or a database (SQLite)
Edit and delete doctors, patients and appointments
Prevent two appointments for the same doctor at the same time
Search doctors and patients by name or specialization
Finish the medical history update feature
Add a graphical interface (Tkinter) or a web version (Flask)
Author

Taleh Suleymanov

Created as a practice project for learning Python and OOP.
