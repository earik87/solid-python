class Student:
    def __init__(self, name, surname, identification_n):
        self.name = name
        self.surname = surname
        self.identification_n = identification_n

    def get_student_info(self):
        print(f"Student {self.name} {self.surname} has ID: {self.identification_n}.")

class CourseRegisterer:
    def register_math(self, student):
        print(f"Student with ID {student.identification_n} is registered to math course.")
    def register_chemistry(self, student):
        print(f"Student with ID {student.identification_n} is registered to chemistry course.")

Enis = Student("Enis", "Arik", 115)
Emre = Student("Emre", "Arik", 120)
Enis.get_student_info()
Emre.get_student_info()
courseRegistry = CourseRegisterer()
courseRegistry.register_math(Enis)
courseRegistry.register_chemistry(Emre)
