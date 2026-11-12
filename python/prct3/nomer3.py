class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def is_available(self, quantity):
        return self.stock >= quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Формат: {объект_Product: количество}

    def add_item(self, product, quantity=1):
        if product.is_available(quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            print(f"Добавлено: {product.name} ({quantity} шт.)")
        else:
            print(f"Ошибка: недостаточно товара '{product.name}' на складе.")

    def update_quantity(self, product, quantity):
        if product in self.items:
            if quantity <= 0:
                self.remove_item(product)
            elif product.is_available(quantity):
                self.items[product] = quantity
                print(f"Количество '{product.name}' обновлено до {quantity} шт.")
            else:
                print(f"Ошибка: на складе доступно только {product.stock} шт.")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"Товар '{product.name}' удален из корзины.")

    def clear(self):
        self.items.clear()


class Order:
    def __init__(self, customer, items, discount_percent=0, tax_percent=20):
        self.customer = customer
        self.items = items.copy()
        self.discount_percent = discount_percent
        self.tax_percent = tax_percent
        self.total_price = self.calculate_total()

    def calculate_total(self):
        subtotal = sum(product.price * qty for product, qty in self.items.items())
        discount_amount = subtotal * (self.discount_percent / 100)
        price_after_discount = subtotal - discount_amount
        tax_amount = price_after_discount * (self.tax_percent / 100)
        return round(price_after_discount + tax_amount, 2)

    def process_order(self):
        # Проверка наличия и списание со склада
        for product, qty in self.items.items():
            if not product.is_available(qty):
                print(f"Заказ отменен: товара '{product.name}' нет в нужном количестве.")
                return False

        for product, qty in self.items.items():
            product.stock -= qty

        self.customer.order_history.append(self)
        print(f"Заказ успешно оформлен! Итоговая сумма (с учетом скидки и налога): {self.total_price} руб.")
        return True


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
        self.order_history = []

    def checkout(self, discount_percent=0, tax_percent=20):
        if not self.cart.items:
            print("Корзина пуста. Невозможно оформить заказ.")
            return None

        order = Order(self, self.cart.items, discount_percent, tax_percent)
        if order.process_order():
            self.cart.clear()
            return order
        return None


# --- Демонстрация работы магазина ---

# 1. Создаем товары
laptop = Product("Ноутбук", 80000, 5, "Электроника")
mouse = Product("Беспроводная мышь", 2500, 15, "Аксессуары")

# 2. Создаем покупателя и наполняем корзину
user = Customer("Алексей", "alex@example.com")
user.cart.add_item(laptop, 1)
user.cart.add_item(mouse, 2)

# 3. Обновляем количество в корзине
user.cart.update_quantity(mouse, 3)

# 4. Оформляем заказ со скидкой 10% и налогом 20%
user.checkout(discount_percent=10, tax_percent=20)

# 5. Проверяем остаток на складе и историю заказов
print(f"Остаток ноутбуков на складе: {laptop.stock} шт.")
print(f"Количество заказов в истории клиента {user.name}: {len(user.order_history)}")
