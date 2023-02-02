# a=5
# b=8
# result=5==8
# print(result)
# False
# print(a!=b)
# True
# print(a>b)
# False
# print(a<b)
# True
# bool1=True
# bool2=False
# print(b and a)
# 5
# print(b>0 and a>=4)
# True
# print(not (b>0 and a>=4))
# False
#  value in siquence
from re import match

print("java" in "java JavaScript python")
print("java" not in "java JavaScript python")
#
# if logic_value:
#     statments1(instructions)
# [else:
#     statments2(instructions)]
#
find_java = "java" in "java JavaScript python"
if find_java:
    print("Result is True")
else:
    print("Result is False")

a=4
b=5
result=a if a>b else b
print(result)


# if logic_value1:
#     statments1(instructions)
# [elif logic_value2:
#     statments2(instructions)]
# [else:
#     statments3(instructions)]
#

n1 = 3
n2 = 5
n3 = -2

if n1 > n2 and n1 > n3:
    max_number = n1
elif n2 > n1 and n2 > n3:
    max_number = n2
else:
    max_number = n3

print("max=", max_number)

print(max(1, 2, 3))



""" switch
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default

until version 3.10
"""
#
# lang = input("What's the programming language you want to learn? ")
# match lang:
#     case "JavaScript":
#         print("You can become a web developer.")
#     case "Python":
#         print("You can become a Data Scientist")
#     case "PHP":
#         print("You can become a backend developer")
#     case "Solidity":
#         print("You can become a Blockchain developer")
#     case "Java":
#         print("You can become a mobile app developer")
#     case _:
#         print("The language doesn't matter, what matters is solving problems.")


"""
while
for
"""

#
# while logic_expression (logic_value):
#     statments
# else:
#     statments

#Вивести привіання 5 разів
print("Hello!" *5)

count=1
while count<=5:
    print(count,": Hello!")
    count+=1

print(sum([1,2,3,4]))

#Підрахувати суму 5 чисел, які  користувач вводить із клавіатури:
# count=0
# sumaN=0
# while count<5:
#     count += 1
#     x=input("input number #"+str(count)+":")
#     sumaN+=int(x)    #sumaN=sumaN+x
#
# print(sumaN)
# використання оператора while і додаткового блоку else
# count=0
# sumaN=0
# while count<5:
#     count += 1
#     x=input("input number #"+str(count)+":")
#     sumaN+=int(x)    #sumaN=sumaN+x
# else:
#     print(f"Result sum after cicle equal {sumaN}. Cicle finished!")
#
# print(sumaN)

# using break continue
#
# count=1
# sumaN=0
# while count<=5:
#     x=input("input number #"+str(count)+":")
#     # if  not type(int(x))==int:             #x.isdigit():
#     if x.isalpha():
#         print("Is not number")
#         break
#     if int(x)<0:
#         continue
#     sumaN+=int(x)    #sumaN=sumaN+x
#     count += 1
# else:
#     print(f"Result sum after cicle equal {sumaN}. Cicle finished!")
#
# print(sumaN)


# for item in sequence:
#     statments1
# else:
#     statments2

text="Python"
for symbol in text:
    print(symbol)
else:
    print(f"Last symbol: {symbol}. Cicle finished")

print("Work done!")


#table multiply

i=1
j=1
while i<10:
    while j<10:
        print(i*j,end="\t")
        j+=1
    print("\n")
    j=1
    i+=1

print(list(range(1,11)))
print(list(range(1,10,2)))
print(list(range(10,0,-1)))

s=0
for number in range(2,11,2):
    s+=number
    print(s)

print("s=",s)

