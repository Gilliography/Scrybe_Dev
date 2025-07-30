import random 
import time
import threading

class WordScramble:
    def __init__(self, word_list, rounds=5, time_limit=5, difficulty='medium'):
        self.word_list = word_list
        self.rounds = rounds
        self.time_limit = time_limit
        self.difficulty = difficulty
        self.current_round = 0
        