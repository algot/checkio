from typing import List


def ext_key(file_name):
    name_split = file_name.split('.')
    if('' == name_split[0] and len(name_split) == 2):
        name_split = [''.join(name_split[1:]), '']

    return name_split[::-1]


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=ext_key)


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext(["1.cad", "2.bat", "1.aa", "1.bat"]) == ["1.aa", "1.bat", "2.bat", "1.cad"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
