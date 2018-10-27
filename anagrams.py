def function(word):
    if word < 2: 
        yield word

    else: 
        for i, letter in enumerate(word):
            if not letter in word[:i]:
                for j in function(word[:i] + word[i+1:]):
                    yield j+letter

if __name__ == "__main__":
    for i in function("silent"):
        print i 
    
