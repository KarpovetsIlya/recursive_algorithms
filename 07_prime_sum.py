# Лабораторная работа 4. Задание 7

from math import isqrt


def is_prime(n):
    return n >= 2 and all(n % divisor != 0 for divisor in range(2, isqrt(n) + 1))


def prime_sum(n):
    if n < 2:
        raise ValueError("Введите целое число не меньше 2.")
    if is_prime(n):
        return [n]

    # Выбираем наибольшее простое, после которого остаток не меньше 2.
    for prime in range(n - 2, 1, -1):
        if is_prime(prime):
            return [prime] + prime_sum(n - prime)


if __name__ == "__main__":
    n = int(input("Введите целое число не меньше 2: "))
    print(" + ".join(map(str, prime_sum(n))))
