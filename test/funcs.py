# get input from user and print factorial of input
# using a user defined function 'factorial(n)'

# def <function_name>(<parameters>):
#   <code>
#   

# def add(a,b):
#     return a+b

# x = add(66,2)
# print(x)

# a = int(input("Ur number plz  ")) 
# fact = 1

# while a>1:
#     fact = fact * (a)
#     a=a-1
#     print(fact)

def factorial(n):
    fact = 1
    while n>1:
        fact = fact * (n)
        n=n-1
    return fact

def main():
    n = int(input("Ur number plz  "))
    a = factorial(n)
    print(a)

if __name__=="__main__":
    main()