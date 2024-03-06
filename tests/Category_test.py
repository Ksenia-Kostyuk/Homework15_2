import pytest
from main.Category import Category

@pytest.fixture
def category_test():
    return Category('Фрукты', 'Сладкие, спелые и свежие', ['Яблоки', 'Апельсины', 'Персики'])

def test_init_category(category_test):
    assert category_test.name == 'Фрукты'
    assert category_test.description == 'Сладкие, спелые и свежие'
    assert category_test.products == ['Яблоки', 'Апельсины', 'Персики']
    assert category_test.products_return() == 'Яблоки, Апельсины, Персики'