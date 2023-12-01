from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestIngredient:

    @pytest.mark.parametrize('ing_type, expected', [[INGREDIENT_TYPE_SAUCE, 'SAUCE'], [INGREDIENT_TYPE_FILLING, "FILLING"]])
    def test_ingredient_init_true(self,ing_type,expected):
        ingredient = Ingredient(ing_type, 'ketchup', 1.00)
        assert ingredient.type == expected
        assert ingredient.name == 'ketchup'
        assert ingredient.price == 1.00

    def test_get_type_valid_type_success(self):
        ingredient = Ingredient('SAUCE', 'ketchup', 1.00)
        assert ingredient.get_type() == 'SAUCE'

    def test_get_price_valid_type_success(self):
        ingredient = Ingredient('SAUCE', 'ketchup', 1.00)
        assert ingredient.get_price() == 1.00

    def test_get_name_valid_type_success(self):
        ingredient = Ingredient('SAUCE', 'ketchup', 1.00)
        assert ingredient.get_name() == 'ketchup'
