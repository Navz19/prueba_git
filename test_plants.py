from plants import COLOMBIAN_PLANTS
from plants import get_random_plant

def test_successfully_get_random_plant():
    random_plant = get_random_plant()
    assert type(random_plant) == str
    assert (random_plant in COLOMBIAN_PLANTS) is True
