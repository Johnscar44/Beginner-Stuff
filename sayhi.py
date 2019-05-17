def get_word(word_type):
    """get word from the user and return that word"""
if word_type == 'adjective':
    a_or_an = 'an'
else:
    a_or_an = 'an'
return input('return word that is {0} {1}:'.format(a_or_an,word_type))
def fill_in_the_blanks(noun,verb,adjective):
    """fill in the blanks with a noun verb and adjective to make a story"""
    story = "I love eating {0}. But tits and drugs get in the way of {1}. Its just so {2} though.".format(noun,verb,adjective)
    return story
def display_story(story):
    """displays story"""
    print()
    print()
    print("this is my story, enjoy fuck tard")
    print()
def create_story():
    """displays story by caturing the input and creating a story"""
    noun = get_word("noun")
    verb = get_word("verb")
    adjective = get_word("adjective")
the_story = fill_in_the_blanks(noun, verb, adjective)
display_story('the story')
create_story()
