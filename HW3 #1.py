class Patient():
    def __init__(self, name, hospital):
        self.cost = 0
        self.type = ''
        self.name = name
        self.hospital = hospital

    def discharge(self):
        self.hospital.cost += self.cost
        self.hospital.patients.remove(self)
        print(self.name, self.type)


class EmergencyPatient(Patient):
    def __init__(self, name, hospital):
        self.cost = 1000.0
        self.type = "Emergency"
        self.name = name
        self.hospital = hospital


class HospitalizedPatient(Patient):
    def __init__(self, name, hospital):
        self.cost = 2000.0
        self.type = "Hospitalized for the day"
        self.name = name
        self.hospital = hospital


class Hospital():
    def __init__(self):
        self.patients = []  # store the admitted patients
        self.cost = 0.0  # will get updated whenever a patient gets discharged

    def admit(self, patient_name, patient_type):
        if patient_type == "Emergency":
            new_patient = EmergencyPatient(patient_name, self)
            self.patients.append(new_patient)
            return new_patient
        elif patient_type == "Hospitalized":
            new_patient = HospitalizedPatient(patient_name, self)
            self.patients.append(new_patient)
            return new_patient
        else:
            print("We don't admit that type of patient in our hospital")

    def discharge_all(self):
        patients = self.patients
        for patient in patients:
            self.cost += patient.cost
        self.patients = []
        print("All patients discharged")

    def get_total_cost(self):
        # Count all the discharged patients to calculate the cost. In order to count every patient, start by discharging all the remaining patients
        self.discharge_all()
        return str(self.cost)


if __name__ == "__main__":
    print("HW3 scenario")
    hospital = Hospital()
    jake = hospital.admit("Jake", "Emergency")
    emma = hospital.admit("Emma", "Emergency")
    sam = hospital.admit("Sam", "Emergency")
    thomas = hospital.admit("Thomas", "Hospitalized")
    paul = hospital.admit("Paul", "Hospitalized")
    total_cost = hospital.get_total_cost()
    print(total_cost)
