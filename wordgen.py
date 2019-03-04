from text_break import text_break
import random

letters = text_break("shakespeare.txt", "qwertyuiopasdfghjklzxcvbnm ")
letters.run()
l_freq = letters.get_letter_freq()
print("analysis done")

def gen(word = ""):
    
    word = word.lower()
    print(word)
    
    if word == "": #checks if user gave starting letter(s)
        
        p = random.random() #initial random generation
        cumulative_p = 0

        for s_letter in l_freq[" "]: #picks word start based on letters coming after a space
            cumulative_p += l_freq[" "][s_letter]

            if p <= cumulative_p:
                word += s_letter
                break

    while word[-1] != " ": #while the word hasn't ended
        p = random.random() 
        cumulative_p = 0
        
        for s_letter in l_freq[word[-1]]: #picks a letter using the probalities of letters following that letter
            cumulative_p += l_freq[word[-1]][s_letter]

            if p <= cumulative_p: #checks if letter should be added
                word += s_letter
                break
            
    return word
