import numpy as np
import pandas as pd

class Utils:
    @staticmethod
    def spell(sentence: str, thresh: float, seed=None):
        """
        Misspells a word by changing its spelling once in a random way

        :param word: str, the word to be misspelled
        :param seed: int, random seed for reproducibility

        :return: str, the misspelled word
        """
        np.random.seed(seed) if seed else None

        tokens = sentence.split()
        for i, word in enumerate(tokens):
            if np.random.rand() > thresh or len(word) < 3:
                continue

            change = np.random.randint(1, 5)
            if change == 1:
                # Add a letter close to the letter in the querty keyboard or itself
                idx = np.random.randint(len(word))
                word = word[:idx] + np.random.choice(list(letters[word[idx]]) + [word[idx]]) + word[idx:]
            elif change == 2:
                # Remove a letter
                idx = np.random.randint(len(word))
                word = word[:idx] + word[idx+1:]
            elif change == 3:
                # Swap two letters
                idx = np.random.randint(len(word)-1)
                word = word[:idx] + word[idx+1] + word[idx] + word[idx+2:]
            else:
                # Change a letter to a letter that is close to it in the querty keyboard
                idx = np.random.randint(len(word))
                word = word[:idx] + np.random.choice(list(letters[word[idx]])) + word[idx+1:]
        
            tokens[i] = word

        return " ".join(tokens)

    @staticmethod
    def remove_non_arabic(sentence: str):
        """
        Removes non-Arabic characters from a sentence

        :param sentence: str, the sentence to be cleaned

        :return: str, the cleaned sentence
        """
        sentence = sentence.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
        
        return "".join([char for char in sentence if char in letters.keys() or char == " "])

letters = {
    "ذ": ["د", "ز"],
    "ض": ["ص", "ش"],
    "ص": ["ض", "ث", "س"],
    "ث": ["ص", "ق"],
    "ق": ["ث", "ف"],
    "ف": ["ق", "غ"],
    "غ": ["ف", "ع"],
    "ع": ["غ", "ه"],
    "ه": ["ع", "خ"],
    "خ": ["ه", "ح"],
    "ح": ["خ", "ج"],
    "ج": ["ح", "د"],
    "د": ["ج", "ذ", "ض"],
    "ش": ["س", "ض"],
    "س": ["ش", "ي", "ص"],
    "ي": ["س", "ب"],
    "ب": ["ي", "ل"],
    "ل": ["ب", "ا"],
    "ا": ["ل", "ت"],
    "ت": ["ا", "ن"],
    "ن": ["ت", "م"],
    "م": ["ن", "ك"],
    "ك": ["م", "ط"],
    "ط": ["ك", "ظ"],
    "ئ": ["ء", "ش"],
    "ء": ["ئ", "ؤ"],
    "ؤ": ["ء", "ر"],
    "ر": ["ؤ", "لا"],
    "لا": ["ر", "ى"],
    "ى": ["لا", "ة"],
    "ة": ["ى", "و"],
    "و": ["ة", "ز"],
    "ز": ["و", "ظ", "ذ"],
    "ظ": ["ز", "ط"]
}

ar_to_en = {
    "ذ": "ذ",
    "ض": "q",
    "ص": "w",
    "ث": "e",
    "ق": "r",
    "ف": "t",
    "غ": "y",
    "ع": "u",
    "ه": "i",
    "خ": "o",
    "ح": "p",
    "ج": "[",
    "د": "]",
    "ش": "a",
    "س": "s",
    "ي": "d",
    "ب": "f",
    "ل": "g",
    "ا": "h",
    "ت": "j",
    "ن": "k",
    "م": "l",
    "ك": ";",
    "ط": "'",
    "ئ": "z",
    "ء": "x",
    "ؤ": "c",
    "ر": "v",
    "لا": "b",
    "ى": "n",
    "ة": "m",
    "و": ",",
    "ز": ".",
    "ظ": "/"
}

"""
5 Ways to change the spelling of a word:
1. Add a letter
2. Remove a letter
3. Swap two letters
4. Change a letter to a letter that is close to it in the querty keyboard
5. Change a letter to a letter it's corresponding to in the English layout. N/A since the llm doesn't accept English characters
"""
