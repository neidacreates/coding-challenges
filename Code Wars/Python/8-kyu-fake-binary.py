'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

'''
def fake_bin(x):
    new = ""
    for i in range(len(x)):
        if x[i] < '5':
            new += '0'
        else:
            new += '1'
    return new

# other solution
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)