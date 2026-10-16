import random
import string

print("-" * 40 + "\n   ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ\n" + "-" * 40)

# 1. Запрос параметров одной строкой для экономии места
length = int(input("Длина пароля: ") or 8)
use_lower = input("Нижний регистр? (y/n): ").lower() != "n"
use_upper = input("Верхний регистр? (y/n): ").lower() != "n"
use_digits = input("Цифры? (y/n): ").lower() != "n"
use_spec = input("Спецсимволы? (y/n): ").lower() != "n"

# 2. Формирование пула символов
pool = ""
if use_lower:
    pool += string.ascii_lowercase
if use_upper:
    pool += string.ascii_uppercase
if use_digits:
    pool += string.digits
if use_spec:
    pool += string.punctuation

# 3. Генерация и вывод
if pool:
    password = "".join(random.choice(pool) for _ in range(length))
    print(f"\n Сгенерированный пароль: \033[1;32m{password}\033[0m\n" + "-" * 40)
else:
    print("\n Ошибка: Вы не выбрали ни один тип символов!")