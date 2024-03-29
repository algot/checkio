def checkio(expression):
    stack = ['']
    brackets = {'(': ')', '[': ']', '{': '}'}

    for e in expression:
        if e in brackets:
            stack.append(brackets[e])
        elif e in brackets.values() and e != stack.pop():
            return False

    return stack == ['']


if __name__ == "__main__":
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
