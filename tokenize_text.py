# Module for cleaning up and creating corpus text and also tokenizing the text to be returned as a list
import re
import string

def tokenize_text(text_file):
    ''' Takes in raw text from a text file and will return a split()(list) of all the words in the text file '''
    try:
        with open(text_file, 'r') as myfile:
            # cleaned_text = re.sub('[^a-zA-Z\s]*$','',myfile.read())
            # return cleaned_text.replace('\n', '').lower().split()
            cleaned_text = myfile.read().translate(string.punctuation)
            cleaner_text = re.sub('[^a-zA-Z\s]*$','',cleaned_text)
            white_list = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            cleanest_text = ''.join(filter(white_list.__contains__,cleaner_text))
            return cleanest_text.lower().split()
    except IOError:
        raise Exception('Could not open file, should be in proper .txt format')



if __name__ == "__main__":
    print(tokenize_text('game_of_golf.txt'))


    

