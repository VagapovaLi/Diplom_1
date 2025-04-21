import pytest
from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDatabase:

    @pytest.mark.parametrize("expected_bun", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns(self, expected_bun):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3

        bun_name, bun_price = expected_bun
        assert any(bun.get_name() == bun_name and bun.get_price() == bun_price for bun in buns), \
            f"Bun {bun_name} with price {bun_price} not found in database"



    @pytest.mark.parametrize("expected_ingredient", [
        Ingredient('SAUCE', "hot sauce", 100.0),
        Ingredient('SAUCE', "sour cream", 200.0),
        Ingredient('SAUCE', "chili sauce", 300.0),
        Ingredient('FILLING', "cutlet", 100.0),
        Ingredient('FILLING', "dinosaur", 200.0),
        Ingredient('FILLING', "sausage", 300.0)
    ])

    def test_available_ingredients(self, expected_ingredient):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        assert any(
            ingredient.get_type() == expected_ingredient.get_type() and
            ingredient.get_name() == expected_ingredient.get_name() and
            ingredient.get_price() == expected_ingredient.get_price()
            for ingredient in ingredients),\
            (f"Ingredient {expected_ingredient.get_name()} of type {expected_ingredient.get_type()}"
             f" with price {expected_ingredient.get_price()} not found in database")