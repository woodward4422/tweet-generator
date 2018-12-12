# Golf Tweet Generator
Using Python, I created a project that users Markov Chains as an intro to NLP to generate sentences based off of a Second Order Markov chain to replicate realistic sentences from the 2019 Rules of Golf Handbook.

# Important Files Overview

## app.py
This is where all the flask routes are handled.

## tokenize_text.py
This file is responsible for taking in a text file and taking out the junk in the the file, as long as returning all the words in an array that is usable.

## second_markov.py
Class used to encapsulate the functionality of a second order markov chain made by inheriting from dict which will allow me to construct a histogram of a tuple as a key(two words after eachother) and the value being another dictionary containing the third word as a key and the frequency as the value.

## sentence.py
Responsible for taking a markov "walk" to create develop a sentence based off of a passed in Second
_Markov_Dictorgram, length of sentence is hardcoded until I have added stop tokens logic to the generate_second_order_markov_sentence function.

## linkedlist.py
This was a mandatory Linked List data structure implementation, not related to my tweet generator, but used as an introduction to algorithm analysis and data structures 

## hashtable.py
This was a mandatory Hash Table data structure implementation, not related to my tweet generator, but used as an introduction to algorithm analysis and data structures 

## game_of_golf.txt
Used as my corpus to be tokenized and then passed into my Second_Markov_Dictogram to create the markov model which will generate a realistic sentence about the rules of golf

## All the rest 
Most of the files are just testing files created while we were learning different topics in my CS 1.2 Intro to Data Structures course. I hope to refactor the code in the next few weeks once this assigment gets graded in order to improve the readability of the code base 


