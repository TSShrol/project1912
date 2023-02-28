# На вхід програми подається один рядок з цілими числами.
#  Числа розділені пропусками. Необхідно вивести суму цих чисел
# Наприклад, якщо був введений рядок чисел 2 -1 9 6, то результатом роботи програми буде їх сума 16.
str_number="2 -1 9 6"
list_number=str_number.split() # " "
print(list_number)

suma_number=0
for number in list_number:
    suma_number=suma_number+int(number)

print(suma_number)


str_number="2 -1 9 6"
list_number=[ int(n) for n in str_number.split()] # " "
print(list_number)

suma_number=0
for number in list_number:
    suma_number=suma_number+number

print(suma_number)


"""
Дано список чисел.
 Визначте, скільки в цьому списку елементів, 
 які більші двох своїх сусідів, і виведіть кількість таких елементів.
"""

import random

list1=[]

for n in range(0,20):
    list1.append(random.randint(0,99))

print(list1)

count=0

for i in range(1,19):
    if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
        print(f' {list1[i]}>{list1[i-1]} і {list1[i]}>{list1[i+1]}')
        count+=1
    
print("count=",count)    


# Дано двовимірний масив розміру nxn.
# Знайти суму елементів матриці, розташованих між першим
#  і другим додатними елементами кожного рядка.

arr=[
    [3,4,7],
    [7,8,9],
    [56,34,67]
]

for row in arr:
    #print(row)
    for col in row:
        print(col, end="\t")
    print()

#генерування матриці nxn
n=3
arr2=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(random.randint(0,99))
    arr2.append(row)

print(arr2) 


for row in arr2:
    #print(row)
    for col in row:
        print(col, end="\t")
    print()
# for n in range(0,20):
#     list1.append(random.randint(0,99))

#suma elementiv matrix
suma_arr=0
for row in arr2:
    suma_arr=sum(row) #max, min
    # for col in row:
    #     suma_arr+=col
    
print(suma_arr)

max_n=arr2[0][0]
for row in arr2:
    for col in row:
        if max_n<col:
            max_n=col

print("max=",max_n)

