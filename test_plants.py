import pytest
from plants import COLOMBIAN_PLANTS, PlantTypeDoesNotExistsError
from plants import get_random_plant

def test_successfully_get_random_plant():
    random_plant = get_random_plant()
    assert isinstance(random_plant, str)
    assert any(random_plant in plant_type_list for plant_type_list in COLOMBIAN_PLANTS.values())

def test_successfully_get_random_plant_by_type():
    for plant_type in COLOMBIAN_PLANTS.keys():
        random_plant = get_random_plant(plant_type)
        assert isinstance(random_plant, str)
        assert any(random_plant in plant_type_list for plant_type_list in COLOMBIAN_PLANTS.values())
    
def test_get_random_plant_invalid_type():
    unregistered_plant_type = "Azul"
    with pytest.raises(PlantTypeDoesNotExistsError):
        get_random_plant(unregistered_plant_type)