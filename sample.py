import random
import word_count

def weighted_random_word(histogram_dict):
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
# TODO: Add a tested function to test the weighted selection

if __name__ == "__main__":
    print(weighted_random_word(word_count.create_histogram('fish.txt')))

