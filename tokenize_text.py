# Module for cleaning up and creating corpus text and also tokenizing the text to be returned as a list

def tokenize_text(text_file):
    ''' Takes in raw text from a text file and will return a split()(list) of all the words in the text file '''
    try:
        with open(text_file, 'r') as myfile:
            return myfile.read().replace('\n', '').lower().split()
    except IOError:
        raise Exception('Could not open file, should be in proper .txt format')



if __name__ == "__main__":
    print(tokenize_text("fish.txt"))
    print(tokenize_text("fishyyyy"))
    

