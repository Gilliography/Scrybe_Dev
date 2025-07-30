import random
import time
import threading

class WordScrambleGame:
    def __init__(self, word_list, rounds=5, time_limit=5, difficulty='medium'):
        self.word_list = word_list
        self.rounds = rounds
        self.time_limit = time_limit
        self.score = 0
        self.difficulty = difficulty.lower()
        self.points = {'easy': 1, 'medium': 2, 'hard': 3}

    def scramble_word(self, word):
        scrambled = list(word)
        while True:
            random.shuffle(scrambled)
            if ''.join(scrambled) != word:
                break
        return ''.join(scrambled)

    def get_guess_with_timer(self, time_limit):
        guess = [None]

        def time_limited_input():
            guess[0] = input("Your guess: ").strip().lower()

        input_thread = threading.Thread(target=time_limited_input)
        input_thread.start()
        input_thread.join(timeout=time_limit)

        if input_thread.is_alive():
            print("\n⏰ Time's up!")
            return None
        return guess[0]

    def play_round(self):
        word = random.choice(self.word_list)
        scrambled = self.scramble_word(word)

        print(f"\n🔤 Scrambled word: {scrambled}")
        print(f"⏱️ You have {self.time_limit} seconds to guess...")

        guess = self.get_guess_with_timer(self.time_limit)

        if guess is None:
            print(f"❌ You ran out of time! The word was '{word}'.")
        elif guess == word:
            points = self.points.get(self.difficulty, 2)
            self.score += points
            print(f"✅ Correct! You earned {points} point(s).")
        else:
            print(f"❌ Wrong! The correct word was: {word}")

    def start_game(self):
        print("\n🧠 Welcome to the Word Scramble Game!")
        print(f"🎮 Difficulty: {self.difficulty.capitalize()} | Rounds: {self.rounds} | Timer: {self.time_limit}s")
        print("🔥 Let's start!\n")

        for i in range(self.rounds):
            print(f"--- Round {i+1} ---")
            self.play_round()

        print(f"\n🏁 Game Over! Final Score: {self.score} / {self.rounds * self.points.get(self.difficulty, 2)}")

def get_user_words():
    print("Enter at least 5 words to create your custom word list.")
    words = []
    while len(words) < 5:
        word = input(f"Enter word {len(words)+1}: ").strip().lower()
        if word.isalpha():
            words.append(word)
        else:
            print("Please enter only alphabetic characters.")
    return words

def get_game_settings():
    try:
        rounds = int(input("How many rounds would you like to play? (Default: 5): ") or 5)
        time_limit = int(input("Time limit per word in seconds? (Default: 5): ") or 5)
        difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
        if difficulty not in ['easy', 'medium', 'hard']:
            difficulty = 'medium'
    except ValueError:
        print("Invalid input. Using default settings.")
        return 5, 5, 'medium'
    return rounds, time_limit, difficulty

# Entry point
if __name__ == "__main__":
    print("🎯 Word Scramble Game Setup")
    custom_words = get_user_words()
    rounds, time_limit, difficulty = get_game_settings()

    game = WordScrambleGame(custom_words, rounds, time_limit, difficulty)
    game.start_game()
