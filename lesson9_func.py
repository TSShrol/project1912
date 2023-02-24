import math 
print(math.sqrt(16))
print(math.sqrt(16)+sum([3,4,5]))

#create function suma of add two numberaad items our numbers list 

#зчитали дані зі списку, просумували
list_number=[2,3,6,8,9]

suma=0 
for index in range(0,len(list_number)):  #range(0,5)
    suma=suma+list_number[index]

print(suma)


def sumaOflist(list_num=[]):
    suma=0 
    for number in list_num:
        suma=suma+number
    print(f'suma={suma}')

sumaOflist(list_number)
print(sumaOflist([3,4,5,6]))

result_sum=sum([3,4,5,6])
print("result_sum=",result_sum)


def sumaOflistReturn(list_num=[]):
    suma=0 
    for number in list_num:
        suma=suma+number
    return suma

result_sum=sumaOflistReturn([3,3,3])
print("result_sum=",result_sum)

#визначити функцію, яка виводить привітання. Hello, WOrld!

def hello():
    print("Hello, World!")

hello()
hello()
hello()

def helloFriend(name=""):
    print(f"Hello, {name}! How are you?")

helloFriend("Artem")
helloFriend("Yana")
helloFriend("Polina")
helloFriend("Matviej")

def helloFriend1(name, age):
    print(f"Hello, {name}! You have {age} yeas old.")

helloFriend1("Denis",12)
helloFriend1("Illya",14)
helloFriend1(name="Stanislav",age=12)
helloFriend1(age=14, name="Ivan")

#hw Написати функцію make_shirt(), що приймає, як параметр два значення: ромір футболки
#  і що на ній написати. Функція виводить інформацію про цю футболку.
#  За замовчуванням можуть передаватися значення розміру М  і логоти  "I love Ukrain"

def make_shirt(size="M", logo="I love Ukraine"):
    pass # тут має бути ваш код

