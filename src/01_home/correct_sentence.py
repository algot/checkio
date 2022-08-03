from curses.ascii import islower


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    if text[0].islower():
        text = text.replace(text[0], text[0].upper(), 1)
    if not text.endswith('.'):
        text += '.'

    return text


print('Example:')
# print(correct_sentence("greetings, friends"))

# assert correct_sentence('greetings, friends') == 'Greetings, friends.'
# assert correct_sentence('Greetings, friends') == 'Greetings, friends.'
# assert correct_sentence('Greetings, friends.') == 'Greetings, friends.'
# assert correct_sentence('greetings, friends.') == 'Greetings, friends.'
assert correct_sentence('welcome to New York') == 'Welcome to New York.'

print("The mission is done! Click 'Check Solution' to earn rewards!")
