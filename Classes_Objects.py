class Student:
    dress = "blue"

    def __int__(self):
        pass

    def __init__(self, name, roll, section):
        self.name = name
        self.roll = roll
        self.section = section

    def changesxn(self, section):
        self.section = section

    @classmethod
    def str_data(cls, str):
        lis = str.split('-')
        return cls(lis[0], int(lis[1]), lis[2])
        # return cls(*str.split("-"))

    def get_data(self):
        return f"Name is: {self.name}.\nRoll no. is: {self.roll}.\nSection is: {self.section}"

    @staticmethod
    def result():
        return "Passes"


sagar = Student.str_data("Sagar-30-b")
# sagar.name = "sagar"
# sagar.roll = 30
# sagar.section = 'a'
sagar.knowledge = 'coding'
print(sagar.__dict__)
pwn = Student("pawan", 40, 'b')
pwn.standard = 2
print(pwn.__dict__)
# pwn.changesxn('c')
# print(pwn.get_data())
# print(Student.result())
