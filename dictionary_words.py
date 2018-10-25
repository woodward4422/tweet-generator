import sys
import random

number_of_words = sys.argv[1]
print(number_of_words)

unshuffled_sentence = [] 

# file = open('/usr/share/dict/words','r')
# def select_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile):
#         if random.randrange(num + 2): continue
#         line = aline
#     return line

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


while len(unshuffled_sentence) != int(number_of_words):
    new_line = random_line('/usr/share/dict/words')
    unshuffled_sentence.append(new_line)
    
shuffled = random.sample(unshuffled_sentence,len(unshuffled_sentence))
print(" ".join(map(lambda s: s.strip(),shuffled)))



        



    





    
    



    

