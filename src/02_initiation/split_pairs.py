def split_pairs(a: str) -> list:
    odds = []
    evens = []

    for i in range(len(a)):
        item = a[i]
        if i % 2 == 1:
            evens.append(item)
        else:
            odds.append(item)

    if len(odds) == len(evens):
        result = []
        for i in range(len(odds)):
            result.append(odds[i] + evens[i])
        return result
    else:
        result = []
        for i in range(len(evens)):
            result.append(odds[i] + evens[i])
        result.append(odds[-1] + '_')
        return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
