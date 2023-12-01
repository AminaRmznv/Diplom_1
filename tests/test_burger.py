from unittest.mock import Mock
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_init_valid_data_success(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_success(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.name = "Булка"
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock
        assert burger.bun.name == "Булка"

    def test_add_ingredient_success(self):
        burger = Burger()
        ingredient = Ingredient("SAUCE", "Test Sauce", 0.5)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_success(self):
        burger = Burger()
        ingredient = Ingredient("SAUCE", "Test Sauce", 0.5)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient_success(self):
        burger = Burger()
        ingredient = Ingredient("SAUCE", "Test Sauce", 0.5)
        ingredient_2 = Ingredient("FILLING", "Meat", 5.20)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_2

    @patch('praktikum.bun.Bun.get_price')
    @patch('praktikum.ingredient.Ingredient.get_price')
    def test_get_price_success(self, mock_ingredient_get_price, mock_bun_get_price):
        mock_bun_get_price.return_value = 2.0
        mock_ingredient_get_price.return_value = 20
        bun = Bun("Test Bun", mock_bun_get_price.return_value)
        ingredient = Ingredient("SAUCE", "Test Sauce", mock_ingredient_get_price.return_value)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_price = 2 * mock_bun_get_price.return_value + mock_ingredient_get_price.return_value
        assert burger.get_price() == expected_price

    @patch('praktikum.bun.Bun.get_name')
    @patch('praktikum.bun.Bun.get_price')
    @patch('praktikum.ingredient.Ingredient.get_type')
    @patch('praktikum.ingredient.Ingredient.get_name')
    @patch('praktikum.ingredient.Ingredient.get_price')
    def test_get_receipt(self, mock_ingredient_get_price, mock_ingredient_get_name,
                         mock_ingredient_get_type, mock_bun_get_price, mock_bun_get_name):
        mock_bun_get_name.return_value = "Test Bun"
        mock_bun_get_price.return_value = 2.0
        mock_ingredient_get_price.return_value = 0.5
        mock_ingredient_get_name.return_value = "Test Sauce"
        mock_ingredient_get_type.return_value = "SAUCE"

        bun = Bun(mock_bun_get_name.return_value, mock_bun_get_price.return_value)
        ingredient = Ingredient(mock_ingredient_get_type.return_value,
                                mock_ingredient_get_name.return_value,
                                mock_ingredient_get_price.return_value)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f"(==== Test Bun ====)\n= sauce Test Sauce =\n(==== Test Bun ====)\n\nPrice: 4.5"
        assert burger.get_receipt() == expected_receipt
