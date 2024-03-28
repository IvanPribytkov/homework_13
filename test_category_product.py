import pytest
from product import Product
from category import Category

@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Description 1", 10, 50),
        Product("Product 2", "Description 2", 20, 30),
        Product("Product 3", "Description 3", 15, 40)
    ]

@pytest.fixture
def empty_category():
    return Category("Empty Category", "Empty Category Description", [])

def test_category_counters_increment(sample_products, empty_category):
    initial_total_categories = Category.total_categories
    initial_total_unique_products = Category.total_unique_products

    # Создаем категорию с тремя продуктами
    category = Category("Sample Category", "Category Description", sample_products)

    assert Category.total_categories == initial_total_categories + 1  # Увеличилось ли количество категорий на 1
    assert Category.total_unique_products == initial_total_unique_products + len(
        set(sample_products))  # Увеличилось ли количество уникальных продуктов на количество уникальных продуктов в списке

    # Добавляем продукт в пустую категорию
    empty_category.add_product(Product("New Product", "New Product Description", 25, 10))
    assert Category.total_unique_products == initial_total_unique_products + 1  # Увеличилось ли количество уникальных продуктов на 1
