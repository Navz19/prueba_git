import random
COLOMBIAN_PLANTS = dict(
PLANT_TYPE_FRUIT = [
    'Melón',
    'Cocotero',
    'Platanero',
    'Mata de piña',
    'Uchuva',
    'Granadilla'
],
PLANT_TYPE_VEGETABLE = [
    'Calabaza',
    'Lechuga',
    'Brocoli',
    'Zuchini'
],
PLANT_TYPE_FLOWER = [
    'Guayacán',
    'Orquídea',
    'Girasol'
],
PLANT_TYPE_OTHER = [
    'Totumo',
    'Palmera',
    'Mata de café',
    'Pino',
    'Achira',
    'Caña de azúcar',
    'Cocoa'
])


def get_random_plant(plant_type=None):
    if plant_type is None:
        random_type = random.choice(list(COLOMBIAN_PLANTS.keys()))
        return random.choice(COLOMBIAN_PLANTS[random_type])
    if plant_type in COLOMBIAN_PLANTS.keys():
        return random.choice(COLOMBIAN_PLANTS[plant_type])
    raise KeyError(f"Plant type '{plant_type}' is not allowed")