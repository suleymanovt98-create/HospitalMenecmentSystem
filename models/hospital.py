from models.appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
      self.doctors.append(doctor)

    def addPatient(self, patient):
        self.patients.append(patient)

    def showDoctors(self):
        for doctor in self.doctors:
            doctor.showInfo()

    def showPatients(self):
        for patient in self.patients:
            patient.showInfo()
           
    def createAppointment(self, doctorID, patientID, date):
        doctor = None
        patient = None

        for d in self.doctors:
            if d.doctorID == doctorID:
                doctor = d

        for p in self.patients:
            if p.patientID == patientID:
                patient = p

        if doctor is None or patient is None:
            print("Hekim və ya xeste tapilmadi.")
            return

        appointmentID = len(self.appointments) + 1
        self.appointments.append(Appointment(appointmentID, doctor, patient, date))

    def showAppointments(self):
        for appointment in self.appointments:
            appointment.showInfo()