from flask import Flask 
app = Flask(__name__)
import weighted_random_test 

@app.route('/')
def get_string():
    total_string = ""
    words = weighted_random_test.open_file()
    histo = weighted_random_test.histogram(words)

    for _ in range(6):
        rand_word = weighted_random_test.random_word(histo)
        total_string = total_string + " " +  rand_word
    return total_string
