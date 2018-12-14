import random 


# Takes in text and will return a histogram(dictionary) of word frequency that will follow the form "word":frequency
def histogram(source_text):
    histogram_dict = {}
    for word in source_text:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
    
    return histogram_dict

def random_word(histogram_dict):
    ''' Takes in a Dictionary in the format of a histogram and returns a random key '''
    #Create an accumulator value to be a running total 
    accumulator = 0 
    # Gets a uniform random number between 0 and the sum total of all the frequencies
    sum_dict = sum(histogram_dict.values())
    rand_sum = random.randint(0,sum_dict - 1)
    #The items() method will give me a interator over the dictionary 
    for key, value in histogram_dict.items():
        accumulator += value
        if accumulator > rand_sum:
            return key
        else: 
            continue
            
def random_test(histogram_dict):
    test_dict = {}
    for _ in range(0,10000):
        word_selected = random_word(histogram_dict)
        if word_selected in test_dict:
            test_dict[word_selected] += 1
        else:
            test_dict[word_selected] = 1
    return test_dict

def open_file():
    '''This will open and then return the file '''
    with open('fish.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    return words

    

    


if __name__ == "__main__":
    words = open_file()
    histo = histogram(words)
    print(histo)
    print(random_word(histo))
    print(random_test(histo))


    
