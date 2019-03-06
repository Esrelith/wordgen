import random

class text_break(object):

    def __init__(self, tfile = None, chars = None):
        self.allowed_char = chars #allowed characters for word generation
        self.letter_freq = {} #dictionary of dictionaries that contain letter frequencies
        self.file = tfile #file to operate on
        self.word_length = {} #dictionary containing counts of word lengths

        if self.file != None:
            with open(self.file) as f:
                self.contents = f.read()
                self.contents = self.contents.lower()
                
        else:
            self.contents = None
            

    def set_file(self, filename):
        self.file = filename

    def get_file(self):
        return self.file

    def set_chars(self, chars):
        self.allowed_char = chars

    def get_chars(self):
        return self.allowed_char

    def get_letter_freq(self):
        return self.letter_freq

    def get_word_len(self):
        return self.word_length

    def __histogram(self, contents, allowed_chars): #creates dictionary within dictionary for each letter in allowed_char
        chars = {}
        for char in contents:
            if char in allowed_chars and char not in chars.keys():
                chars[char] = {}

        return chars

    def __next_letter(self, contents, allowed_chars, chars): #add the count of letter y following letter x to letter x's dictionary
        for key in chars.keys():
            for i in range(len(contents) - 1):
                if contents[i + 1] in allowed_chars and contents[i] == key:
                    if contents[i + 1] in chars[key]:
                        chars[key][contents[i + 1]] += 1

                    else:
                        chars[key][contents[i + 1]] = 1

        return chars

    def __letter_percentages(self, chars): #changes letter y's count to a percentage of the total
        for key in chars.keys():
            total = 0
            
            for letter in chars[key].keys(): #adding up total for each letters subsequent letters
                total += chars[key][letter]

            for letter in chars[key].keys(): #calculating percentage of total for each letter
                chars[key][letter] = chars[key][letter]/total

        return chars

    def __word_break(self): #breaks contents into a list of words and makes sure word only contain allowed letters
        lines = self.contents.split("\n")
        words = []

        for line in lines:
            for word in line.split(" "):
                cleaned_word = ""
                for char in word:
                    if char in self.allowed_char:
                        cleaned_word += char
                        
                words.append(cleaned_word)

        return words

    def __word_length_perc(self, w_lengths):
        total = 0
        
        for key in w_lengths.keys():
            total += w_lengths[key]

        for key in w_lengths.keys():
            w_lengths[key] = w_lengths[key]/total

        return w_lengths

            

    def run_word_len(self): #counts amount of word length n and adds it to n's value in self.word_length
        words = self.__word_break()

        for word in words:
            if len(word) in self.word_length.keys() and len(word) > 0:
                self.word_length[len(word)] += 1

            elif len(word) > 0:
                self.word_length[len(word)] = 1

        self.word_length = self.__word_length_perc(self.word_length)

    def run(self):

        self.letter_freq = self.__histogram(self.contents, self.allowed_char)
        self.letter_freq = self.__next_letter(self.contents, self.allowed_char, self.letter_freq)
        self.letter_freq = self.__letter_percentages(self.letter_freq)
