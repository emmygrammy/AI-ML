class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

p1 = person('John', 'Doe')
p1.printname()


class student(person):
    pass


x = student('Mike', 'Olsen')
x.printname()


class student(person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname,lname)
        self.graduationyear = graduationyear

    def welcome(self):
        print("Welcome", self.fname, self.lname , "to the class of", self.graduationyear)

x=student('Mike', 'Olsen', 2019)
x.welcome()