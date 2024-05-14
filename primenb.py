import math
i=2
num=int(input("enter number :"))
def prime(num):
    if num <= 1:
        return 0
    for i  in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 0
        return 1

if prime(num):
    print("not prime")
else:
    print("prime nb")








