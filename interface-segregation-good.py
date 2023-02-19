from abc import ABC, abstractmethod

class RegisterBeginnerCourses(ABC):
    def RegisterIntroductionToComputerScience(self):
        pass

class RegisterAdvanceCourses(ABC):
    def RegisterAdvancedAlgorithms(self):
        pass

class FirstYearStudent(RegisterBeginnerCourses):
    def RegisterIntroductionToComputerScience(self):
        print("Register to Introduction to Computer Science Course")

class SecondYearStudent(RegisterBeginnerCourses, RegisterAdvanceCourses):
    def RegisterIntroductionToComputerScience(self):
        print("Register to Introduction to Computer Science Course")

    def RegisterAdvancedAlgorithms(self):
        print("Register to Advanced Algorithms Course")
