#!/usr/bin/env python3
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by zero!")
        return a / b

    def power(self, num1, num2):
        return num1**num2
