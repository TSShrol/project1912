# str1="Python"
# print(str1)
# str2="JavaScript" 
# print(type(str1))
# print(str1.index('y'))
# num1=345
# print(num1)
# print(type(num1))
# str1=45
# print(str1)

# +,-     +,-,*,/,//,%
#Обчислити значення виразу: (a+b)^3+a*b, якщо a=4, b=7. Дані ввети з клавіутри
a=4
b=7
a=int(input("Input a:"))
b=int(input("Input b:"))
print("result=",(a+b)**3+a*b)
viraz=(a+b)**3+a*b
print("result=",viraz)




# suma=345
# print("suma =",suma)
# #збільшити дану суму на число 20 3 рази
# suma=suma+20
# #suma+=20
# print("suma =",suma)
# suma=suma+20
# print("suma =",suma)
# suma=suma+20
# print("suma =",suma)

# print("$"*30)
# suma=345
# count=1
# while(count<=3):
#     suma=suma+20
#     print("suma =",suma)
#     if(count==2):
#         break
#     count=count+1
# else:
#     print("The END")

# suma=345

# print(range(3))



#Визначити чи попадає точка в круг радіусу R
print("Введіть координати точки (x,y):")
x=float(input("x="))
y=float(input("y="))
R=float(input("Введіть R:"))

#x^2+y^2<=R^2   x=3, y=4, R=5   3*3+4*4=25   25<=25
if (x**2+y**2<=R**2):
    print("Попадає!")
else:
    print("НЕ попадає!")