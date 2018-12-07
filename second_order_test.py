import tokenize_text
from second_markov import Second_Markov_Dictogram
import sentence


def second_order_markov_walk():
    tokenized_text = tokenize_text.tokenize_text('gatsby.txt')
    markov_dicto = Second_Markov_Dictogram(tokenized_text)
    return sentence.generate_second_order_markov_sentence(markov_dicto,20)






if __name__ == "__main__":
    print(second_order_markov_walk())

