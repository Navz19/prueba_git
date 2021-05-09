import random

PLANT_TYPE_FRUIT = 'fruta'
PLANT_TYPES = [
    PLANT_TYPE_FRUIT,
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
    if plant_type == PLANT_TYPE_FRUIT:
        # TODO: return random fruit
        return None
    # TODO: add more plant types validation

    if plant_type not in PLANT_TYPES:
        # TODO: raise an error if plant type is invalid
        return None
