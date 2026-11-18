class Student:
    school = 'UIT'

    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    @staticmethod
    def greet():
        print(f"Xin chao tui la {Student.school}")
    @classmethod
    def show(cls):
        print(f"Xin chao tui la mot {cls.__name__}")
Student.show()

class MIT(Student):
    pass
MIT.show()