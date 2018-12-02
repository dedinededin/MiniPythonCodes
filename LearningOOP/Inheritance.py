class UniversityPeople:

    def __init__(self, fname, lname, email, id):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.id = id

    def fullname(self):
        print(self.fname + ' ' + self.lname)

    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.email + ' ' + self.id


class Students(UniversityPeople):
    pass


class Teachers(UniversityPeople):
    def __init__(self, fname, lname, email, id, salary):
        super().__init__(fname, lname, email, id)
        self.salary = salary


# nested inheritance Maths inherits both Teachers and UniversityPeople classes.
class Maths(Teachers):
    pass


stu1 = Students('Abraham', 'Dogan', 'abraham@dogan.com', '1')
stu2 = Students('Ismet', 'Deniz', 'ismet@deniz.com', '2')
maths = Teachers('Emma', 'Watson', 'emma@watson.com', '3', '97000')

stu1.fullname()
maths.fullname()
print(maths.salary)
print(maths)

print(isinstance(stu1, Students))
print(isinstance(stu1, Teachers))
print(isinstance(stu1, UniversityPeople))
print(issubclass(Students, UniversityPeople))
