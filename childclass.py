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


class ExtendedMyName(MyName):
    def __init__(self, name=None, second_name=None, birth_yr=None, city=None, country=None, hobby=None):
        super().__init__(name, second_name, birth_yr)
        self.city = city
        self.country = country
        self.hobby = hobby

    def get_full_info(self):
        return {
            "Name": self.name,
            "Second Name": self.second_name,
            "Birth Year": self.birth_yr,
            "City": self.city,
            "Country": self.country,
            "Hobby": self.hobby
        }

    def _is_adult(self):
        if self.birth_yr is None:
            return None
        return (datetime.now().year - self.birth_yr) >= 16

obj = ExtendedMyName("Ілля", "Пітбульович", 2008,  "Техас", "ЮСА", "гачімучі")
print("студент на курсі", obj.calculate_course())
print("ПІ", obj.name_list())
print(obj.get_full_info())
print(obj._is_adult())