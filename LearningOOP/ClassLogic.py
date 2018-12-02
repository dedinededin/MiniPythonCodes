class Students:

    num_of_students = 0

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
        Students.num_of_students +=1

    def __str__(self):
        return self.fname+" "+self.lname+" "+self.email

    def fullname(self):
        print(self.fname+" "+self.lname)

stu1 = Students("abraham","dogan","abraham@dogan.com")
stu2 = Students("ismet","deniz","enes@dogan.com")

stu1.fullname()
stu2.fullname()

print(stu1)
print(Students.num_of_students)

