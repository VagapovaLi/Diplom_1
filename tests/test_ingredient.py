
import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_ingredient_give_name_price_type(self):
        name = 'сок лимона'
        price = 10
        type = 'соус'

        ingredient =Ingredient(type, name, price,)

        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == type