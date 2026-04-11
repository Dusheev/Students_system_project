import pandas as pd

class PandasOpr:
    def __init__(self, student_list):
        self.student_list = student_list
        self.df = pd.DataFrame(student_list)

    def sort_by_avg(self):
        self.df["avg_grade"] = self.df["grades"].apply(
            lambda g: sum(g) / len(g) if g else 0
        )
        return self.df.sort_values("avg_grade", ascending=False)