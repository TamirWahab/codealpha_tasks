import random
from typing import List

class Hangman:
    def __init__(self, words: List[str], max_guesses: int = 6):
        self.word: str = random.choice(words)
        self.guessed_letters: set = set()
        self.max_guesses: int = max_guesses
        self.incorrect_guesses: int = 0

    def get_display_word(self) -> str:
        return " ".join([char if char in self.guessed_letters else "_" for char in self.word])

    def play(self):
        print("Welcome to Modern Hangman!")
        
        while self.incorrect_guesses < self.max_guesses:
            print(f"\nWord: {self.get_display_word()}")
            print(f"Remaining Guesses: {self.max_guesses - self.incorrect_guesses}")
            
            if "_" not in self.get_display_word():
                print("\nCongratulations! You guessed the word correctly!")
                return

            guess = input("Guess a letter: ").strip().lower()
            
            # Input validation
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter!")
            elif guess in self.word:
                self.guessed_letters.add(guess)
                print("Correct guess!")
            else:
                self.guessed_letters.add(guess)
                self.incorrect_guesses += 1
                print("Incorrect guess!")

        print(f"\nGame Over! The word was: '{self.word}'")

if __name__ == "__main__":
    word_list = ["python", "intern", "coding", "alpha", "script"]
    game = Hangman(words=word_list)
    game.play()