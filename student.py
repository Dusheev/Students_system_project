class Student(object):
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades      

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'grades': self.grades
        }