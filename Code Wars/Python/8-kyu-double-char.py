# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    doubled_string = ''
    for letter in s:
        doubled_string += letter*2
    return doubled_string