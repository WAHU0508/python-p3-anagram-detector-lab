# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, anagrams):
        word_list = sorted([letter for letter in self.word])
        self.anagrams = []
        for anagram in anagrams:
            anagram_list = sorted([leter for leter in anagram])
            if word_list == anagram_list:
                self.anagrams.append(anagram)
        return self.anagrams

anagram = Anagram("listen")
print(anagram.match(['enlists', 'google', 'inlets', 'banana']))