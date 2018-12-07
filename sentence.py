import sample
import word_count
import tokenize_text
import sentence
import random
# Module that at first will be creating sentences without the use of Markov models, but a Markov model will be implmeneted next week

def generate_sentence(histogram,amount_of_words):
    ''' Takes in a histogram and the amount of words needed to be generated and returns a sentence(Pre Markov chain model) ''' 
    # word_list = []
    # for _ in range(amount_of_words):
    #     word_list.append(sample.weighted_random_word(histogram))
    # if len(word_list) == 0:
    #     raise Exception("Attempted to make a sentence with no words given")
    # return " ".join(word_list)
    token_text = tokenize_text.tokenize_text('fish.txt')
    print(token_text)
    dicty = word_count.create_histogram(tokenize_text)
    return sentence.generate_sentence(dicty,10)

def generate_markov_sentence(word_histogram,markov_histogram,amount_of_words):
    word_list = []
    if len(word_histogram) == 0:
        raise Exception("Attempted to make a sentence with no words given")
    word = sample.weighted_random_word(word_histogram)
        

    while len(word_list) is not amount_of_words:
        word_list.append(word)
        word = sample.weighted_random_word(markov_histogram[word])
    return " ".join(word_list)

def generate_second_order_markov_sentence(markov_histogram,amount_of_words):
    word_list = []
    if len(markov_histogram) == 0:
        raise Exception("Attempted to make a sentence with no words given")
    word = random.choice(markov_histogram.keys())
    while len(word_list) is not amount_of_words:
        word_list.append(word[1])
        word = (word[1],sample.weighted_random_word(markov_histogram[word]))
    return " ".join(word_list)

    
    






if __name__ == "__main__":
    print(generate_sentence(word_count.create_histogram('fish.txt'),5))



