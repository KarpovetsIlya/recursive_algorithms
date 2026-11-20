# Лабораторная работа 4. Задание 5

def binary_search(numbers, target):
    def search(left, right):
        if left > right:
            return -1

        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if target < numbers[middle]:
            return search(left, middle - 1)
        return search(middle + 1, right)

    return search(0, len(numbers) - 1)


if __name__ == "__main__":
    numbers = list(map(int, input("Введите отсортированные целые числа: ").split()))
    target = int(input("Введите искомое число: "))
    print(binary_search(numbers, target))
