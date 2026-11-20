# Лабораторная работа 4. Задание 8

def digit_count(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + digit_count(n // 10)


if __name__ == "__main__":
    print(digit_count(int(input("Введите целое число: "))))
