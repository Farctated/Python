import random
class CFGStudent:
    def __init__(self, name,surname,age,email,):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
    @staticmethod
    def generate_id(self, student_id):
        self.student_id = student_id
    def get_id(self):
        print(self.student_id)
    def get_fullname(self):
        return self.name + self.surname
class NanoStudent(CFGStudent):
    def __init__(self, specialization):
        'your code goes here'
        self.specialization = specialization
        self.course_grades = 95
    @staticmethod
    def generate_id(self):
        self.student_id = f"NANO{random.randrange(1000, 10000)}"
        # 'your code goes here'
        # 'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        # 'return id as a string'
        # "Example 'NANO1234' "
    def add_new_grade(self, grade):
        self.course_grades = grade
        # 'your code goes here'
        # 'update course_grades container'
        # "Example: pass in a task name and its grade, so that both are added to course_grades"
    def get_course_grades(self):
        pass
        # 'your code goes here'
        # 'fetch course grades container and its values'

############################################

# Example run
s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}
