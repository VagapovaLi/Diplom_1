import pytest

from praktikum.bun import Bun

class TestBun:
    @pytest.mark.buns
    def test_buns_give_name_and_price(self):
        name ='Соевая булка'
        price = 10
        bun = Bun(name,price)
        assert bun.get_name() == name
        assert bun.get_price() == price