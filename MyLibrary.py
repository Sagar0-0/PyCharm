class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class CgcLibrary:
    data = {'a': None, 'b': None, 'c': None, 'd': None}

    @classmethod
    def issue_Book(cls, student, bookName):
        if cls.data[bookName] is None:
            cls.data[bookName] = student.name
            print(f"Issued book '{bookName}' to Student with name '{student.name}' and roll no. '{student.roll}'")
        else:
            str = cls.data[bookName]
            print(f"'{bookName}' book is already issued by '{str}'")

    @classmethod
    def give_back(cls, student, bookname):
        print(f"'{student.name}' returned the book '{bookname}'")
        cls.data[bookname] = None

    @classmethod
    def get_data(cls):
        print(cls.data)


pwn = Student("Pawan", 223)
arvnd = Student("Arvind", 225)
CgcLibrary.issue_Book(pwn, 'a')
CgcLibrary.issue_Book(pwn, 'b')
CgcLibrary.issue_Book(pwn, 'c')
CgcLibrary.issue_Book(pwn, 'd')
CgcLibrary.get_data()
CgcLibrary.give_back(pwn, 'a')
CgcLibrary.give_back(pwn, 'b')
CgcLibrary.get_data()
CgcLibrary.issue_Book(arvnd, 'a')
CgcLibrary.get_data()
CgcLibrary.issue_Book(arvnd, 'c')
