# =============================================================================
# Week 05 - Day 03 | Inheritance — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Animal Hierarchy
# -----------------------------------------------------------------------------
# KEY INSIGHT: super().__init__(name, age) in both Dog and Cat means we only
# define the shared attributes once — in Animal. Adding a new shared attribute
# later only requires changing one place.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def eat(self):
        return f"{self.name} is eating."

    def __str__(self):
        return f"{self.name} (age {self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def __str__(self):
        return f"{self.name} the {self.breed} (age {self.age})"


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} says: Meow!"

    def __str__(self):
        location = "indoor" if self.indoor else "outdoor"
        return f"{self.name} ({location} cat, age {self.age})"


rex      = Dog("Rex", 3, "Labrador")
whiskers = Cat("Whiskers", 4, indoor=True)

print(rex)
print(rex.eat())
print(rex.speak())
print(rex.fetch("ball"))
print(whiskers)
print(whiskers.speak())
print(isinstance(rex, Animal))
print(isinstance(whiskers, Animal))
print()

# WHY call super().__init__ instead of Animal.__init__(self, ...)?
# Using super() is the correct OOP idiom — it respects the MRO and works
# correctly even with multiple inheritance or further subclassing.

# -----------------------------------------------------------------------------
# Solution 2 — Shape Area Calculator
# -----------------------------------------------------------------------------
# KEY INSIGHT: describe() in Shape calls self.area(), which Python resolves
# to the CHILD's area() at runtime (polymorphism). The parent doesn't need
# to know about its children to produce the correct description.

class Shape:
    def __init__(self, color="red"):
        self.color = color

    def area(self):
        return 0

    def describe(self):
        return f"A {self.color} shape with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height, color="red"):
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Triangle(Shape):
    def __init__(self, base, height, color="blue"):
        super().__init__(color)
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


r = Rectangle(4, 6)
t = Triangle(3, 8)

print(r)
print(r.area())
print(r.describe())
print(t)
print(t.area())
print(t.describe())
print()

# WHY does describe() in Shape work correctly for subclasses?
# self.area() uses dynamic dispatch — Python calls the method on the
# ACTUAL object (Rectangle or Triangle), not the Shape placeholder.
# This is polymorphism in action; we'll cover it fully in Day 05.

# -----------------------------------------------------------------------------
# Solution 3 — Employee Hierarchy
# -----------------------------------------------------------------------------
# KEY INSIGHT: Manager.work() fully overrides Employee.work() (different
# message, no super()). But Manager.get_info() EXTENDS Employee.get_info()
# using super() — avoiding duplication while adding extra info.

class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def work(self):
        return f"{self.name} is working."

    def get_info(self):
        return f"Employee: {self.name}, Salary: ${self.salary:,.2f}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is managing a team of {self.team_size}."

    def give_raise(self, employee, amount):
        employee.salary += amount
        return f"{employee.name} got a raise!"

    def get_info(self):
        return super().get_info() + f" | Team size: {self.team_size}"


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        return f"{self.name} is coding in {self.language}."

    def get_info(self):
        return super().get_info() + f" | Language: {self.language}"


mgr = Manager("Alice", 90000, team_size=5)
dev = Developer("Bob", 80000, language="Python")

print(mgr.get_info())
print(mgr.work())
print(dev.get_info())
print(dev.work())
print(mgr.give_raise(dev, 5000))
print(dev.get_info())
print()

# WHY use super().get_info() instead of repeating the string?
# If Employee.get_info() changes format later, Manager and Developer
# automatically benefit — one source of truth.

# -----------------------------------------------------------------------------
# Solution 4 — Vehicle Hierarchy
# -----------------------------------------------------------------------------
# KEY INSIGHT: Car.start() uses super() to extend the parent message.
# ElectricCar.start() does a full override with a completely different
# message — no super() needed. This shows both patterns side-by-side.

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def start(self):
        return f"Starting {self.year} {self.make} {self.model}."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start(self):
        return super().start() + f" (Car, {self.num_doors} doors)"

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.num_doors}-door)"


class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_kwh):
        super().__init__(make, model, year, num_doors)
        self.battery_kwh = battery_kwh

    def start(self):
        return f"{self.year} {self.make} {self.model} silently powered on."

    def charge(self):
        return f"Charging {self.battery_kwh} kWh battery..."

    def __str__(self):
        return f"{self.year} {self.make} {self.model} [EV, {self.battery_kwh} kWh]"


car = Car("Toyota", "Camry", 2020, 4)
ev  = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

print(car)
print(car.start())
print(ev)
print(ev.start())
print(ev.charge())
print(isinstance(ev, Car))
print(isinstance(ev, Vehicle))
print()

# WHY does super().__init__ chain correctly through 3 levels?
# ElectricCar → Car → Vehicle. Each level adds its own attribute and
# passes the shared ones up. The chain means Vehicle.__init__ still
# sets make/model/year even though ElectricCar called Car's __init__.

# -----------------------------------------------------------------------------
# Solution 5 — Account Hierarchy
# -----------------------------------------------------------------------------
# KEY INSIGHT: SavingsAccount.withdraw() overrides the parent to enforce a
# minimum balance — a domain rule that only applies to savings accounts.
# PremiumAccount.deposit() overrides to add cashback before delegating
# to the parent. Both patterns (guard + extend) are useful overrides.

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
    def __init__(self, owner, balance=0, rate=0.04):
        super().__init__(owner, balance)
        self.rate = rate

    def apply_interest(self):
        self.balance += self.balance * self.rate

    def withdraw(self, amount):
        if self.balance - amount < 100:
            print("Minimum balance required")
        else:
            self.balance -= amount

    def __str__(self):
        return super().__str__() + f" [Savings {self.rate*100:.1f}%]"


class PremiumAccount(BankAccount):
    def __init__(self, owner, balance=0, cashback_rate=0.02):
        super().__init__(owner, balance)
        self.cashback_rate = cashback_rate

    def deposit(self, amount):
        total = amount + amount * self.cashback_rate
        super().deposit(total)   # reuse parent deposit logic

    def __str__(self):
        return super().__str__() + f" [Premium {self.cashback_rate*100:.1f}% cashback]"


sav  = SavingsAccount("Alice", 1000)
prem = PremiumAccount("Bob")

print(sav)
sav.apply_interest()
print(sav)
sav.withdraw(1000)
sav.withdraw(100)
print(sav)

print(prem)
prem.deposit(500)
print(prem)

# WHY call super().deposit(total) in PremiumAccount.deposit()?
# It reuses BankAccount's balance update logic. If BankAccount.deposit()
# ever adds validation or logging, PremiumAccount benefits automatically.
