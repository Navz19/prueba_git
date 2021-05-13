import random


class PlantTypeDoesNotExistsError(Exception):
    pass

COLOMBIAN_PLANTS = {
'fruit' : ['Melón','Cocotero', 'Platanero', 'Mata de piña', 'Uchuva', 'Granadilla'],
'vegetable' : ['Calabaza', 'Lechuga', 'Brocoli', 'Zuchini'],
'flower' : ['Guayacán', 'Orquídea', 'Girasol'],
'other_plants' : ['Totumo', 'Palmera', 'Mata de café', 'Pino', 'Achira', 'Caña de azúcar', 'Cocoa']
}


def get_random_plant(plant_type=None):
    if plant_type is None:
        random_type = random.choice(list(COLOMBIAN_PLANTS.keys()))
        return random.choice(COLOMBIAN_PLANTS[random_type])
    if plant_type in COLOMBIAN_PLANTS.keys():
        return random.choice(COLOMBIAN_PLANTS[plant_type])
    raise PlantTypeDoesNotExistsError