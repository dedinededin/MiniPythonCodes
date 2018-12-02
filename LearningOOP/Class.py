class Students:
    num_of_students = 0

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
        Students.num_of_students += 1

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email

    def fullname(self):
        print(self.fname + ' ' + self.lname)

    @classmethod
    def from_string(cls, data_string):
        firstname, lastname, email = data_string.split('-')
        return cls(firstname, lastname, email)


stu1 = Students('abraham', 'dogan', 'abraham@dogan.com')
stu2 = Students('ismet', 'deniz', 'enes@dogan.com')

stu1.fullname()
stu2.fullname()

print(stu1)
print(Students.num_of_students)

stu1_string = 'abraham-dogan-abraham@dogan.com'

stu1 = Students.from_string(stu1_string)

stu1.fullname()
print(stu1)
print(Students.num_of_students)
