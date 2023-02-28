dict = {}
for i in range(1,5):
    dict[i] = i * 2
    
print(dict)

''' CON UNA SINTAXIS MAS CORTA'''

dict_v2 = {i: i * 2 for i in range(1,5)}
print(dict_v2)

'''otro tipo de ejemplo'''


import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
    
print(population)

population_v2 = {country: random.randint(1,100) for country in countries}

"NOMBRES DE USUARIOS EN LISTAS"

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names,ages)))

new_dict = {name: age for (name,age) in zip(names,ages)}
