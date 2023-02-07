# # if value1:
# #     commands
# # elif value2:
# #     commands
# # else:
# #     commands

# t=int(input("Input t:"))
# if t>18:
#     print("shirt")
# elif  t>=10 and t<=18:
#     print("skirt")  
# else:
#     print("warm jacket")

# # elif t<10:
# #     print("warm jacket")

# """
# while умова:
#     команди
# else:       #доцільно, коли використовується break
#     команди
# """

# '''
# Дано два цілих числа A і B (при цьому A ≤ B). 
# Виведіть всі числа від A до B включно.
# '''
# a=int(input("input a:"))
# b=int(input("input b:"))

# #1 to 4
# """
#      a  b     a<=b    print(a)    a=a+1
#  1)  1  4     1<=4    print(1)    a=1+1 => 2
#  2)  2  4     2<=4    print(2)    a=2+1 => 3
#  3)  3  4     3<=4    print(3)    a=3+1 =>4
# 4)   4  4     4<=4    print(4)    a=4+1 =>5
# 5)  5   4     5<=4   
# """

# while a<=b:
#     print(a,end="\t\a")
#     a=a+1
# print()
# print("the end cicle while")

# """
# for змінна in послідовність:
#    команди

# for змінна in послідовність:
#    команди
# else:
#    команди
# """
# a=int(input("input a:"))
# b=int(input("input b:"))
# for number in range(a,b+1):
#     print(number)

# for letter in "Python":  # ['P','y','t','h','o','n']
#     print(letter, end="\t")

# """
# Дано два цілих числа A і В. 
# Виведіть всі числа від A до B включно, в порядку зростання, 
# якщо A <B, або в порядку спадання в іншому випадку.
# """
# # 2   8       8   4
# a=int(input("input a:"))
# b=int(input("input b:"))

# if a<b:
#     while a<=b:
#         print(a,end="\t\a")
#         a=a+1
# else:
#     while a>=b:
#         print(a,end="\t\a")
#         a=a-1


# if a<b:
#     number=1
# else:
#     number=-1

# for n in range(a,b,number):
#     print(n, end="\t")

# print()

a=11
b=6

for i in range(a,b,-2):
    print(i, end="\t")

print()


for i in range(a,b,-1):
    if (i%2!=0):
        print(i, end="\t")

print()



 
    