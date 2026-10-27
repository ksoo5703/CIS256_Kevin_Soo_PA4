from guess_the_word import GuessTheWordGame

import unittest

game = GuessTheWordGame()

class TestGuessTheWordGame(unittest.TestCase):
    def test_reset_game(self):
        game.reset_game()
        self.assertEqual(game.guessed_letters, [])
        self.assertEqual(game.remaining_guesses, game._STARTING_GUESS_COUNT)
        self.assertIn(game._chosen_word, game._word_list)
        self.assertEqual(game.word_progress_str, "_" * len(game._chosen_word))

    def test_validate_guessed_letter(self):
        game.reset_game()
        self.assertTrue(game._validate_guessed_letter('a'))
        self.assertTrue(game._validate_guessed_letter('Z'))
        self.assertFalse(game._validate_guessed_letter(1))
        self.assertFalse(game._validate_guessed_letter("?"))
        self.assertFalse(game._validate_guessed_letter("3"))
        self.assertFalse(game._validate_guessed_letter("ab"))
        game._guessed_letters = ['a']
        self.assertFalse(game._validate_guessed_letter("a"))

    def test_update_word_progress(self):
        game.reset_game()
        game._chosen_word = "test"
        self.assertTrue(game._update_word_progress("e"))
        self.assertEqual(game._word_progress_str, "_e__")
        self.assertFalse(game._update_word_progress("a"))
        self.assertEqual(game._word_progress_str, "_e__")

    def test_check_game_over(self):
        game.reset_game()
        self.assertFalse(game.check_game_over())
        game._word_progress_str = game._chosen_word
        self.assertTrue(game.check_game_over())

if __name__ == '__main__':
    unittest.main()
