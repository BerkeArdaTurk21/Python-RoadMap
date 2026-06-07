# =============================================================================
# Week 05 - Day 03 | Inheritance
# =============================================================================
# Topics: parent/child classes, super(), method overriding, isinstance(),
#         issubclass(), multi-level inheritance, multiple inheritance
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS INHERITANCE?
# -----------------------------------------------------------------------------
# Inheritance lets one class (child/subclass) REUSE and EXTEND the code of
# another class (parent/superclass).
#
# Real-world analogy:
#   Parent class  = Animal  (has name, age, eat())
#   Child class   = Dog     (inherits everything + adds bark(), fetch())
#
# Benefits:
#   • Avoid repeating code (DRY principle)
#   • Model real-world "is-a" relationships (a Dog IS-A Animal)
#   • Override specific behaviour without rewriting everything

# -----------------------------------------------------------------------------
# 2. BASIC INHERITANCE SYNTAX
# -----------------------------------------------------------------------------
# class ChildClass(ParentClass):
#     ...

class Animal:
    """Base class for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def __str__(self):
        return f"{self.name} (age {self.age})"


class Dog(Animal):
    """Dog inherits everything from Animal and adds its own behaviour."""

    def bark(self):
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


rex = Dog("Rex", 3)

# Methods inherited from Animal:
print(rex.eat())        # Rex is eating.
print(rex.sleep())      # Rex is sleeping.
print(rex)              # Rex (age 3)  ← uses Animal's __str__

# Methods defined in Dog:
print(rex.bark())       # Rex says: Woof!
print(rex.fetch("ball"))  # Rex fetches the ball!

# -----------------------------------------------------------------------------
# 3. THE super() FUNCTION
# -----------------------------------------------------------------------------
# super() gives you access to the PARENT class.
# Most commonly used in __init__ to call the parent's constructor first,
# so you don't have to re-type shared attributes.

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)   # call Animal.__init__ — sets name & age
        self.indoor = indoor          # Cat-specific attribute

    def speak(self):
        return f"{self.name} says: Meow!"

    def __str__(self):
        location = "indoor" if self.indoor else "outdoor"
        return f"{self.name} ({location} cat, age {self.age})"


whiskers = Cat("Whiskers", 4, indoor=True)
print(whiskers)           # Whiskers (indoor cat, age 4)
print(whiskers.eat())     # Whiskers is eating.  ← inherited
print(whiskers.speak())   # Whiskers says: Meow!

# Without super().__init__(), self.name and self.age would not be set!

# -----------------------------------------------------------------------------
# 4. METHOD OVERRIDING
# -----------------------------------------------------------------------------
# A child class can REDEFINE a method inherited from the parent.
# Python always calls the MOST SPECIFIC (child) version first.

class Animal2:
    def speak(self):
        return "..."    # generic — animals make some sound

class Dog2(Animal2):
    def speak(self):    # overrides Animal2.speak
        return "Woof!"

class Cat2(Animal2):
    def speak(self):    # overrides Animal2.speak
        return "Meow!"

class Fish(Animal2):
    pass               # does NOT override — uses Animal2.speak

animals = [Dog2(), Cat2(), Fish()]
for a in animals:
    print(a.speak())   # Woof!  /  Meow!  /  ...

# -----------------------------------------------------------------------------
# 5. CALLING THE PARENT METHOD WITH super()
# -----------------------------------------------------------------------------
# Sometimes you want to EXTEND the parent's method, not completely replace it.
# Use super().method_name() inside the override.

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)  # reuse parent __init__
        self.battery_kwh = battery_kwh       # extend with extra attribute

    def describe(self):
        base = super().describe()            # reuse parent describe()
        return f"{base} [Electric, {self.battery_kwh} kWh]"  # extend it


v  = Vehicle("Toyota", "Camry", 2020)
ev = ElectricCar("Tesla", "Model 3", 2023, 75)

print(v.describe())    # 2020 Toyota Camry
print(ev.describe())   # 2023 Tesla Model 3 [Electric, 75 kWh]

# -----------------------------------------------------------------------------
# 6. isinstance() AND issubclass()
# -----------------------------------------------------------------------------
# isinstance(obj, Class)       → True if obj is an instance of Class OR
#                                 any subclass of Class
# issubclass(Child, Parent)    → True if Child is a subclass of Parent

class Shape:
    pass

class Rectangle(Shape):
    pass

class Square(Rectangle):
    pass

r = Rectangle()
s = Square()

print(isinstance(r, Rectangle))   # True  — r is a Rectangle
print(isinstance(r, Shape))       # True  — Rectangle IS-A Shape
print(isinstance(r, Square))      # False — r is NOT a Square

print(isinstance(s, Square))      # True
print(isinstance(s, Rectangle))   # True  — Square IS-A Rectangle
print(isinstance(s, Shape))       # True  — Square IS-A Shape

print(issubclass(Square, Rectangle))  # True
print(issubclass(Rectangle, Shape))   # True
print(issubclass(Square, Shape))      # True  (transitive)
print(issubclass(Shape, Rectangle))   # False — wrong direction

# Every class is a subclass of object (Python's root class)
print(issubclass(Shape, object))   # True
print(isinstance(r, object))       # True

# -----------------------------------------------------------------------------
# 7. MULTI-LEVEL INHERITANCE
# -----------------------------------------------------------------------------
# A → B → C: C inherits from B which inherits from A.

class LivingThing:
    def breathe(self):
        return "Breathing..."

class Animal3(LivingThing):
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Dog3(Animal3):
    def bark(self):
        return f"{self.name} says: Woof!"


buddy = Dog3("Buddy")
print(buddy.breathe())   # Breathing...   ← from LivingThing
print(buddy.eat())       # Buddy is eating. ← from Animal3
print(buddy.bark())      # Buddy says: Woof! ← from Dog3

# Method Resolution Order (MRO) — the order Python searches for a method:
print(Dog3.__mro__)
# (<class 'Dog3'>, <class 'Animal3'>, <class 'LivingThing'>, <class 'object'>)

# -----------------------------------------------------------------------------
# 8. MULTIPLE INHERITANCE (BRIEF OVERVIEW)
# -----------------------------------------------------------------------------
# Python allows inheriting from MORE than one parent class.
# Use sparingly — it can make code harder to follow.

class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal3, Flyable, Swimmable):
    def speak(self):
        return f"{self.name} says: Quack!"


donald = Duck("Donald")
print(donald.eat())     # Donald is eating.   ← from Animal3
print(donald.fly())     # Donald is flying!   ← from Flyable
print(donald.swim())    # Donald is swimming! ← from Swimmable
print(donald.speak())   # Donald says: Quack! ← from Duck

# -----------------------------------------------------------------------------
# 9. PRACTICAL EXAMPLE — BANK ACCOUNT HIERARCHY
# -----------------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account[{self.owner}]: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    """Adds interest functionality to a basic bank account."""

    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        base = super().__str__()
        return f"{base} [Savings, {self.interest_rate*100:.1f}% interest]"


class CheckingAccount(BankAccount):
    """Adds overdraft limit to a basic bank account."""

    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):   # OVERRIDE — allows overdraft
        if amount > self.balance + self.overdraft_limit:
            print("Exceeds overdraft limit")
        else:
            self.balance -= amount


acc  = BankAccount("Alice", 500)
sav  = SavingsAccount("Bob", 1000, 0.05)
chk  = CheckingAccount("Carol", 50, overdraft_limit=200)

acc.deposit(200)
print(acc)              # Account[Alice]: $700.00

sav.apply_interest()
print(sav)              # Account[Bob]: $1050.00 [Savings, 5.0% interest]

chk.withdraw(200)       # allowed — 200 <= 50 + 200
print(chk)              # Account[Carol]: $-150.00
chk.withdraw(100)       # Exceeds overdraft limit

print(isinstance(sav, BankAccount))   # True  — SavingsAccount IS-A BankAccount
print(isinstance(chk, BankAccount))   # True

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────┬────────────────────────────────────────────────────┐
# │  Concept             │  Key Point                                         │
# ├──────────────────────┼────────────────────────────────────────────────────┤
# │  Inheritance         │  Child class reuses parent's code (IS-A relation)  │
# │  super()             │  Calls the parent class method / __init__          │
# │  Method override     │  Child redefines a method from the parent          │
# │  isinstance()        │  True for the class AND all parent classes         │
# │  issubclass()        │  Checks class-level IS-A relationship              │
# │  MRO                 │  Order Python searches for a method (C3 algorithm) │
# │  Multi-level         │  A → B → C chain of inheritance                    │
# │  Multiple            │  Child inherits from more than one parent          │
# └──────────────────────┴────────────────────────────────────────────────────┘
print("\nDay 03 — Inheritance complete!")
