class Student:
    def __init__(self, name, surname, identification_n):
        self.name = name
        self.surname = surname
        self.identification_n = identification_n

    def get_student_info(self):
        print(f"Student {self.name} {self.surname} has ID: {self.identification_n}.")

class Registerer:
    def register(self, identification_n):
        print(f"Student with ID {identification_n} is registered.")
        self.registered = True

Enis = Student("Enis", "Arik", 115)
Enis.get_student_info()
registerer = Registerer()
registerer.register(115)
