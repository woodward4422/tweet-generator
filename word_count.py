import tokenize
from dictogram import Dictogram
import sys

# module for generating histograms from a list of tokens

def create_histogram(text_file):
    ''' Takes in a raw text file to be tokenized and then will return a dictogram '''
   tokenized_word = tokenize.tokenize_text(text_file)
   return Dictogram(tokenized_word)


if __name__ == "__main__":
    print(create_histogram('fish.txt'))


