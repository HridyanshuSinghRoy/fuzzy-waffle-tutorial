#for i in range(l,u): range(u) => range(0,u)
#   <code>
#
# l -> u - 1
#
#while <condition>:
#   <code>

# Q1
# make a code that prints numbers from 0 - 100 using for and while loop

# for i in range(0,101):
#     print(i)

# a=0
# while a<=100:
#     print(a)
#     a=a+1

# Q2
# fizzbuzz : print numbers from 1 - 100
# but when a number is divisible by 3 print "fizz" instead
# but when a number is divisible by 5 print "buzz" instead
# and when divisible by both print "fizzbuzz"
# print the number itself if not divisible by either
# (hint : use %)

# a = 15
# b = a % 4
# print(b)

# a=1
# while a<=100:
#     b=a%3
#     c=a%5
#     if b==0 and c==0:
#         print("fizzbuzz")
#     elif b==0:
#         print("fizz")
#     elif c==0:
#         print("buzz")
#     elif b!=0 and c!=0:
#         print(a)
#     a=a+1

# for a in range(1,101):
#     if a % 3 == 0 and a % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif a % 3 == 0:
#         print("fizz")
#         continue
#     elif a % 5 == 0:
#         print("buzz")
#         continue
#     print(a)

# Q3
# print the factorial of input number using a loop
# (hint: use another dummy variable)
# l -> u - 1

# a = int(input("Ur number plz  "))
# fact = 1 #save the here

# for i in range(1, a + 1):
#     fact = fact * i
#     # print(fact)
# # print(fact)

# a = int(input("Ur number plz  "))
# fact = a #save the here

# for i in range(1, a):
#     fact = fact * i
#     print(fact)
# print(fact)

# a = int(input("Ur number plz  "))  
# fact = 1

# while a>1:
#     fact = fact * (a)
#     a=a-1
#     print(fact)


