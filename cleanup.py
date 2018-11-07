def cleanup_text(raw_text):
    ''' Takes in raw text from a text file and will return a split()(list) of all the words in the text file '''
    try:
        with open(raw_text, 'r') as myfile:
            return myfile.read().replace('\n', '').lower().split()
    except IOError:
        raise Exception('Could not open file, should be in proper .txt format')

if __name__ == "__main__":
    print(cleanup_text("fish.txt"))
    print(cleanup_text("fishyyyy"))
    

