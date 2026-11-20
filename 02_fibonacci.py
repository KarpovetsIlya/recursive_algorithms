# Лабораторная работа 4. Задание 2

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        raise ValueError("Введите неотрицательный индекс.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(input("Введите индекс n (начиная с 0): "))))
