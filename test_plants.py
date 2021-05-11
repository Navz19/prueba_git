import pytest
from plants import COLOMBIAN_PLANTS
from plants import get_random_plant

def test_successfully_get_random_plant():
    random_plant = get_random_plant()
    assert isinstance(random_plant, str)
    assert any(random_plant in T for T in COLOMBIAN_PLANTS.values())
    for key in COLOMBIAN_PLANTS.keys():
        random_plant = get_random_plant(key)
        assert isinstance(random_plant, str)
        assert any(random_plant in T for T in COLOMBIAN_PLANTS.values())
    
def test_unsuccesful_get_random_plant():
    with pytest.raises(KeyError):
        get_random_plant('Azul')