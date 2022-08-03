def checkio(number: int) -> int:
    str_number = str(number)
    list_number = list(str_number)

    m = 1
    for x in list_number:
        if x != '0':
            m *= int(x)

    return m


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
