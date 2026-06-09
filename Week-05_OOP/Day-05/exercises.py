# =============================================================================
# Week 05 - Day 05 | Polymorphism — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Payment Processor
# -----------------------------------------------------------------------------
# Create a payment hierarchy using polymorphism:
#
# PaymentMethod (base):
#   - __init__(self, amount)
#   - process(self) → "Processing $X.XX..."  (generic)
#   - __str__       → "PaymentMethod: $X.XX"
#
# CreditCard(PaymentMethod):
#   - __init__(self, amount, last4)
#   - process(self) → "Charging $X.XX to card ending in XXXX"
#   - __str__       → "CreditCard(****XXXX): $X.XX"
#
# PayPal(PaymentMethod):
#   - __init__(self, amount, email)
#   - process(self) → "Sending $X.XX via PayPal to email@x.com"
#   - __str__       → "PayPal(email@x.com): $X.XX"
#
# CryptoWallet(PaymentMethod):
#   - __init__(self, amount, coin)
#   - process(self) → "Transferring $X.XX in BTC"
#   - __str__       → "CryptoWallet(BTC): $X.XX"
#
# Write process_all(payments) that calls process() on each.
#
# Expected output:
#   Charging $50.00 to card ending in 1234
#   Sending $25.00 via PayPal to user@example.com
#   Transferring $100.00 in BTC

class PaymentMethod:
    pass  # TODO

class CreditCard(PaymentMethod):
    pass  # TODO

class PayPal(PaymentMethod):
    pass  # TODO

class CryptoWallet(PaymentMethod):
    pass  # TODO

def process_all(payments):
    pass  # TODO


payments = [
    CreditCard(50, "1234"),
    PayPal(25, "user@example.com"),
    CryptoWallet(100, "BTC"),
]
process_all(payments)
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Serializer (Duck Typing)
# -----------------------------------------------------------------------------
# Create three serializer classes that do NOT share a base class:
#
# JSONSerializer:
#   - serialize(self, data: dict) → "JSON: {"key": "value", ...}"
#     (format each pair as "key": "value" separated by ", ")
#
# CSVSerializer:
#   - serialize(self, data: dict) → "CSV: key1,key2,...\nval1,val2,..."
#
# XMLSerializer:
#   - serialize(self, data: dict) → "XML: <root><key>value</key>...</root>"
#
# Write save(serializer, data) that calls serializer.serialize(data).
# None of the serializers inherit from a common class — demonstrate duck typing.
#
# Expected output (for data = {"name": "Alice", "age": "30"}):
#   JSON: {"name": "Alice", "age": "30"}
#   CSV: name,age
#   Alice,30
#   XML: <root><name>Alice</name><age>30</age></root>

class JSONSerializer:
    pass  # TODO

class CSVSerializer:
    pass  # TODO

class XMLSerializer:
    pass  # TODO

def save(serializer, data):
    pass  # TODO


data = {"name": "Alice", "age": "30"}
save(JSONSerializer(), data)
save(CSVSerializer(),  data)
save(XMLSerializer(),  data)
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Notification System
# -----------------------------------------------------------------------------
# Build a polymorphic notification system:
#
# Notifier (base):
#   - send(self, message) → "Sending: {message}"
#
# EmailNotifier(Notifier):
#   - __init__(self, address)
#   - send(self, message) → "Email to {address}: {message}"
#
# SMSNotifier(Notifier):
#   - __init__(self, phone)
#   - send(self, message) → "SMS to {phone}: {message}"
#
# PushNotifier(Notifier):
#   - __init__(self, device)
#   - send(self, message) → "Push to {device}: {message}"
#
# broadcast(notifiers, message) → calls send() on each notifier
#
# Expected output:
#   Email to alice@example.com: Server is down!
#   SMS to +1234567890: Server is down!
#   Push to iPhone-12: Server is down!

class Notifier:
    pass  # TODO

class EmailNotifier(Notifier):
    pass  # TODO

class SMSNotifier(Notifier):
    pass  # TODO

class PushNotifier(Notifier):
    pass  # TODO

def broadcast(notifiers, message):
    pass  # TODO


notifiers = [
    EmailNotifier("alice@example.com"),
    SMSNotifier("+1234567890"),
    PushNotifier("iPhone-12"),
]
broadcast(notifiers, "Server is down!")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Discount Calculator
# -----------------------------------------------------------------------------
# Polymorphic discount strategies:
#
# Discount (base):
#   - apply(self, price) → price (no discount)
#   - __str__            → "No discount"
#
# PercentDiscount(Discount):
#   - __init__(self, percent)
#   - apply(self, price) → price * (1 - percent/100), rounded to 2 dp
#   - __str__            → "10% off"
#
# FixedDiscount(Discount):
#   - __init__(self, amount)
#   - apply(self, price) → max(0, price - amount), rounded to 2 dp
#   - __str__            → "$5.00 off"
#
# BuyOneGetOne(Discount):
#   - apply(self, price) → price / 2  (you pay half)
#   - __str__            → "Buy 1 Get 1 Free"
#
# checkout(price, discount) → prints the discount and final price
#
# Expected output:
#   No discount → $100.00
#   10% off → $90.00
#   $15.00 off → $85.00
#   Buy 1 Get 1 Free → $50.00

class Discount:
    pass  # TODO

class PercentDiscount(Discount):
    pass  # TODO

class FixedDiscount(Discount):
    pass  # TODO

class BuyOneGetOne(Discount):
    pass  # TODO

def checkout(price, discount):
    pass  # TODO


checkout(100, Discount())
checkout(100, PercentDiscount(10))
checkout(100, FixedDiscount(15))
checkout(100, BuyOneGetOne())
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Polymorphic Area + Perimeter
# -----------------------------------------------------------------------------
# Create Shape, Rectangle, Circle, Triangle with polymorphic methods.
# Also add a compare_shapes(s1, s2) function that prints which has a larger area.
#
# Shape (base):
#   - area(self)      → 0.0
#   - perimeter(self) → 0.0
#   - summary(self)   → "Rectangle: area=24.00, perimeter=20.00"
#                        (uses type(self).__name__, self.area(), self.perimeter())
#
# Rectangle(Shape): w, h → area=w*h, perimeter=2*(w+h)
# Circle(Shape):    r    → area=3.14159*r², perimeter=2*3.14159*r
# Triangle(Shape):  a, b, c (sides), h (height to base a)
#                        → area=0.5*a*h, perimeter=a+b+c
#
# compare_shapes(s1, s2) → "{name1} is larger" or "{name2} is larger" or "Equal area"
#
# Expected output:
#   Rectangle: area=24.00, perimeter=20.00
#   Circle: area=78.54, perimeter=31.42
#   Triangle: area=12.00, perimeter=12.00
#   Circle is larger

import math

class Shape:
    pass  # TODO

class Rectangle(Shape):
    pass  # TODO

class Circle(Shape):
    pass  # TODO

class Triangle(Shape):
    pass  # TODO

def compare_shapes(s1, s2):
    pass  # TODO


r = Rectangle(4, 6)
c = Circle(5)
t = Triangle(3, 4, 5, 8)   # sides 3,4,5 and height 8

print(r.summary())
print(c.summary())
print(t.summary())
compare_shapes(r, c)
