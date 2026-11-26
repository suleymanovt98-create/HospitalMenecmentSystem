from models.person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID 
        self._bloodGroup = bloodGroup  
        self.__medicalHistory = medicalHistory 

    def showInfo(self):
        super().showInfo()
        print(f"PatientID:{self.patientID}\nbloodGroup:{self._bloodGroup}\nMedicalHistory:{self.__medicalHistory}")

    def getMedicalHistory(self):
        return self.__medicalHistory

    def updateMedicalHistory(self):
        return self._bloodGroup




