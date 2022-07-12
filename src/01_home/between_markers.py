def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    left_marker = text.find(begin)
    right_marker = text.find(end)

    if left_marker == -1:
        left_marker = 0
    else:
        left_marker += len(begin)

    if right_marker == -1:
        right_marker = len(text)

    return text[left_marker:right_marker]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
