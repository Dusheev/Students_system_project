import numpy as np

class NumpyOpr():
    def num_mark(self, student_list):
        result_list = []
        for i in student_list:
            i['average_numpy'] = np.mean(np.array(i['grades']))
            i['max_value'] = max(i['grades'])
            result_list.append(f"{i['name']} average mark {i['average_numpy']}, max mark {i['max_value']}")
        return result_list

        
    
