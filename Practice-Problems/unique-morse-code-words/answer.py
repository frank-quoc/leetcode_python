class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE_CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = []
        for word in words:
            morse = ""
            for letter in word:
                letter_num = ord(letter) - 97
                morse += MORSE_CODE[int(letter_num)]
            transformations.append(morse)
        return len(set(transformations))
