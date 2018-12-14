import sys

input = sys.argv
input.remove('reverse_word.py')
word = input.pop()
print(word[::-1])