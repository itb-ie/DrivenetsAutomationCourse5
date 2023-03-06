def factorial(n: int) -> int:
    """
    This function calculate n!
    :param n: the factorial value
    :return:
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == "__main__":  # this is True if I run it directly, False otherwise
    # this is my private code, will not be seen by ppl importing!
    print("lets do some tests")
    print(factorial(3))
    print(factorial(4))
    print(factorial(10))
