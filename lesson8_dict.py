# dict_def_food={
#     "food": ["варення", "їда", "їжа", "їство", "наїдок","пожива"],
#     "eating": ["їда", "їжа"]
# }
# print(dict_def_food)

# # print(dict_def_food.keys())
# # print(dict_def_food.values())
# # print(dict_def_food.items())

# #meat зміст, їжа, м'ясиво, м'ясо

# dict_def_food["meet"]=["їжа","м'ясиво","м'ясо"]
# print(dict_def_food)
# # dict_def_food["food"]="nothing...."
# # print(dict_def_food)


# for list_words in dict_def_food.values():
#     print(list_words)


# print("="*20)
# for wordEng in dict_def_food.keys():
#     print(wordEng,":", sep="",end="\n\t")
#     for word in dict_def_food[wordEng]:
#         print(word,end="; ")   
#     print()

# #сформувати список справ на вихідні

# def print_list_todo():
#     for todo_of_day in list_todos.keys():
#         print(todo_of_day)
#         count_todo = 1
#         for todo_list in list_todos[todo_of_day]:
#             print(f'{count_todo}. {todo_list}')
#             count_todo += 1



# list_todos = {
#     "Saturday":["read book","homework","walk with friends"], 
#     "Sunday":["sleep until lunch","watch cartoon"]
# }
# list_todos["Saturday"].append("Clean my room")
# print(list_todos["Saturday"])
# print('-' * 30)
# print_list_todo()


# '''for todo_of_day in list_todos.keys():
#     print(todo_of_day)
#     count_todo = 1
#     for todo_list in list_todos[todo_of_day]:
#         print(f'{count_todo}. {todo_list}')
#         count_todo += 1
# '''
# #видалити зі списку зроблену справу назва справи водиться з клавіатури
# delete_todo = input("Введіть справу яку треба видалити: ")
# for todo_of_day in list_todos.keys():
#     if delete_todo in list_todos[todo_of_day]:
#         list_todos[todo_of_day].remove(delete_todo)
# print_list_todo()

# '''
# for todo_of_day in list_todos.keys():
#     print(todo_of_day)
#     count_todo = 1
#     for todo_list in list_todos[todo_of_day]:
#         print(f'{count_todo}. {todo_list}')
#         count_todo += 1
# '''

list_things=["велосипед","дрон","планшет"]

print(f'Я хочу купити {list_things[1]}')

for thing in list_things:
    print(f'Я хочу купити {thing}')



# HW8. Сформувати словник бібліотеки книжок кількох ваших улюблених авторів (наприклад,
# my_library={ “Шевченко”: ["Кобзар", "Катерина“], “Джоан Роулінг”:[“Гаррі Поттер”]).
# Продемонструвати роботу з ним: додавання книгу та видалити книгу певного автора.

