from student import Student
from json_manager import MakeJson
from numpy_analysis import NumpyOpr
from pandas_analysis import PandasOpr


class Main(MakeJson, NumpyOpr):
    def __init__(self):
        self.student_list = []
        
    def add_student(self, name, age, grades):
        student = Student(name, age, grades)
        self.student_list.append(student.to_dict())
    
    def display_students(self):
        for student in self.student_list:
            print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']} \n")
    
    def update_student(self, name, age=None, grades=None):
        for students in self.student_list:
            if students['name'] == name:
                if age is not None:
                    students['age'] = age
                if grades is not None:
                    students['grades'] = grades
                
    def delete_student(self, name):
        for i in self.student_list:
            if i['name'] == name:
                self.student_list.remove(i)
    
    def save_json(self):
        filename = input("Filename to save:")
        self.save_to_file(self.student_list, filename)

    def load_json(self):
        filename = input("Filename to load:")
        self.student_list = self.load_to_file(filename)

    def numpy_calc(self):
        return self.num_mark(self.student_list)

    def pandas_calc(self):
        res = PandasOpr(self.student_list)
        return res.sort_by_avg()


        


def main():
    app = Main()

    while True:
        print("\n===== STUDENT SYSTEM =====")
        print("1. Add student")
        print("2. Show all students")
        print("3. Delete student")
        print("4. Update student")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. NumPy analysis")
        print("8. Pandas analysis")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Name: ").strip().capitalize()
            age = int(input("Age: "))

            grades = list(map(int, input("Grades (comma separated): ").split(",")))

            app.add_student(name, age, grades)

        elif choice == "2":
            app.display_students()

        elif choice == "3":
            name = input("Name to delete: ")
            app.delete_student(name)

        elif choice == "4":
            name = input("Name to update: ")

            age_input = input("New age (or Enter to skip): ")
            age = int(age_input) if age_input else None

            grades_input = input("New grades (comma separated or Enter to skip): ")
            grades = list(map(int, grades_input.split(",")))

            app.update_student(name, age, grades)

        elif choice == "5":
            app.save_json()
            print("Saved.")

        elif choice == "6":
            app.load_json()
            print("Loaded.")

        elif choice == "7":
            result = app.numpy_calc()
            for i in result:
                print(i)

        elif choice == "8":
            print(app.pandas_calc())

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid option.")

main()