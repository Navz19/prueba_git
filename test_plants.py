from plants import COLOMBIAN_PLANTS, PLANT_TYPE_FRUIT, PLANT_TYPE_VEGETABLE, PLANT_TYPE_FLOWER
from plants import get_random_plant

def test_successfully_get_random_plant():
    random_plant = get_random_plant()
    assert type(random_plant) == str
    assert (random_plant in COLOMBIAN_PLANTS) is True

def test_successfully_get_random_fruit():
    random_fruit = get_random_plant(plant_type='fruta')
    assert type(random_fruit) == str
    assert (random_fruit in PLANT_TYPE_FRUIT) is True

def test_successfully_get_random_vegetable():
    random_vegetable = get_random_plant(plant_type='verdura')
    assert type(random_vegetable) == str
    assert (random_vegetable in PLANT_TYPE_VEGETABLE) is True

def test_successfully_get_random_flower():
    random_flower = get_random_plant(plant_type='flor')
    assert type(random_flower) == str
    assert (random_flower in PLANT_TYPE_FLOWER) is True