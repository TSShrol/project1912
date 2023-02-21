str1="python"
str2="""JavaScript"""
str3='C++'
print(id(str1))
strNew=str1.capitalize()
# виведення значення змінної str1
print(str1)
# виведення адреси оперативної памяті,де зберігається str1
print("id(str1) =",id(str1))

print(strNew)
print(id(strNew))

# конкатенація або обєдання
str1=str1+str2  # pythonJavaScript
print(str1)
print("id(str1) =",id(str1))

print("Hello"*3)
# Вирізати із str1= "pythonJavaScript"  підрядок "Java"
print("str1= ",len(str1))
strAboutJava=str1[6:10]
print(strAboutJava)
print(strAboutJava[::-1])
print("first symbol =",str1[0])
print("last symbol =",str1[-1])
print("last symbol =",str1[len(str1)-1])

#повернути код в ascii таблиці символів від 'a' (96) до 'z'   'A' (65)
for symbol in 'abcdef'.upper():
    print(ord(symbol),end="\t")

print()
#вивести символи кодів ascii таблиці від 30 до 100
for kod in range(32,101):
        print(chr(kod),end="\t")

print()

#Визначити чи  слово "Java" є у введеному рядку 
inputStr=input("Введіть рядок:")
if (inputStr.find("Java")>=0):
    print("string 'Java' is finded")
else:
    print("string 'Java' isn't finded")

"""
   Знайдіть відому цитату, яка вам подобається, і збережіть у змінній citate. 
   Збережіть ім’я автора вислову у змінній famous_person. 
   Cкладіть повідомлення і збережіть його у новій змінній з ім’ям message.
    Виведіть своє повідомлення. 
    Результат повинен виглядати приблизно так (включаючи лапки): 
    Albert Einstein once said, "A person who never made a mistake never tried anything new.".
"""
famous_person="Albert Einstein"
citate="A person who never made a mistake never tried anything new"
message=famous_person+" once said, \""+citate+"\""
message1=f'{famous_person} once said, "{citate}"'
message2=famous_person+' once said, "' +citate+'"'
print(message)
print(message1)
print(message2)

msg="""
Збережіть ім’я користувача у змінній і додайте на початку і у кінці імені кілька пропусків.
 Простежте за тим, щоб кожна керуюча послідовність (\t і \n) зустрічалася принаймні один раз. 
 Виведіть ім’я, щоб було видно пропуски на початку і в кінці рядка. 
Потім виведіть його знову з використанням кожної з функцій видалення пропусків: lstrip(), rstrip() і strip().
"""
userName="  Katrin   "
print(userName)
print(userName.strip())
userName="****Katrin****"
print(userName)
print(userName.strip("*"))

print(msg.split("."))





