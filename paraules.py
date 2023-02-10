import random

paraules = [
    ['CIUTAT', 'ALAIOR'],
    ['CIUTAT', 'MADRID'],
    ['CIUTAT', 'BARCELONA'],
    ['CIUTAT', 'PARIS'],
    ['CIUTAT', 'SEVILLA'],
    ['ANIMAL', 'SERP'],
    ['ANIMAL', 'GIRAFA'],
    ['ANIMAL', 'RATOLI']
]


def retorna_paraula():
    if len(paraules) == 0:
        return False
    else:
        paraula = random.choice(paraules)
        paraules.remove(paraula)
        return paraula