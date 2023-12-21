# Цього ж разу створи функцію sum_even_numbers і sum_not_even_numbers, які будуть приймати число (num)
# і буде повертати суму всіх парни і непарних чисел відповідно починаючи від 1 до num включно.


def sum_even_numbers (num) -> int:
    sum = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            sum += i
    return sum

def sum_not_even_numbers(num) -> int:
    sum =0
    for i in range(1, num + 1):
        if i % 2 !=0:
            sum +=i
    return sum

