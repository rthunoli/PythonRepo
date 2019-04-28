# import math
# radius = input("Enter a radius of a circle : ")
# area = math.pi * float(radius) ** 2
# print("Area : {:<10.3f}".format(area))

# numbers = [1,2,3,4,5]
# it = iter(numbers)
# while(True):
#     try:
#         print(next(it))
#     except:
#         break

# def myGenerator():
#     for _ in range(1,11):
#         yield _*2
#
# for _ in myGenerator():
#     print(_)

# bases=[10, 20, 30, 40, 50]
# index=[1, 2, 3, 4, 5]
# powers=list(map(pow, bases, index))
# print(powers)


# def isPrime(x):
#     if x%2 == 0:
#         return False
#     for n in range(3,int(x/2)):
#         if x%n==0:
#             return False
#     else:
#         return True
#
# fltrObj=filter(isPrime, range(100000))
# print ('Prime numbers between 1-10:', list(fltrObj))

# import functools
# def mult(x,y):
#     print("x=",x," y=",y)
#     return x*y
#
# fact=functools.reduce(mult, range(1, 6))
# print ('Factorial of 5: ', fact)
#


def fact(n):
    if n == 1:
        print(1)
        return 1

    print(n,"*" ,end=" ")
    return n * fact(n-1)

print(fact(10))
