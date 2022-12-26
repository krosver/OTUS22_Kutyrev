"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers) -> list[int]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int) -> bool:
    for divider in range(num)[:1:-1]:
        if num % divider == 0:
            return False
    return True



def filter_numbers(num_list:list[int], filter_type) -> list[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return [number for number in num_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in num_list if number % 2 == 0]
    if filter_type == PRIME:
        return list(filter(is_prime, num_list))
