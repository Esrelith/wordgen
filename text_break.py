import random

class text_break(object):

    def __init__(self):
        self.allowed_char = None #allowed characters for word generation
        self.letter_freq = {} #dictionary of dictionaries that contain letter frequencies
        self.letter_perc = {}
        self.file = None #file to operate on
        self.word_length = {} #dictionary containing counts of word lengths

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

##    def get_letter_perc(self):
##        return self.letter_perc

    def __histogram(self, contents, allowed_chars):
        chars = {}
        for char in contents:
            if char in allowed_chars and char not in chars.keys():
                chars[char] = {}

        return chars

    def __next_letter(self, contents, allowed_chars, chars):
        for key in chars.keys():
            for i in range(len(contents) - 1):
                if contents[i + 1] in allowed_chars and contents[i] == key:
                    if contents[i + 1] in chars[key]:
                        chars[key][contents[i + 1]] += 1

                    else:
                        chars[key][contents[i + 1]] = 1

        return chars

    def __letter_percentages(self, chars):
        for key in chars.keys():
            total = 0
            for letter in chars[key].keys():
                total += chars[key][letter]

            for letter in chars[key].keys():
                chars[key][letter] = chars[key][letter]/total

        return chars
            

    def run(self):
        f = open(self.file)
        contents = f.read()
        f.close()

        contents = contents.lower()

        self.letter_freq = self.__histogram(contents, self.allowed_char)
        self.letter_freq = self.__next_letter(contents, self.allowed_char, self.letter_freq)
        self.letter_perc = self.__letter_percentages(self.letter_freq)
