import tokenize_text
from markov_dictogram import Markov_Dictogram
from dictogram import Dictogram
import sentence


def loop_testing(list_of_words):
    for i in range(0,len(list_of_words)-1):
        print("First Element: {} and Second Element: {}".format(list_of_words[i],list_of_words[i+1]))

def test_markov_model(list_of_words):
    markov_dict = Markov_Dictogram(list_of_words)
    print(markov_dict)

def markov_walk(list_of_words):
    markov_dict = Markov_Dictogram(list_of_words)
    regular_dictogram = Dictogram(list_of_words)
    print(sentence.generate_markov_sentence(regular_dictogram,markov_dict, 10))




if __name__ == "__main__":
    list_of_words = tokenize_text.tokenize_text("fish.txt")
    markov_walk(list_of_words)
