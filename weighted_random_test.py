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

def random_word(histogram_dict):
    ''' Takes in a Dictionary in the format of a histogram and returns a random key '''
    #Create an accumulator value to be a running total 
    accumulator = 0 
    # Gets a uniform random number between 0 and the sum total of all the frequencies
    rand_sum = random.randint(0,sum(histogram_dict.values()))
    #The iteritems() method will give me a interator over 
    for key, value in histogram_dict.iteritems():
        accumulator += value
        if accumulator >= rand_sum:
            return key
        else: 
            continue

    

    


if __name__ == "__main__":
    with open('wordtest.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    histo = histogram(words)
    print(random_word(histo))


    
