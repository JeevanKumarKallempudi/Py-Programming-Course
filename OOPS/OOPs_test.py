"""
1. create a class SchoolMember , it should have following instance attributes :
- name
- age
SchoolMember should have a introduce() function, that should return "My name is xyz. I am abc years old."
2. create a subclass of SchoolMember called Student, there should be following instance attributes :
- name
- age
- my_class
- roll_no
Note : (Make sure you reuse the parent class attributes)
Student class should override introduce() function from SchoolMember class, and Student introduce() should return "I am in xyz class. My roll number is pqr."
3. create another subclass of SchoolMember with name of Teacher, there should be following instance attributes :
- name
- age
- subject
- salary
Note : (Make sure you reuse the parent class attributes)
Teacher class should override introduce() function from SchoolMember class, and Teacher introduce() should return "I Teach xyz subject. My salary is pqr."
"""

# Write only the classes and their member functions.
# No need to initialize and call functions.
class SchoolMember:
    ### Write Code for SchoolMember class ###
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is {}. I am {} years old.".format(self.name, self.age)
    ### Code ends here ###


class Student(SchoolMember):
    ### Write Code for Student class ###
    def __init__(self, name, age, my_class, roll_no):
        super().__init__(name, age)
        self.my_class = my_class
        self.roll_no = roll_no

    def introduce(self):
        return "I am in {} class. My roll number is {}.".format(self.my_class, self.roll_no)
    ### Code ends here ###


class Teacher(SchoolMember):
    ### Write Code for Teacher class ###
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def introduce(self):
        return "I Teach {} subject. My salary is {}.".format(self.subject, self.salary)
    ### Code ends here ###