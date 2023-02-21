numbers=list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[0])
hw_mark_1912_1=10
hw_mark_1912_2=11
hw_mark_1912_3=10
hw_mark_1912_4=11
hw_mark_1912_5=10
hw_mark_1912_6=11
hw_mark_1912_7=10
hw_mark_1912_8=11
hw_mark_1912_9=11

ser=(hw_mark_1912_1+hw_mark_1912_2+hw_mark_1912_3+hw_mark_1912_4+hw_mark_1912_5+hw_mark_1912_6+hw_mark_1912_7+hw_mark_1912_8+hw_mark_1912_9)/9
print(f'ser={ser}')
list_marks_hw=list() #   list_marks_hw=[]
print(list_marks_hw)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(10)
list_marks_hw.append(11)
list_marks_hw.append(11)
print(list_marks_hw)

"""
# kahoot [0-100]
#заповнили список балами 9-студентів
list_marks_by_kahoot=[]
for indexByMagazin in range(1,10): # 1,2, ...,9
    markByKahoot=int(input(f'Input mark by kahoot students number of {indexByMagazin}: '))
    list_marks_by_kahoot.append(markByKahoot)

print(f'list marks by kahoot: {list_marks_by_kahoot}')

#зчитали дані зі списку, просумували
suma=0 
for indexByMagazin in range(0,len(list_marks_by_kahoot)):  #range(0,9)
    suma=suma+list_marks_by_kahoot[indexByMagazin]

print(f'suma all marks: {suma}')
#середнє арифметичне
ser=suma/len(list_marks_by_kahoot)

print(f'ser={ser}')
"""

#creating topics ingradients of pizza
#доступні і пфцерії
avaliable_toppings=['mushrooms','olives','pepperoni','extra cheese','green peppers','tomatos']

#замолення клієнта
requested_toppings=['mushrooms','pepperoni','pineapple']

my_pizza=[]

#готується наша піца
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings: #True
        print(f'Adding {requested_topping} on pizza')
        my_pizza.append(requested_topping)
    else: #False
        print(f'Sorry, we don\'t have {requested_topping}')

print(f'My pizza:{my_pizza}')
other_list=[3,4,7.8, "JS",[67,77]]
#include_list=other_list[4] # include_list[1]
print(other_list[0])
print(other_list[4][1])
other_list[0]=33


#кортежі 
tuple1=("nik23","Andriy","andriy@gmail.com","qwerty-1")
login, username,email, password=tuple1

print(f'Userinfo: {login}; {username}, {email},{password} ')

tuple2=("www.logbook.org",)