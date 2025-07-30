import random 
import time
import threading

class WordScramble:
    def __init__(self, word_list, rounds=5, time_limit=5, difficulty='medium'):
        self.word_list = word_list
        self.rounds = rounds
        self.time_limit = time_limit
        self.difficulty = difficulty.lower()
        self.current_round = 0
        self.score = 0
        self.points_per_round = 10 if difficulty == 'easy' else 20 if difficulty == 'medium' else 30
    
    def scramble_word(self, word):
        scrambled = list(word)
        while True:
            random.shuffle(scrambled)
            if ''.join(scrambled) != word:
                break
        return ''.join(scrambled)
    
    def get_guess_with_timer(self, time_limit):
        guess = [None]
        guess[0] = input("Enter your guess: ").strip().lower()
        
        input_thread = threading.Thread(target=self.time_limit_input, args=(guess, time_limit))
        input_thread.start()
        input_thread.join(timeout=time_limit)
        
        if input_thread.is_alive():
            print("Time's up! You didn't guess in time.")
            return None
        return guess[0]

        def time_limit_input():
            guess[0] = input(f"Guess the word (You have {time_limit} seconds): ")
            timer.cancel()

        timer = threading.Timer(time_limit, lambda: guess.__setitem__(0, None))
        timer.start()
        time_limit_input()
        return guess[0]
