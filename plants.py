import random

PLANT_TYPE_FRUIT = [
    'Melón',
    'Cocotero',
    'Platanero',
    'Mata de piña',
    'Uchuva',
    'Granadilla'
]
PLANT_TYPE_VEGETABLE = [
    'Calabaza',
    'Lechuga',
    'Brocoli',
    'Zuchini'
]

PLANT_TYPE_FLOWER = [
    'Guayacán',
    'Orquídea',
    'girasol'
]

PLANT_TYPES = [
    'fruta',
    'verdura',
    'flor'
]

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
    'Granadilla',
]


def get_random_plant(plant_type=None):
    if plant_type is None:
        return random.choice(COLOMBIAN_PLANTS)
    if plant_type == 'fruta':
        return random.choice(PLANT_TYPE_FRUIT)
    if plant_type == 'verdura':
        return random.choice(PLANT_TYPE_VEGETABLE)
    if plant_type == 'flor':
        return random.choice(PLANT_TYPE_FLOWER)
    if plant_type not in PLANT_TYPES:
        raise TypeError(f"Plant type '{plant_type}' is not allowed")
    return None