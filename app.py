from flask import Flask 
from flask import request
app = Flask(__name__)
import weighted_random_test 

@app.route('/')
def get_string():
    total_words = int(request.args.get('words')) 
    total_string = ""
    words = weighted_random_test.open_file()
    histo = weighted_random_test.histogram(words)

    for _ in range(total_words):
        rand_word = weighted_random_test.random_word(histo)
        total_string = total_string + " " +  rand_word
    return total_string

# TODO: Add terminal args functionality to run the script
# script = argv[0]
# try:
#     arg1 = argv[1]
# except:
#     arg1 = ''