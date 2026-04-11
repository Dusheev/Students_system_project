import json

class MakeJson():
    def save_to_file(self, student_list, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(student_list, f, ensure_ascii=False, indent=4)

    def load_to_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
        