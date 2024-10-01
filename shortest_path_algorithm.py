# Bismillah
"""
Created on Tue Oct  1 21:22:35 2024

@author: Faxriddin
"""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
del copper['age']

for i, j in copper.items():
    print(i, j)