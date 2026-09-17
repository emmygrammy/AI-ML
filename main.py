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



class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)



class Dog(Animal):
    def make_sound(self):
        print('Woof! Woof!')
               


class Cat(Animal):
    def make_sound(self):
        print('Meow! Meow!')
                

x=Dog('Buddy', 'Woof!')
x.make_sound()

x=Cat('Kitty', 'Meow!')
x.make_sound()

#Create a base class Shape with a method area() that raises NotImplementedError.
#Create subclasses Rectangle and Circle that implement area() appropriately.
#Instantiate both and print their areas.
#Create subclasses Rectangle and Circle that implement area() appropriately.
#Instantiate both and print their areas.

class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

x=rectangle(5, 10)
print(x.area())

x=circle(5)
print(x.area())
       

#Create a base class BankAccount with owner, balance, and methods deposit() and withdraw().
#Create a subclass SavingsAccount that adds an interest_rate and a method add_interest() which increases the balance.
#Demonstrate deposits, withdrawals, and interest application.

class bankAccout:
    def __init__(self, owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.owner}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}")
           
        else:
            print("Insufficient funds")


class savingsaccout(bankAccout):
    def __init__(self, owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100
        print(f"Added interest of {self.balance * self.interest_rate / 100} to {self.owner}")
       


x=savingsaccout('John', 1000, 5)
x.add_interest()
x.deposit(500)
x.withdraw(5000)


##Create a base class Vehicle with attributes brand and model, and a method display_info().
##Create a subclass Car that adds doors and overrides display_info().
##Create another subclass ElectricCar (child of Car) that adds battery_capacity and overrides display_info() to include all details.
##Create an ElectricCar object and call display_info().


myTuple = ("mango", "apple", "orange")
myIterator = iter(myTuple)
 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))


myStuff = 'Emmanuel'
myIterator = iter(myStuff)
 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

List = [1, 2, 3, 4, 5]
myIterator = iter(List)
 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
myIterator = iter(dict)
 
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))