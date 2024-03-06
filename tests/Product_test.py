import pytest
from main.Products import Product


@pytest.fixture
def product_test():
    return Product('Яблоки', 'Белый налив, сбор 2023 года', 70.0, 50)


def test_init_product(product_test):
    assert product_test.name == 'Яблоки'
    assert product_test.description == 'Белый налив, сбор 2023 года'
    assert product_test._pay == 70.0
    assert product_test.remain == 50