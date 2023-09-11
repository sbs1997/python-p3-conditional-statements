#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password =="12345":
        return "Access granted"
    else:
        return "Access denied"
    
# print(admin_login("admin", "12345"))
# print(admin_login("failure", "12345"))

def hows_the_weather(temperature):
    def describe_weather(temp):
        if temperature < 40:
            return "brisk"
        if temperature < 65:
            return "a little chilly"
        if temperature > 85:
            return "too dang hot"
        return "perfect"
    return f"It's {describe_weather(temperature)} out there!"

def fizzbuzz(num):
    if num%3 == 0:
        if num%5 == 0:
            return "FizzBuzz"
        return "Fizz"
    if num%5 == 0:
        return "Buzz"
    return num


def calculator(operation, num1, num2):
    if operation == "+":
        return num1+num2
    if operation == "-":
        return num1-num2
    if operation == "*":
        return num1*num2
    if operation == "/":
        return num1/num2
    print("Invalid operation!")
    return None

