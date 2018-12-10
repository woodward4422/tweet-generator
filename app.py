from flask import Flask 
from flask import request
import tokenize_text 
import word_count
import sentence
import tester
from markov_dictogram import Markov_Dictogram
from dictogram import Dictogram
from second_markov import Second_Markov_Dictogram


app = Flask(__name__)
app.config['DEBUG'] = True

# Comment
@app.route('/')
def get_string():
    ''' Route will generate a sentence of 10 random words based from the fish.txt corpus '''
    # total_words = int(request.args.get('words'))
    # token_text = tokenize_text.tokenize_text('fish.txt')
    # dicty = word_count.create_histogram(tokenize_text)
    # return sentence.generate_sentence(dicty,10)
    tokenized_words = tokenize_text.tokenize_text('game_of_golf.txt')
    second_order_markov = Second_Markov_Dictogram(tokenized_words)
    return sentence.generate_second_order_markov_sentence(second_order_markov,12)

    

get_string()

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
    