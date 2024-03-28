import pytest
from category import Category
from product import Product

@pytest.fixture
def sample_product():
    return Product("Sample Product", "Description", 10.99, 50)

@pytest.fixture
def sample_category():
    return Category("Sample Category", "Category Description")

def test_category_init(sample_category):
    assert sample_category.name == "Sample Category"
    assert sample_category.description == "Category Description"
    assert sample_category.products == []
    assert Category.total_categories == 1

def test_product_init(sample_product):
    assert sample_product.name == "Sample Product"
    assert sample_product.description == "Description"
    assert sample_product.price == 10.99
    assert sample_product.quantity == 50

def test_add_product_to_category(sample_product, sample_category):
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 1
    assert Category.total_unique_products == 1

def test_count_categories(sample_category):
    assert Category.total_categories == 3
