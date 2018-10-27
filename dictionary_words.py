import sys
import random
# Number of words the user wants 
number_of_words = sys.argv[1]
unshuffled_sentence = []
lines = open('/usr/share/dict/words').read().splitlines()

# file = open('/usr/share/dict/words','r')
# def select_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile):
#         if random.randrange(num + 2): continue
#         line = aline
#     return line

# Get a random line by opening the file and then using splitlines() to put it into an array, then get a random element from the array
def random_word(all_lines):
    return random.choice(lines)


# Gets a new word and appends it until 
while len(unshuffled_sentence) != int(number_of_words):
    new_word = random_word(lines)
    unshuffled_sentence.append(new_word)

print(" ".join(unshuffled_sentence))



        



    





    
    



    

