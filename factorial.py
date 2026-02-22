#efficiency code
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=int(input("enter number: "))
print(f"Factorial of {num} is {factorial(num)}")
#more efficient code
import math
num=int(input("enter  valid number:"))
print(f"Factorial of {num} is {math.factorial(num)}")