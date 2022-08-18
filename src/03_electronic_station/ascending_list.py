from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    if len(items) < 2:
        return True
    elif items.count(items[0]) == len(items):
        return False
    else:
        return items == sorted(items)


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
