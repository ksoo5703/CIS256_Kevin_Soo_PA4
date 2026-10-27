"""
Kevin Soo
CIS256 Fall 2026
Programming Assignment 4
"""
import random

class GuessTheWordGame:
    """ Class to track game attributes and perform game functions """
    _word_list = [
        "apple", "river", "castle", "guitar", "window", "pencil", "rocket", "forest",
        "bridge", "candle", "dragon", "garden", "hammer", "island", "jungle", "kitten",
        "ladder", "mirror", "nickel", "orange", "pirate", "quilt", "rabbit", "saddle",
        "tunnel", "umbrella", "violin", "walnut", "yogurt", "zipper", "anchor", "balloon",
        "cactus", "diamond", "engine", "feather", "glacier", "harbor", "igloo", "jacket",
        "kettle", "lantern", "meadow", "needle", "ocean", "puzzle", "ribbon", "sunset",
        "thunder", "volcano", "whistle", "blanket", "compass", "dolphin", "eclipse",
        "fountain", "giraffe", "horizon", "jigsaw", "lighthouse", "magnet", "notebook",
        "orchard", "parrot", "quarter", "pyramid", "satellite", "telescope", "unicorn",
        "village", "waffle", "xylophone", "yacht", "zebra", "avalanche", "bicycle",
        "carousel", "dungeon", "elephant", "flamingo", "gondola", "hurricane", "iceberg",
        "kangaroo", "labyrinth", "mushroom", "nightmare", "octopus", "penguin", "raccoon",
        "scarecrow", "tornado", "whisper", "wizard", "trumpet", "sandwich", "pumpkin"
    ]
    _guessed_letters = []
    _word_progress_str = ""
    _remaining_guesses = 0
    _STARTING_GUESS_COUNT = 5

    def __init__(self):
        self.reset_game()

    @property
    def guessed_letters(self):
        """ Getter for guessed_letters attribute """
        return self._guessed_letters
    @property
    def remaining_guesses(self):
        """ Getter for remaining_guesses attribute """
        return self._remaining_guesses
    @property
    def word_progress_str(self):
        """ Getter for word_progress_str attribute """
        return self._word_progress_str

    def _validate_guessed_letter(self, val):
        """ Checks if a guessed letter is a valid entry """
        if not val.isalpha():
            print("Please enter only letters a-z.")
        elif len(val) != 1:
            print("Please enter a single letter.")
        elif val.lower() in self.guessed_letters:
            print("Please enter a letter that has not been used.")
        else:
            return True

        return False

    def _update_word_progress(self, selected_letter):
        """ Updates the word_progress_str and returns if a letter was changed """
        for i, letter in enumerate(self._chosen_word):
            if letter == selected_letter:
                self._word_progress_str[i] = selected_letter
                return True

        return False

    def check_game_over(self):
        """ Checks if the game is over and displays a win or loss message to the user. """
        if "_" not in self._word_progress_str:
            print("Congratulations!. You guessed the word.")
            return True
        if self.remaining_guesses == 0:
            print("Sorry, you ran out of guesses.")

        return False

    def guess_letter(self):
        """ Allows user to guess a letter and 
        performs necessary backend game functionality after letter is guessed. """

        # Display game information
        print(self._word_progress_str)
        print(f"Guessed Letters: {self._guessed_letters}")
        print(f"Remaing Guesses: {self._remaining_guesses}")

        # Ask user for letter and validate
        selected_letter = input("Guess a letter: ")
        while not self._validate_guessed_letter(selected_letter):
            selected_letter = input("Guess a letter: ")

        # Update game attributes
        selected_letter = selected_letter.lower()
        self._guessed_letters.append(selected_letter)
        self._remaining_guesses -= 1

        # Display result of letter guess
        update_check = self._update_word_progress(selected_letter)
        if update_check:
            print(f"There is a(n) {selected_letter} in the word!")
        else:
            print(f"The letter {selected_letter} is not in the word.")

        # Display word progress
        print(self._word_progress_str)

    def reset_game(self):
        """ Resets the game state and chooses a new word. """
        self._guessed_letters = []
        self._remaining_guesses = self._STARTING_GUESS_COUNT
        self._chosen_word = random.choice(self._word_list)
        self._word_progress_str = "_" * len(self._chosen_word)
        print("The mystery word has been chosen.")
if __name__ == '__main__':
    game = GuessTheWordGame()
    replay = "y"
    print("Welcome to the Word Guesser Game")

    while replay == "y":
        while not game.check_game_over():
            game.guess_letter()
        replay = input("Play again? (y/n): ")
        if replay == "y":
            game.reset_game()
