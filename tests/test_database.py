from unittest.mock import Mock
from praktikum.database import Database


class TestDatabase:

    def test_available_buns_success(self):
        db = Database()
        mock_buns = [
            Mock(name="black bun", price=100),
            Mock(name="white bun", price=200),
            Mock(name="red bun", price=300)
        ]
        db.available_buns = Mock(return_value=mock_buns)
        assert db.available_buns() == mock_buns

    def test_available_ingredients_success(self):
        db = Database()
        mock_ingredients = [
            Mock(type='SAUCE', name="hot sauce", price=100),
            Mock(type='SAUCE', name="sour cream", price=200),
            Mock(type='SAUCE', name="chili sauce", price=300),
            Mock(type='FILLING', name="cutlet", price=100),
            Mock(type='FILLING', name="dinosaur", price=200),
            Mock(type='FILLING', name="sausage", price=300)
        ]
        db.available_ingredients = Mock(return_value=mock_ingredients)
        assert db.available_ingredients() == mock_ingredients
