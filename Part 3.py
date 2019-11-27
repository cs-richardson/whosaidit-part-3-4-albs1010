import math

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

#This function counts the amount of words and its repetition, and outputs it.

def get_counts(document):
    count = 0
    stored_words = {}
    every_word = []
    input_file = open(document)

#This loop stores the text in a variable
    
    text = ""
    for line in input_file:
        text = text + line + "\n"

    every_word = text.split()
    

#This loop, adds everything into a dictionary with the amount of that word repeated. It also counts the amount of words


    for word in every_word:
        word = normalize(word)
        if word != "":
            
            if word in stored_words:
                stored_words[word] = stored_words[word] + 1
                count = count + 1
            else:
                stored_words[word] = 1
                count = count +1
            

    stored_words["_total"] = count

    return stored_words

    input_file.close()

'''This function takes a word and a dictionary of word counts, and it generates
a score that approximates the relevance of the word in the document from
which the word counts were generated.
'''

def get_score(word, counts):
    
    denominator = float(1 + counts["_total"])
    
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    
    else:
        return math.log(1 / denominator)
'''
This function uses the given text and iterates through each element and
uses the get_score function to get a score and adds it to the total.
'''

def adding_scores(text, author, dictionary):

    author = 0

    for word in text:
        if word != "":
            word = normalize(word)
            author = author + get_score(word, dictionary)
            
    return author

'''
This function uses the functions above and compares the total score produced
by the get score function. The one with the higher score will output (either
willam or jane).
'''
def predict(user_input, william_counts, jane_counts):
    
    william = 0
    jane = 0
    
    sample_text = user_input.split()
    
    william = adding_scores(sample_text, william, william_counts)
    
    jane = adding_scores(sample_text, jane, jane_counts)
   
    if william > jane:
        print("I think this is William Shakespeare.")

    elif william == jane:
        print("It's the same!")

    else:
        print("I think this is Jane Austen.")


user_input = input("Your text: ")

predict(user_input, get_counts("hamlet.txt"), get_counts("pride-and-prejudice.txt"))

    




















