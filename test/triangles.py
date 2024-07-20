#Q1 Print this pattern
# *
# **
# ***
# ****
# *****

# def star_pattern(rows):
#   for i in range(1, rows + 1):
#     print("*" * i)

# star_pattern(5)

#Q2 Print make Q1 a user inputable height

# def star_pattern(rows):
#    for i in range(1, rows + 1):
#       print("*" * i)
# a = int(input("How BIG u want triangle  "))
# star_pattern(a)

#Q3 Make inverted version of Q1/Q2

# def star_pattern_inverted(rows):
#    for i in range(rows, 0, -1):
#       print("*" * i)
# a = int(input("How BIG u want triangle  "))
# star_pattern(a)

#Q4 make a hollowed version of Q1/Q2 
#i.e hollow
# *
# **
# * *
# *  *
# *****

# def star_pattern_hollow(rows):
#    for i in range(1, rows + 1):
#       for j in range(i):
#          # if j not equal to 0 or i - 1 print " "
#          # if j is equal to i or 0 print "*"

def star_pattern_hollow(rows):
   for i in range(1, rows):
      for j in range(i):
         if j == 0:
            print("*", end = '')
         elif j == i - 1:
            print("*", end = '')
         else :
            print(" ", end = '')
      print()
   print("*" * rows)

a = int(input("How BIG u want triangle  "))
star_pattern_hollow(a)