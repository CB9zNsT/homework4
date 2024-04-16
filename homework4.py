immutable_var = 1, 2, True, False
print(immutable_var)

#immutable_var([0], 2) в кортеже данные не изменяются. Но если добавить список в кортеж, список внутри можно будет изменить
#print(immutable_var)

mutable_list = [2, 3, 'Sergey']
print(mutable_list)

mutable_list[2] = 'David'
print(mutable_list)