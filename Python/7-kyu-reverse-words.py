"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"""

def reverse_words(text):
    words_list = text.split(" ")
    reverse_words = []
    for word in words_list: 
        reverse_word = word[::-1]
        reverse_words.append(reverse_word)
    reverse_sentence = " ".join(reverse_words)
    return reverse_sentence
    
# other solutions
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words(str):
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)
