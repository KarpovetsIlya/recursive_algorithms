# Лабораторная работа 4. Задание 4

def is_palindrome(text):
    def check(left, right):
        if left >= right:
            return True
        return text[left] == text[right] and check(left + 1, right - 1)

    return check(0, len(text) - 1)


if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Палиндром" if is_palindrome(text) else "Не палиндром")
