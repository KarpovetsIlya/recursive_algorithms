# Лабораторная работа 4. Задание 1

def factorial(n):
    if n < 0:
        raise ValueError("Введите неотрицательное число.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(int(input("Введите n: "))))
