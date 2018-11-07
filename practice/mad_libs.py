# This is the MadLibs project created by Noah Woodward 
import random 

inital_story = ["There once was a (Noun) at (Noun), who loved to (Verb) and would always (Verb).", "At Make School, it is said that you can see a (Noun) and a (Noun), and can be seen (Verb), but they are also know to be (Verb)"]
def get_Initial_Story():
    return random.choice(inital_story)

def display_first_story(story): 
    print(story)

def get_input(story_selected): 
     first_noun = raw_input("Give me a noun:")
     second_noun = raw_input("Give me another noun:")
     first_verb = raw_input("Give me a verb:")
     second_verb = raw_input("Give me another verb:")
     show_message(story_selected,first_noun,second_noun,first_verb,second_verb)
    
def show_message(selected_story,first_noun,second_noun,first_verb,second_verb):
    story_index = inital_story.index(selected_story)
    new_story = ["There once was a " + first_noun + " at " + second_noun + " who loved to " + first_verb + " and would always " + second_verb, "At Make School, it is said that you can see a " + first_noun + " and a " + second_noun + ", and can be seen " + first_verb + ", but they are also known to be " + second_verb]
    print(new_story[story_index])

    

    






def test():
 story = get_Initial_Story()
 display_first_story(story)
 get_input(story)


test()

