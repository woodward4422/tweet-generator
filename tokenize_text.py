# Module for cleaning up and creating corpus text and also tokenizing the text to be returned as a list
import re

def tokenize_text(text_file):
    ''' Takes in raw text from a text file and will return a split()(list) of all the words in the text file '''
    try:
        with open(text_file, 'r') as myfile:
            cleaned_text = re.sub(("[a-zA-Z]",'',myfile)
            return cleaned_text.replace('\n', '').lower().split()
    except IOError:
        raise Exception('Could not open file, should be in proper .txt format')



if __name__ == "__main__":
    tokenize_text('game_of_golf.txt')


    

