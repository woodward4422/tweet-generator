# This Script will take in a book of text and will analyze the text to create a histogram for the frequency of the words in the list
histogram_list = []

# Takes in text and will return a histogram(list) of word frequency that will follow the form [[word,frequency]]
def histogram(source_text):
    for word in source_text:
        frequency = source_text.count(word)
        histogram_list.append([word,frequency])
        print(histogram_list)
    for i in range(len(histogram_list) -1):
        for j in range(i+1,len(histogram_list) - 1):
            try:
                if histogram_list[i] == histogram_list[j]:
                    histogram_list[j], histogram_list[-1] = histogram_list[-1], histogram_list[j]
                    histogram_list.pop()
            except IndexError:
                break
    return histogram_list

        

#Takes in a histogram and will return the total count of unique words in the histogram
def unique_words(histogram_list):
    return len(histogram_list)

# Takes in a word and a histogram and returns the number of times that the word appears in the text
def frequency(word,histogram_list):

    for element in histogram_list:
        if element[0] == word:
            return element[1]
        else:
            print("This word is not in the text")
    


        
    else:
        print("That is not a word in the histogram")

if __name__ == "__main__":
    with open('book.txt', 'r') as myfile:
        words = myfile.read().replace('\n', '').lower().split()
    histo_list = histogram(words)
    print(histo_list)
    print("Unique Words: {}".format(unique_words(histo_list)))
    freq_word = "the"
    print("Frequency of {} in the histogram is: {}".format(freq_word,frequency(freq_word,histo_list)))