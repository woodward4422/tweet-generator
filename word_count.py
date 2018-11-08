
from dictogram import Dictogram
import sys

# module for generating histograms from a list of tokens

def create_histogram(tokenized_words):
   ''' Takes in a tokenized list of the text and then will return a dictogram object '''
   return Dictogram(tokenized_words)


if __name__ == "__main__":
    print(create_histogram('fish.txt'))


