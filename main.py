# Lpu project ( you have to enter a range [a, b] and system will randomly
#
# Pick any number from your given range
# And check the status of that given number.
 import random

 n = range(int(input("Enter the range: ")),int(input()))
 Rng=[]
 for i in n:
     Rng.append(i)
 num = int(random.choice(Rng))
 print("The randomly selected number is : ", num)
 # (1.) Check for positive,negative or zero number
 if num > 0:
     print(num, "is a positive number")
 elif num < 0:
     print(num, "is a negative number")
 else:
     print("entered number is zero!")
 # (2.) Check for Even or Odd number
 if num % 2 == 0:
     print("{0} is an Even number".format(num))
 else:
     print("{0} is a Odd number".format(num))
 # (3.) Check for prime or composite.
 if num > 1:
     for i in range(2, num):
         if (num % i) == 0:
             print(num, "is a not  prime number")
             print(i, "times", num // i, "is", num)
             break
     else:
         print(num, "is a prime number")
 else:
     print(num, "is a composite number")

def factorial(value):
    if value==0:
        return 1
    else:
        return(value*factorial(value-1))
print(factorial(0))


