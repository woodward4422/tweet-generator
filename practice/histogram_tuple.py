# This Script will take in a book of text and will analyze the text to create a histogram for the frequency of the words in the list
histogram_tup = []

# Takes in text and will return a histogram(dictionary) of word frequency that will follow the form "word":frequency
def histogram(source_text):
    for word in source_text:
        frequency = source_text.count(word)
        histogram_tup.append((word,frequency))
        remove_dup = set(histogram_tup)
    return list(remove_dup)

        

#Takes in a histogram and will return the total count of unique words in the histogram
def unique_words(histogram_tuple):
    return len(histogram_tuple)

# Takes in a word and a histogram and returns the number of times that the word appears in the text
def frequency(word,histogram_tuple):

    if word in dict(histogram_tuple):
        dict_tuple = dict(histogram_tup)
        return dict_tuple[word]
    else:
        print("That is not a word in the histogram")

if __name__ == "__main__":
    with open('book.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    histo_tuple = histogram(words)
    print(histo_tuple)
    print("Unique Words: {}".format(unique_words(histo_tuple)))
    freq_word = "the"
    print("Frequency of {} in the histogram is: {}".format(freq_word,frequency(freq_word,histo_tuple)))



