import tokenize_text
import sample

def create_sentence(markov_histogram,amount_of_words):
    ''' Takes in a markov histogram and will give you a sentence ''' 
    stop_words = stop_words(markov_dictogram)
    word_list = []
    if len(markov_histogram) == 0:
        raise Exception("Attempted to make a sentence with no words given")
    word = random.choice(stop_words)
    while word in stop_words:
        word = random.choice(stop_words)
    if len(word_list) <= amount_of_words:
        while word not in stop_words:
            word_list.append(word[1])
            word = (word[1],)



# word_list = []
#     if len(markov_histogram) == 0:
#         raise Exception("Attempted to make a sentence with no words given")
#     word = random.choice(markov_histogram.keys())
#     while len(word_list) is not amount_of_words:
#         word_list.append(word[1])
#         word = (word[1],sample.weighted_random_word(markov_histogram[word]))
#     return " ".join(word_list) + "."

def stop_words(markov_dictogram):
    ''' Used to find the words that can end the sentence '''
    stop_words = []
    for key, value in markov_dictogram.items:
        if key[2].endsWith(".") or key[2].endsWith("?"):
            stop_words.append(key)
    return stop_words

def main_script(source_file):
    tokenized_text = 

