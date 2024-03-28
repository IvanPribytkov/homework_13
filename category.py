class Category:
    total_categories = 0  # Общее количество категорий
    total_unique_products = 0  # Общее количество уникальных продуктов (не учитывая количество в наличии)

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация объекта Category.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список продуктов в данной категории.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set(products))  # Добавляем количество уникальных продуктов из списка

    def add_product(self, product):
        """
        Добавление продукта в категорию.

        :param product: Продукт для добавления.
        """
        self.products.append(product)
        Category.total_unique_products = len(set(self.products))  # Обновляем количество уникальных продуктов
