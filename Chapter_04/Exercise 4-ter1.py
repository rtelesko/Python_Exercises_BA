number = int(input("Please enter an integer: "))

# 1 is not being a prime number, is ignored
if number > 1:
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            print(number, "is NOT a prime number.")
            break
    else:
        print(number, "is a prime number.")

else:
    print(number, "is NOT a prime number.")
