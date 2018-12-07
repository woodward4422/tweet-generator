import tokenize_text
import sample
import random
from second_markov import Second_Markov_Dictogram
import sentence

def create_sentence(text_file,amount_of_words):
    ''' Takes in a markov histogram and will give you a sentence ''' 

    tokenized_words = tokenize_text.tokenize_text('gatsby.txt')
    second_order_markov = Second_Markov_Dictogram(tokenized_words)
    return sentence.generate_second_order_markov_sentence(second_order_markov,10)


if __name__ == "__main__":
    print(create_sentence('gatsby.txt',10))



