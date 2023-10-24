import typing

from task2 import sum_even_numbers, sum_not_even_numbers


def test_even_func_annotations():
    annotations = typing.get_type_hints(sum_even_numbers)

    expected_annotations = {"num": int, "return": int}

    if annotations != expected_annotations:
        return f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"

    return "Type annotations for 'sum_even_numbers' function are correct."


def test_not_even_func_annotations():
    annotations = typing.get_type_hints(sum_not_even_numbers)

    expected_annotations = {"num": int, "return": int}

    if annotations != expected_annotations:
        return f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"

    return "Type annotations for 'sum_not_even_numbers' function are correct."


def test_even_func():
    test_cases = {30: 10, 240: 30, 250500: 1000, 10714024813212: 6546457}

    results = []

    for key, value in test_cases.items():
        try:
            result = sum_even_numbers(value)
            if result != key:
                results.append(
                    f"Test case {value}: Expected result: {key}, Actual result: {result}"
                )
        except Exception as e:
            return f"Test case {key}: Error - {str(e)}"

    if results:
        print(results)
        return "\n".join(results)

    return "All test cases passed."


def test_not_even_func():
    test_cases = {25: 10, 225: 30, 250000: 1000, 10714028086441: 6546457}

    results = []

    for key, value in test_cases.items():
        try:
            result = sum_not_even_numbers(value)
            if result != key:
                results.append(
                    f"Test case {value}: Expected result: {key}, Actual result: {result}"
                )
        except Exception as e:
            return f"Test case {key}: Error - {str(e)}"

    if results:
        print(results)
        return "\n".join(results)

    return "All test cases passed."


result1 = test_even_func_annotations()
result2 = test_not_even_func_annotations()
result3 = test_even_func()
result4 = test_not_even_func()


print(result1)
print(result2)
print(result3)
print(result4)
