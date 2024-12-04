my_dict = {'Dasha' : 1992, 'Masha' : 1999, 'Glasha' : 2003}
print('Список людей и их годов рождения: ', my_dict)
print('Существующее значение: ', my_dict.get('Dasha'))
print('Несуществующее значение: ', my_dict.get('Sasha'))
my_dict.update({'Lera': 2001, 'Sveta': 2005})
a = my_dict.pop ('Masha')
print("Удаленное значение: ", a)
print("Измененный список людей и их годов рождения: ", my_dict)

my_set = {1,2,1,2,3,4,5,1,22, 'law', (1, 2, 3) }
print("Множество: ", my_set)
my_set.update({7, 65, 'fgd'})
my_set.discard(1)
print("Измененное множество: ", my_set)

