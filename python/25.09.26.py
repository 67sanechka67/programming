#1
temp_C = float(input())
temp_F = round((temp_C *9/5) + 32, 2)
temp_K = round(temp_C + 273.15, 2)
print(temp_F, '°F')
print(temp_K, 'K')
#2
chislo = int(input())
if chislo%2==0: print('Число чётное')
else: print('Число нечётное')
if chislo>0: print('Число положительное')
else: print('Число отрицательное')
if chislo>=10 and chislo<=50: print('Число принадлежит диапозону [10,50]')
else: print('Число не принадлежит диапозону [10,50]')
#3
import random
import string
def generate_password():
    # Генерируем 3 буквы, 3 цифры и 2 спецсимвола
    chars = [
        *(random.choice(string.ascii_uppercase) for _ in range(3)),
        *(random.choice(string.digits) for _ in range(3)),
        *(random.choice("!@#$%^&*") for _ in range(2))
    ]
    random.shuffle(chars)
    return "".join(chars)
print(generate_password())
#4
from collections import Counter
text = input().lower()
print(Counter(text).most_common(3))
#5
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]
print(sieve_of_eratosthenes(int(input())))

