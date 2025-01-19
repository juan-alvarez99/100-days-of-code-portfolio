from morse_alphabet import MORSE_ALPHABET

class MorseCodeConverter:
    """
    The length of a dot is one unit
    The length of a dash is three units
    The space between parts of the same letter is one unit
    The space between letters is three units
    The space between words is seven units
    """
    def __init__(self, space_unit: int):
        self.space_unit: int = space_unit
        self.__space_letters: str = space_unit*3*" "
        self.__space_words: str = space_unit*7*" "
        self.__morse_alphabet: dict[str, str] = MORSE_ALPHABET

    def _translate_word(self, word: str) -> str:
        """
         For each character translates to the corresponding morse code leaving
         three units of space between letters and removing the trailing spaces

        :param str word: string to convert into Morse Code letter by letter
        :return:
         """
        morse_word: str = "".join([self.__morse_alphabet[letter.upper()] + self.__space_letters
                           for letter in word if letter.upper() in self.__morse_alphabet])

        return morse_word.strip()

    def translate(self, msg: str) -> str:
        """
        Convert a string message into Morse Code where dots, dashes and space between members of the same word are
        constant 1 unit

        :param msg: string to translate
        :return: Converted message
        """
        return ("".join([self._translate_word(word) + self.__space_words for word in msg.split(" ")])).strip()


if __name__ == "__main__":
    user_msg = input("Please enter a message to translate to morse code: ")
    morse_code_converter: MorseCodeConverter = MorseCodeConverter(1)
    print(morse_code_converter.translate(user_msg))
