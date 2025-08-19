import sympy

number = int(input("Please enter an integer: "))

if sympy.isprime(number):
    print(number, "is a prime number.")
else:
    print(number, "is NOT a prime number.")
