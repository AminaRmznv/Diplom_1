class TestBun:

    def test_bun_init_true(self, create_bun):
        assert create_bun.name == 'Сырная булочка'
        assert create_bun.price == 1.15

    def test_get_name_valid_type_success(self, create_bun):
        assert create_bun.get_name() == 'Сырная булочка'

    def test_get_price_valid_type_success(self, create_bun):
        assert create_bun.get_price() == 1.15
