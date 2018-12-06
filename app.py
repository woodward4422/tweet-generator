from flask import Flask 
from flask import request
import tokenize_text 
import word_count
import sentence
import tester
from markov_dictogram import Markov_Dictogram
from dictogram import Dictogram


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def get_string():
    ''' Route will generate a sentence of 10 random words based from the fish.txt corpus '''
    # total_words = int(request.args.get('words'))
    # token_text = tokenize_text.tokenize_text('fish.txt')
    # dicty = word_count.create_histogram(tokenize_text)
    # return sentence.generate_sentence(dicty,10)
    tokenized_words = tokenize_text.tokenize_text('gatsby.txt')
    markov_dict = Markov_Dictogram(tokenized_words)
    regular_dictogram = Dictogram(tokenized_words)
    return sentence.generate_markov_sentence(regular_dictogram,markov_dict, 10)

    

get_string()

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
    