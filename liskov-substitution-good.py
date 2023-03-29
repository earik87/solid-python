from abc import ABC, abstractmethod

class RegisterCourse(ABC):
    @abstractmethod
    def register(self, student_name):
        pass

class RegisterCourseWithGithubAccount(ABC):
    @abstractmethod
    def register(self, github_account):
        pass

class RegisterMath(RegisterCourse):
    def register(self, student_name):
        print(f"Student with name: {student_name} is registered to math course.")

class RegisterChemistry(RegisterCourse):
    def register(self, student_name):
        print(f"Student with name: {student_name} is registered to chemistry course.")

class RegisterComputerScience(RegisterCourseWithGithubAccount):
    def register(self, github_account):
        print(f"Student with github account: {github_account} is registered to computer science course.")


math_registerer = RegisterMath()
math_registerer.register("Enis")
computerscience_registerer = RegisterComputerScience()
computerscience_registerer.register("enis@github.com")
