from dictogram import Dictogram
class Second_Markov_Dictogram(dict):

    def __init__(self,word_list=None):
        super(Second_Markov_Dictogram,self).__init__
        if word_list is not None:
            length = len(word_list)-2
            
            for i in range(0, length):
                self.add_count((word_list[i],word_list[i+1]),word_list[i+2])

    def add_count(self,word_tuple,next_word):
        if word_tuple in self:
            if next_word in self[word_tuple]:
                self[word_tuple][next_word] += 1
            else:
                self[word_tuple][next_word] = 1
        else:
            self[word_tuple] = {next_word:1}
    
    def frequency(self,first_word,second_word):
        if second_word in self[first_word]:
            return self[first_word][second_word]
        else:
            return 0