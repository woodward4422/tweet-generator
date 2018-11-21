from flask import Flask 
from flask import request
app = Flask(__name__)
import tokenize_text 
import word_count
import sentence
import tester


@app.route('/')
def get_string():
    ''' Route will generate a sentence of 10 random words based from the fish.txt corpus '''
    # total_words = int(request.args.get('words'))
    token_text = tokenize_text.tokenize_text('gatsby.txt')
    histo = word_count.create_histogram(token_text)
    markov_histo = word_count.create_markov_histogram(tokenize_text)
    return sentence.generate_markov_sentence(histo,markov_histo,10)