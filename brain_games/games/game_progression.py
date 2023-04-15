import random


ABOUT = 'What number is missing in the progression?'


def choice_game():
    numbers = []
    num_start = random.randint(1, 100)  # начальное число
    numbers.append(num_start)
    n = random.randint(5, 10)  # длина списка
    n_step = random.randint(1, 10)  # шаг арифм. прог-ии
    numbers.append(num_start + n_step)
    for i in range(1, n):
        num = numbers[-1] + n_step
        numbers.append(num)
    numbers.sort()  # сортировка списка
    # индекс выбранного случайного элемента
    true_answer_index = random.randint(0, len(numbers) - 1)
    # получаем значение элемента выбранного индекса
    true_answer = str(numbers[true_answer_index])
    # элементс выбранным индексом заменяем нужным символом
    numbers[true_answer_index] = ".."
    # переводим список в строку с разделителем ", "
    str_numbers = (', '.join(map(str, numbers)))
    return str_numbers, str(true_answer)  # возвращаю в виде строки
    # так как, при вводе своего ответа,данные вводятся в виде str()


""" Данный код определяет функцию "choice_game()",
которая генерирует список случайных чисел. Сначала она использует функцию
"random.randint()" из модуля "random", чтобы выбрать случайное целое
число от 1 до 10 и присвоить его переменной "num1".
Она также выбирает другое случайное целое число от 80 до 100 и
присваивает его переменной "num2". Затем она создает третью переменную
"n" с помощью функции "random.randint()" и выбирает случайное целое
число в диапазоне от 2 до 10. Далее функция создает пустой список
"numbers" и заполняет его числами, начиная от "num1" до "num2" с
шагом "n" с помощью цикла "for". Наконец, она сортирует "numbers"
в порядке возрастания с помощью метода "sort()".
В конце функция завершается без вывода чего-либо."""

# print(choice_game())
