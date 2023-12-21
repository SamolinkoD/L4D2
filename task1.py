# Цього разу ваша щадача написати функцію get_div_amount, яка буде приймати число (number) i віднімати дільник (divisor),
# А повертати вона повинна к-ть разів, скільки вийшло відняти (divisor) - (number) на дільник без остатку.

# Приклади:
#     get_div_amount(10, 2) -> 5
#     get_div_amount(10, 3) -> 3
#     get_div_amount(1000, 9) -> 111

# Підсказка:
#     1) Ми не знає к-ть ітерацій, тому використовуємо while
#     2) Не забудь про аннотації типів тести їх перевіряють також!!!


def get_div_amount(number: int, divisor: int) -> int:
    amount = 0
    while number >= divisor:
        amount += 1
        number -= divisor
    return amount
