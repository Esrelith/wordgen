from text_break import text_break
import random

letters = text_break("ipsum.txt", "qwertyuiopasdfghjklzxcvbnm ")
letters.run()
l_freq = letters.get_letter_freq()
print("ANALYSIS DONE\n")

def gen(word = "", word_length = 8):
    
    word = word.lower()
    
    if word == "": #checks if user gave starting letter(s)
        
        p = random.random() #initial random generation
        cumulative_p = 0

        for s_letter in l_freq[" "]: #picks word start based on letters coming after a space
            cumulative_p += l_freq[" "][s_letter]

            if p <= cumulative_p:
                word += s_letter
                break

    while word[-1] != " ": #while the word hasn't ended
    #while len(word) < 4:
        p = random.random() 
        cumulative_p = 0
        
        for s_letter in l_freq[word[-1]]: #picks a letter using the probalities of letters following that letter
            cumulative_p += l_freq[word[-1]][s_letter]

            if p <= cumulative_p: #checks if letter should be added
                word += s_letter
                break
            
    return word

for i in range(32):
	print(gen("", 8))
