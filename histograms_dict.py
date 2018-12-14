
# This Script will take in a book of text and will analyze the text to create a histogram for the frequency of the words in the list
import random
histogram_dict = {}

# Takes in text and will return a histogram(dictionary) of word frequency that will follow the form "word":frequency
def histogram(source_text):
    for word in source_text:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
    
    return histogram_dict

#Takes in a histogram and will return the total count of unique words in the histogram
def unique_words(histogram_dict):
    return len(histogram_dict)

# Takes in a word and a histogram and returns the number of times that the word appears in the text
def frequency(word,histogram_dict):
    if histogram_dict[word]:
        return histogram_dict[word]
    else:
        print("That is not a word in the histogram")

def random_word(histogram_dict):
    ''' Takes in a Dictionary in the format of a histogram and returns a key based off a weighted sampling '''
    #Create an accumulator value to be a running total 
    accumulator = 0 
    # Gets a uniform random number between 0 and the sum total of all the frequencies
    rand_sum = random.randint(0,sum(histogram_dict.values()))
    #The iteritems() method will give me a iterator over 
    for key, value in histogram_dict.iteritems():
        accumulator += value
        if accumulator >= rand_sum:
            return key
        else: 
            continue
    









if __name__ == "__main__":
    with open('fish.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    histo = histogram(words)
    print(histo)
    print("Unique Words: {}".format(unique_words(histo)))
    freq_word = "fish"
    print("Frequency of {} in the histogram is: {}".format(freq_word,frequency(freq_word,histo)))
    random_selected_word = random_word(histo)
    print("Random Word: {}".format(random_selected_word))



    
