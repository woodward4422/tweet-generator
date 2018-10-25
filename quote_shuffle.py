import sys
import random

userInput = raw_input("Enter some words!:")
words_list = userInput.split()
result = []
while len(words_list) is not 0: 
    i = random.randrange(len(words_list))
    words_list[i], words_list[-1] = words_list[-1], words_list[i]
    rand_word = words_list.pop()
    result.append(rand_word)
print( " ".join(result))



