# Лабораторная работа 4. Задание 6

def reverse_words(text):
    words = text.split()

    def reverse(left, right):
        if left >= right:
            return
        words[left], words[right] = words[right], words[left]
        reverse(left + 1, right - 1)

    reverse(0, len(words) - 1)
    return " ".join(words)


if __name__ == "__main__":
    print(reverse_words(input("Введите строку: ")))
