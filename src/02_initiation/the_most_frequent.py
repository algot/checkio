def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    max_count = 0
    result = ''
    for char in data:
        if data.count(char) > max_count:
            max_count = data.count(char)
            result = char

    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
