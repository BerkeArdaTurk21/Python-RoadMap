# =============================================================================
# Week 05 - Day 05 | Polymorphism — Solutions
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Payment Processor
# -----------------------------------------------------------------------------
# KEY INSIGHT: process_all() calls .process() on every object without
# caring about the type. Adding a new payment method (e.g. BankTransfer)
# requires zero changes to process_all — just add the new class.

class PaymentMethod:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing ${self.amount:.2f}..."

    def __str__(self):
        return f"PaymentMethod: ${self.amount:.2f}"


class CreditCard(PaymentMethod):
    def __init__(self, amount, last4):
        super().__init__(amount)
        self.last4 = last4

    def process(self):
        return f"Charging ${self.amount:.2f} to card ending in {self.last4}"

    def __str__(self):
        return f"CreditCard(****{self.last4}): ${self.amount:.2f}"


class PayPal(PaymentMethod):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return f"Sending ${self.amount:.2f} via PayPal to {self.email}"

    def __str__(self):
        return f"PayPal({self.email}): ${self.amount:.2f}"


class CryptoWallet(PaymentMethod):
    def __init__(self, amount, coin):
        super().__init__(amount)
        self.coin = coin

    def process(self):
        return f"Transferring ${self.amount:.2f} in {self.coin}"

    def __str__(self):
        return f"CryptoWallet({self.coin}): ${self.amount:.2f}"


def process_all(payments):
    for p in payments:
        print(p.process())


payments = [
    CreditCard(50, "1234"),
    PayPal(25, "user@example.com"),
    CryptoWallet(100, "BTC"),
]
process_all(payments)
print()

# -----------------------------------------------------------------------------
# Solution 2 — Serializer (Duck Typing)
# -----------------------------------------------------------------------------
# KEY INSIGHT: None of the serializers inherit from a common base — they just
# all happen to have a serialize() method. This is pure duck typing.
# save() doesn't care about the type — only the interface.

class JSONSerializer:
    def serialize(self, data):
        pairs = ', '.join(f'"{k}": "{v}"' for k, v in data.items())
        print(f'JSON: {{{pairs}}}')


class CSVSerializer:
    def serialize(self, data):
        keys   = ','.join(data.keys())
        values = ','.join(data.values())
        print(f"CSV: {keys}\n{values}")


class XMLSerializer:
    def serialize(self, data):
        inner = ''.join(f"<{k}>{v}</{k}>" for k, v in data.items())
        print(f"XML: <root>{inner}</root>")


def save(serializer, data):
    serializer.serialize(data)


data = {"name": "Alice", "age": "30"}
save(JSONSerializer(), data)
save(CSVSerializer(),  data)
save(XMLSerializer(),  data)
print()

# WHY no base class? Duck typing means Python doesn't enforce inheritance.
# The contract is informal: "must have serialize(data)."
# In larger codebases you'd use an ABC (Abstract Base Class) for documentation.

# -----------------------------------------------------------------------------
# Solution 3 — Notification System
# -----------------------------------------------------------------------------

class Notifier:
    def send(self, message):
        print(f"Sending: {message}")


class EmailNotifier(Notifier):
    def __init__(self, address):
        self.address = address

    def send(self, message):
        print(f"Email to {self.address}: {message}")


class SMSNotifier(Notifier):
    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"SMS to {self.phone}: {message}")


class PushNotifier(Notifier):
    def __init__(self, device):
        self.device = device

    def send(self, message):
        print(f"Push to {self.device}: {message}")


def broadcast(notifiers, message):
    for n in notifiers:
        n.send(message)


notifiers = [
    EmailNotifier("alice@example.com"),
    SMSNotifier("+1234567890"),
    PushNotifier("iPhone-12"),
]
broadcast(notifiers, "Server is down!")
print()

# -----------------------------------------------------------------------------
# Solution 4 — Discount Calculator
# -----------------------------------------------------------------------------

class Discount:
    def apply(self, price):
        return price

    def __str__(self):
        return "No discount"


class PercentDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return round(price * (1 - self.percent / 100), 2)

    def __str__(self):
        return f"{self.percent}% off"


class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return round(max(0, price - self.amount), 2)

    def __str__(self):
        return f"${self.amount:.2f} off"


class BuyOneGetOne(Discount):
    def apply(self, price):
        return round(price / 2, 2)

    def __str__(self):
        return "Buy 1 Get 1 Free"


def checkout(price, discount):
    final = discount.apply(price)
    print(f"{discount} → ${final:.2f}")


checkout(100, Discount())
checkout(100, PercentDiscount(10))
checkout(100, FixedDiscount(15))
checkout(100, BuyOneGetOne())
print()

# -----------------------------------------------------------------------------
# Solution 5 — Polymorphic Area + Perimeter
# -----------------------------------------------------------------------------
# KEY INSIGHT: summary() is defined once in Shape and works for ALL subclasses
# because self.area() and self.perimeter() use dynamic dispatch — Python calls
# the overriding versions in Rectangle, Circle, Triangle.

import math

class Shape:
    def area(self):
        return 0.0

    def perimeter(self):
        return 0.0

    def summary(self):
        name = type(self).__name__
        return f"{name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Circle(Shape):
    PI = 3.14159

    def __init__(self, r):
        self.r = r

    def area(self):
        return round(Circle.PI * self.r ** 2, 2)

    def perimeter(self):
        return round(2 * Circle.PI * self.r, 2)


class Triangle(Shape):
    def __init__(self, a, b, c, h):
        self.a, self.b, self.c, self.h = a, b, c, h

    def area(self):
        return round(0.5 * self.a * self.h, 2)

    def perimeter(self):
        return self.a + self.b + self.c


def compare_shapes(s1, s2):
    n1 = type(s1).__name__
    n2 = type(s2).__name__
    if s1.area() > s2.area():
        print(f"{n1} is larger")
    elif s2.area() > s1.area():
        print(f"{n2} is larger")
    else:
        print("Equal area")


r = Rectangle(4, 6)
c = Circle(5)
t = Triangle(3, 4, 5, 8)

print(r.summary())
print(c.summary())
print(t.summary())
compare_shapes(r, c)

# WHY type(self).__name__ instead of hardcoding?
# It dynamically gets the actual class name — works for any subclass
# without needing to override summary(). This is polymorphism via introspection.
