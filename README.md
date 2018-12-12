# Golf Tweet Generator
Using Python, I created a project that users Markov Chains as an intro to NLP to generate sentences based off of a Second Order Markov chain to replicate realistic sentences from the 2019 Rules of Golf Handbook

# Important Files Overview

## tokenize_text.py
This file is responsible for taking in a text file and taking out the junk in the the file, as long as returning all the words in an array that is usable 

## second_markov.py
Class used to encapsulate the functionality of a second order markov chain made by inheriting from dict which will allow me to construct a histogram of a tuple as a key(two words after eachother) and the value being another dictionary containing the third word as a key and the frequency as the value 

## sentence.py
Responsible for taking a markov "walk" to create develop a sentence based off of a passed in Second
_Markov_Dictorgram 

