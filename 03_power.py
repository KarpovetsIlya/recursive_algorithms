# Лабораторная работа 4. Задание 3

def power(x, n):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x


if __name__ == "__main__":
    x = float(input("Введите основание x: "))
    n = int(input("Введите целую степень n: "))
    print(power(x, n))
