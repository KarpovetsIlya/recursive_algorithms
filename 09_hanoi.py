# Лабораторная работа 4. Задание 9

def hanoi(n, source="A", target="C", spare="B"):
    if n < 0:
        raise ValueError("Количество дисков должно быть неотрицательным.")
    if n == 0:
        return

    hanoi(n - 1, source, spare, target)
    print(f"Диск {n}: {source} → {target}")
    hanoi(n - 1, spare, target, source)


if __name__ == "__main__":
    hanoi(int(input("Введите количество дисков: ")))
