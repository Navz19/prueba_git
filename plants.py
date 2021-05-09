import random


COLOMBIAN_PLANTS = [
    'Melón', 
    'Calabaza', 
    'Totumo', 
    'Palmera', 
    'Guayacán',
    'Cocotero',
    'Platanero',
    'Lechuga',
    'Mata de piña',
    'Mata de café',
    'Orquídea',
    'Uchuva',
    'Pino',
    'Achira',
    'Caña de azúcar',
    'Cocoa',
    'Brocoli',
    'Girasol',
    'Zuchini',
    'Pepino',
]


def get_random_plant():
    return random.choice(COLOMBIAN_PLANTS)
