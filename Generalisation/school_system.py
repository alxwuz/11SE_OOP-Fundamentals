class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display_details(self):
        print(f"Name: {self.name}, Date of Birth: {self.dob}")

class Teacher(Person):
    def __init__(self, name, dob, employee_id, job):
        super().__init__(name, dob)
        self.employee_id = employee_id
        self.job = job

    def display_details(self):
        super().display_details()
        print(f"""Name: {self.name}
            DOB: {self.dob}
            Employee ID: {self.employee_id}
            Currently Teaching:{self.job}""")
        
class Student(Person):
    def __init__(self, name, dob, student_id, top_subject):
        super().__init__(name, dob)
        self.student_id = student_id
        self.top_subject= top_subject

    def display_details(self):
        super().display_details()
        print(f"""Name: {self.name}
            DOB: {self.dob}
            Student ID: {self.student_id}
            Top Subject: {self.top_subject}""")