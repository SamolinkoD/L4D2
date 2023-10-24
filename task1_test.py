import typing
from task1 import get_div_amount


def test_get_div_amount_annotation_types():
    annotations = typing.get_type_hints(get_div_amount)

    expected_annotations = {"number": int, "divisor": int, "return": int}

    if annotations != expected_annotations:
        return f"Type annotations are incorrect. Expected: {expected_annotations}, Actual: {annotations}"

    return "Type annotations for 'get_div_amount' function are correct."


def test_get_div_amount_values():
    test_cases = {
        5: [10, 2],
        3: [10, 3],
        111: [1000, 9],
        6: [24, 4],
        2: [10, 4],
    }

    results = []

    for key, value in test_cases.items():
        try:
            result = get_div_amount(value[0], value[1])
            if result != key:
                results.append(
                    f"Test case {value}: Expected result: {key}, Actual result: {result}"
                )
        except Exception as e:
            results.append(f"Test case {value}: Error - {str(e)}")

    if not results:
        return "All test cases passed."
    else:
        return "\n".join(results)


result1 = test_get_div_amount_annotation_types()
result2 = test_get_div_amount_values()

print(result1)
print(result2)
