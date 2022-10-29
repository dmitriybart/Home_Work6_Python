#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

array = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen', 'anton', 'aoooooooooontooooo', 'elelelelelelelelelel', 'ntoneeee', 'tonee', '253235235a5323352n25235352t253523523235oo235523523523n', 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon', 'unton']
search_number = 253

result = list(filter((lambda x: str('253') in x), array))

if result !='':
    print('Присутствует')
else:
    print('Не присутствует')
