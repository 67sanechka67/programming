#2 олимпиада
def check_winners(all_scores, student_score):
    """Определяет, вошел ли студент в тройку лидеров, и выводит результат."""
    sorted_scores = sorted(all_scores, reverse=True)
    top_three = sorted_scores[:3]
    if student_score in top_three:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")
user_input = input("Введите все баллы участников через пробел: ")
all_scores = [int(x) for x in user_input.split()]
student_score = int(input("Введите свой балл: "))
check_winners(all_scores, student_score)