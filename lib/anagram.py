# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        original = sorted(self.word)  # Sort letters in the original word
        matches = []

        for word in word_list:
            if sorted(word) == original and word.lower() != self.word.lower():
                matches.append(word)

        return matches

