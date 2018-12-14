import random
import word_count

def weighted_random_word(histogram_dict):
    ''' Takes in a Dictionary in the format of a histogram and returns a random key '''
    # Raise an exception if we are given an empty histogram
    if len(histogram_dict) == 0:
        raise Exception("Attempted to random sample from an empty histogram")
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


def weighted_random_test():
    ''' Tests to make sure that the weighted random sampling is correct ''' 
    histogram = word_count.create_histogram('fish.txt')
    for _ in range(0,10000):
        result_dict = {}
        word_selected = weighted_random_word(histogram)
        print(word_selected)
        if word_selected in result_dict:
            result_dict[word_selected] += 1
        else:
            result_dict[word_selected] = 1
    print(result_dict)
    return result_dict

if __name__ == "__main__":
    print(weighted_random_word(word_count.create_histogram('fish.txt')))
    weighted_random_test()

