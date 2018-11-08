import sys
# Module that takes in an argv variable and will try and access it and if there isnt an argument than default to fish.txt
def get_file(argv_input):
    ''' Takes in the terminal arguments and it will default to fish.txt if user forgot to input a textfile ''' 
    try:
        argv_input[1]
    except:
        return 'fish.txt'
    return argv_input[1]
    
