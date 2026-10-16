#1 шифр Цезаря
def detect_language(text):
    """Автоматически определяет язык входного текста."""
    for char in text:
        if 'а' <= char.lower() <= 'я' or char.lower() == 'ё':
            return 'ru'
        if 'a' <= char.lower() <= 'z':
            return 'en'
    return 'en'


def caesar_cipher(text, shift, mode='encrypt'):
    """Шифрует или дешифрует текст шифром Цезаря."""
    if mode == 'decrypt':
        shift = -shift

    lang = detect_language(text)

    if lang == 'ru':
        start_upper, end_upper = ord('А'), ord('Я')
        start_lower, end_lower = ord('а'), ord('я')
        alphabet_size = 32
    else:
        start_upper, end_upper = ord('A'), ord('Z')
        start_lower, end_lower = ord('a'), ord('z')
        alphabet_size = 26

    result = []

    for char in text:
        if start_upper <= ord(char) <= end_upper:
            new_char = chr((ord(char) - start_upper + shift) % alphabet_size + start_upper)
            result.append(new_char)
        elif start_lower <= ord(char) <= end_lower:
            new_char = chr((ord(char) - start_lower + shift) % alphabet_size + start_lower)
            result.append(new_char)
        else:
            result.append(char)

    return "".join(result)


# --- Интерактивный ввод для пользователя ---
if __name__ == "__main__":
    print("--- Программа 'Шифр Цезаря' с автоопределением языка ---")

    while True:
        user_text = input("\nВведите текст (или 'выход' для завершения): ")
        if user_text.lower() in ['выход', 'exit', 'quit']:
            print("Программа завершена. До свидания!")
            break

        # Запрос режима работы с проверкой ввода
        user_mode = input("Выберите режим - шифровать (1) или дешифровать (2): ").strip()
        if user_mode == '1':
            mode = 'encrypt'
        elif user_mode == '2':
            mode = 'decrypt'
        else:
            print("Ошибка: неверный режим. Попробуйте снова.")
            continue

        # Запрос величины сдвига с проверкой на число
        try:
            user_shift = int(input("Введите шаг сдвига (целое число): "))
        except ValueError:
            print("Ошибка: шаг сдвига должен быть целым числом.")
            continue

        # Вычисление и вывод результата
        output_text = caesar_cipher(user_text, user_shift, mode)

        print(f"Результат: {output_text}")
