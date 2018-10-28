# This Script will take in a book of text and will analyze the text to create a histogram for the frequency of the words in the list
histogram_dict = {}

# Takes in text and will return a histogram(dictionary) of word frequency that will follow the form "word":frequency
def histogram(source_text):
    for word in source_text:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
    return histogram_dict

#Takes in a histogram and will return the total count of unique words in the histogram
def unique_words(histogram_dict):
    return len(histogram_dict)

# Takes in a word and a histogram and returns the number of times that the word appears in the text
def frequency(word,histogram_dict):
    if histogram_dict[word]:
        return histogram_dict[word]
    else:
        print("That is not a word in the histogram")








if __name__ == "__main__":
    with open('book.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    histo = histogram(words)
    print(histo)
    print("Unique Words: {}".format(unique_words(histo)))
    freq_word = "the"
    print("Frequency of {} in the histogram is: {}".format(freq_word,frequency(freq_word,histo)))



    
