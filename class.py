from datetime import datetime

class MyName:
    def __init__(self, name=None, second_name=None, birth_yr=None):
        self.name = name
        self.second_name = second_name
        self.birth_yr = birth_yr

    def calculate_course(self):
        if self.birth_yr is None:
            return None
        this_year = datetime.now().year
        age = this_year - self.birth_yr
        course = age - 15 #типу поступають в 15 років
        return max(course, 1) #курс не може бути 0

    def name_list(self):
        return [self.name, self.second_name]


obj = MyName("Ілля", "Пітбульович", 2008)
print(obj.calculate_course())
print(obj.name_list())
obj2 = MyName()
print(obj2.calculate_course())
print(obj2.name_list())