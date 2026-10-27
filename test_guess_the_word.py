"""
Kevin Soo
CIS256 Fall 2026
Programming Assignment 4
"""
import unittest
from guess_the_word import GuessTheWordGame

game = GuessTheWordGame()

class TestGuessTheWordGame(unittest.TestCase):
    """ Unit Tests for the GuessTheWordGame class """
    def test_reset_game(self):
        """ Testing the reset_game function to ensure class attributes are reset correctly """
        game.reset_game()
        # Assertion tests to make sure class attributes are correctly reset
        self.assertEqual(game.guessed_letters, [])
        self.assertEqual(game.remaining_guesses, game._STARTING_GUESS_COUNT)
        self.assertIn(game._chosen_word, game._word_list)
        self.assertEqual(game.word_progress_str, "_" * len(game._chosen_word))

    def test_validate_guessed_letter(self):
        """ Testing the letter validation function for when the user types in letter guesses """
        game.reset_game()
        # Testing valid values return true
        self.assertTrue(game._validate_guessed_letter('a'))
        self.assertTrue(game._validate_guessed_letter('Z'))
        # Testing invalid values return False
        self.assertFalse(game._validate_guessed_letter(1))
        self.assertFalse(game._validate_guessed_letter("?"))
        self.assertFalse(game._validate_guessed_letter("3"))
        self.assertFalse(game._validate_guessed_letter("ab"))
        # Testing already guessed letters return False
        game._guessed_letters = ['a']
        self.assertFalse(game._validate_guessed_letter("a"))

    def test_update_word_progress(self):
        """ Testing that the word_progress_str is updated properly """
        game.reset_game()
        # Change the chosen word to test
        game._chosen_word = "test"
        game._word_progress_str = "____"
        # Assertion tests on the new chosen word of test
        self.assertTrue(game._update_word_progress("e"))
        self.assertEqual(game._word_progress_str, "_e__")
        self.assertFalse(game._update_word_progress("a"))
        self.assertEqual(game._word_progress_str, "_e__")

    def test_check_game_over(self):
        """ Testing that the game over conditions are returning the correct results """
        game.reset_game()
        self.assertFalse(game.check_game_over())

        # End game when word is guessed
        game._word_progress_str = game._chosen_word
        self.assertTrue(game.check_game_over())

        # End game when out of guesses
        game.reset_game()
        game._remaining_guesses = 0
        self.assertTrue(game.check_game_over())

if __name__ == '__main__':
    unittest.main()
