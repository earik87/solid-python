from abc import ABC, abstractmethod

class RegisterCourses(ABC):
    def RegisterIntroductionToComputerScience(self):
        pass

    def RegisterAdvancedAlgorithms(self):
        pass

class FirstYearStudent(RegisterCourses):
    def RegisterIntroductionToComputerScience(self):
        print("Register to Introduction to Computer Science Course")

    def RegisterAdvancedAlgorithms(self):
        raise Exception("Registery to Advanced Algorithms Course is not possible.")

class SecondYearStudent(RegisterCourses):
    def RegisterIntroductionToComputerScience(self):
        print("Register to Introduction to Computer Science Course")

    def RegisterAdvancedAlgorithms(self):
        print("Register to Advanced Algorithms Course")
