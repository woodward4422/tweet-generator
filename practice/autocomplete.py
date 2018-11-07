# This is a script with inputs being a first letter in the word and will output a list of all possible words that could be made from that first letter 
lines = open('/usr/share/dict/words').read().splitlines()
possible_words = []

# Takes in a letter and returns a list of all possible words that start with that letter
def auto_complete(letter,list_of_words):
    for word in list_of_words:
        if word[0].lower() == letter:
            possible_words.append(word)
    return possible_words




if __name__ == "__main__":
    print(auto_complete("b",lines))

