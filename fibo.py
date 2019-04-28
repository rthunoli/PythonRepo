"""Fibonacci series module"""
def fibo(n):
    FiboList=[]
    a,b=0,1
    while b<n:
        FiboList.append(b)
        a, b = b, a+b
    return FiboList
if __name__== "__main__":
    print ("Fibonacci series", fibo(100))
