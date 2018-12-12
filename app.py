from flask import Flask, render_template
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

@app.route('/')
def get_string():
    ''' Route will generate a sentence created with a markov chain and analyzed from the rules of golf handbook '''
    with app.app_context(), app.test_request_context():
        tokenized_words = tokenize_text.tokenize_text('game_of_golf.txt')
        second_order_markov = Second_Markov_Dictogram(tokenized_words)
        final_sentence = sentence.generate_second_order_markov_sentence(second_order_markov,12)
        return render_template("main.html",sentence=final_sentence)

    

get_string()

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
    