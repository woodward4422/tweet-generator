from dictogram import Dictogram
class Markov_Dictogram(dict):

    def __init__(self,word_list=None):
        super(Markov_Dictogram,self).__init__
        print("word list: {}".format(word_list))
        if word_list is not None:
            length = len(word_list)-1
            print("Length: ", length)

            for i in range(0, length):
                self.add_count(word_list[i],word_list[i+1])

    def add_count(self,word,next_word):
        if word in self:
            if next_word in self[word]:
                self[word][next_word] += 1
            else:
                self[word][next_word] = 1
        else:
            self[word] = {next_word:1}
    
    def frequency(self,first_word,second_word):
        if second_word in self[first_word]:
            return self[first_word][second_word]
        else:
            return 0
        
