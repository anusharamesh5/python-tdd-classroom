class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        output_string = input_str[::-1]
        return output_string

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        character = character.lower()
        if(character in 'aeiou'):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest_word = max(sentence.split(), key=len)
        return longest_word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        word_lengths = []
        word_lengths_list = text.split(" ")
        # print(word_lengths_list)
        for x in word_lengths_list:
            word_lengths.append(len(x))

        return word_lengths