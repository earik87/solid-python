class Student:
    def __init__(self, name, surname, identification_n):
        self.name = name
        self.surname = surname
        self.identification_n = identification_n

    def get_student_info(self):
        print(f"Student {self.name} {self.surname} has ID: {self.identification_n}.")

class RegisterCourse:
    def register(self, student):
        pass

class RegisterMath(RegisterCourse):
    def register(self, student):
        print(f"Student with ID {student.identification_n} is registered to math course.")

class RegisterChemistry(RegisterCourse):
    def register(self, student):
        print(f"Student with ID {student.identification_n} is registered to chemistry course.")

class RegisterPsychology(RegisterCourse):
    def register(self, student):
        print(f"Student with ID {student.identification_n} is registered to psychology course.")

Enis = Student("Enis", "Arik", 115)
Emre = Student("Emre", "Arik", 120)
Seda = Student("Seda", "Williams", 130)
Enis.get_student_info()
Emre.get_student_info()
Seda.get_student_info()
math_registerer = RegisterMath()
math_registerer.register(Enis)
chemistry_registerer = RegisterChemistry()
chemistry_registerer.register(Emre)
psychology_registerer = RegisterPsychology()
psychology_registerer.register(Seda)
