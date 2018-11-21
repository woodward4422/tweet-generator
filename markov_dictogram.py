from dictogram import Dictogram
class Markov_Dictogram(Dictogram):

    def __init__(self,word_list=None):
        super(Markov_Dictogram,self).__init__
      
        if word_list is not None:
            self.add_count(word_list)
        



    def add_count(self,word_list):
        for i in range(len(word_list) - 1):
            word = word_list[i]
            next_word = word_list[i+1]
            if word in self:
                if next_word in self[word]:
                    self[word][next_word] += 1
                else:
                    self[word][next_word] = 1
            else:
                self[word] = {next_word:1}
    
    def frequency(first_word,second_word):
        if second_word in self[first_word]:
            return self[first_word][second_word]
        else:
            return 0
        
