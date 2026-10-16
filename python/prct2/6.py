import random

# Графика для этапов виселицы
STAGES = [
    """
       --------

       |      |
       |
       |
       |
       |
    -------
    """,
    """
       --------

       |      |
       |      O
       |
       |
       |
    -------
    """,
    """
       --------

       |      |
       |      O

       |      |
       |
       |
    -------
    """,
    """
       --------

       |      |
       |      O

       |     /|
       |
       |
    -------
    """,
    """
       --------

       |      |
       |      O

       |     /|\\
       |
       |
    -------
    """,
    """
       --------

       |      |
       |      O

       |     /|\\
       |     /
       |
    -------
    """,
    """
       --------

       |      |
       |      O

       |     /|\\
       |     / \\
       |
    -------
    """
]

# Список слов для угадывания
WORDS_POOL = ["ПРОГРАММА", "КОМПЬЮТЕР", "АЛГОРИТМ", "ФУНКЦИЯ", "ПЕРЕМЕННАЯ", "ИНТЕРНЕТ", "СКРИПТ"]


def play_hangman():
    word = random.choice(WORDS_POOL)
    guessed_letters = set()  # Правильно угаданные буквы
    wrong_letters = set()  # Ошибочные буквы
    max_errors = len(STAGES) - 1
    errors = 0

    print("=== Добро пожаловать в игру 'Виселица'! ===")

    while errors < max_errors:
        # Формируем строку с угаданными буквами и пропусками
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(f"\nСлово: {' '.join(word_display)}")
        print(STAGES[errors])
        print(f"Ошибочные буквы: {', '.join(sorted(wrong_letters))}")

        # Проверка на победу
        if "_" not in word_display:
            print(f"🎉 Поздравляем! Вы выиграли! Загаданное слово: {word}")
            break

        # Ввод буквы пользователем
        guess = input("Введите одну русскую букву: ").upper().strip()

        # Валидация ввода
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Ошибка: нужно ввести ровно одну букву.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("⚠️ Вы уже вводили эту букву.")
            continue

        # Проверка наличия буквы в слове
        if guess in word:
            print(f"✅ Отлично! Буква '{guess}' есть в слове.")
            guessed_letters.add(guess)
        else:
            print(f"❌ Увы, буквы '{guess}' нет в слове.")
            wrong_letters.add(guess)
            errors += 1
    else:
        print(STAGES[errors])
        print(f"💥 Игра окончена! Вы проиграли. Загаданное слово было: {word}")


if __name__ == "__main__":
    play_hangman()
