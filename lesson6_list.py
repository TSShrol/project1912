markOfSt1FromPython=[10,11,9,10] # index from 0 end index 3
print(markOfSt1FromPython)
print(markOfSt1FromPython[1])
#print(markOfSt1FromPython[4])
markHWfrom2to3=markOfSt1FromPython[1:3] # 1, 2
print(markHWfrom2to3)
#видалення
del markOfSt1FromPython[3]
print(markOfSt1FromPython)
markOfSt1FromPython[2]=12
print(markOfSt1FromPython)

markOfSt1FromPython.append(10)
print("Append 10 to list:",markOfSt1FromPython)
markOfSt1FromPython.insert(1,9)
print("Insert 9 to list in position 2 (by index 1):",markOfSt1FromPython)

#copy list
markOfSt1FromGodot=markOfSt1FromPython.copy()
print("markOfSt1FromPython=",markOfSt1FromPython,"id (address) =", id(markOfSt1FromPython))
print("markOfSt1FromGodot=",markOfSt1FromGodot,"id (address) = ",id(markOfSt1FromGodot))

#create link on markOfSt1FromGodot
markOfSt1FromUnity=markOfSt1FromGodot
print("markOfSt1FromGodot=",markOfSt1FromGodot,"id (address) = ",id(markOfSt1FromGodot))
print("markOfSt1FromUnity=",markOfSt1FromUnity,"id (address) = ",id(markOfSt1FromUnity))

markOfSt1FromUnity[1]=12
print("markOfSt1FromGodot=",markOfSt1FromGodot,"id (address) = ",id(markOfSt1FromGodot))
print("markOfSt1FromUnity=",markOfSt1FromUnity,"id (address) = ",id(markOfSt1FromUnity))

"""
Збережіть імена кількох своїх друзів у списку з ім’ям names. 
Видаліть імя першого друга у списку та додайте його в кінець списку.
Виведіть ім’я кожного друга, звернувшись до кожного елементу списку (по одному разу).
"""
names=["Яна","Денис","Ваня"]
print("My friends:",names)
#add next friend
names.append("Владислав")
print("My friends after meet new friend:",names)
#add next friend
names.append("Максим")
print("My friends after meet new friend:",names)

#add next friend
names.insert(0,"Станіслав")
print("My friends after meet new friend:",names)

#add next friend
names.append("User")
print("My friends after meet new friend:",names)

print("Count my friends: ",len(names))
print("Count name 'Денис':",names.count("Денис"))

names.sort()
print("My friends after sorting:",names)

# names.reverse()
# print("My friends after reversing:",names)

# names.remove("User")
# print("My friends after deleting User:",names)

indexStrimniyUser=names.index("User")
print("indexStrimniyUser=",indexStrimniyUser)

nameStrimniyUser=names.pop(indexStrimniyUser)
print(f'Strimniy user {nameStrimniyUser} deleted from list names. My Friends:{names}')

names.append("Ілля") #index=6
names.append("Матвєй") #index=7

# print(names[0]) 
# print(names[1]) +1
# print(names[2]) +1
# print(names[3]) +1

print("="*20)
index=0
while(index<len(names)):
    print(names[index])
    index=index+1

print("="*20)
for name in names:  
    print(name)

for lang in ["JS","Python","C++","C#"]:
    print(f'{lang} - programming lang')