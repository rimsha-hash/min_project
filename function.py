def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
num=input(int("Enter number: "))
print(f"{num} is prime number " if is_prime(num) else f"{num} is not prime number")

