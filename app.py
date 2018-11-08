from flask import Flask 
from flask import request
app = Flask(__name__)
import tokenize_text
import word_count
import sentence

@app.route('/')
def get_string():
    # total_words = int(request.args.get('words')) 
    total_string = ""
    token_text = tokenize_text.tokenize_text('fish.txt')
    histo = word_count.create_histogram(token_text)
    return sentence.generate_sentence(histo,10)

# TODO: Add terminal args functionality to run the script
# script = argv[0]
# try:
#     arg1 = argv[1]
# except:
#     arg1 = ''