class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def display(self):
        print("\n")
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print("|".join(row))
            print("-" * 5)

    def update_board(self, position, symbol):
        if self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def is_full(self):
        return " " not in self.board

    def check_winner(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[pos] == symbol for pos in condition) for condition in win_conditions)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        print("Welcome to Tic-Tac-Toe!")
        name1 = input("Enter name for Player 1 (X): ")
        name2 = input("Enter name for Player 2 (O): ")
        self.player1 = Player(name1, "X")
        self.player2 = Player(name2, "O")
        self.board = Board()

    def play(self):
        current_player = self.player1

        while True:
            self.board.display()
            try:
                move = int(input(f"{current_player.name} ({current_player.symbol}), choose a position (1-9): ")) - 1
            except ValueError:
                print("Invalid input. Enter a number from 1 to 9.")
                continue

            if move < 0 or move > 8:
                print("Position must be between 1 and 9.")
                continue

            if not self.board.update_board(move, current_player.symbol):
                print("That spot is already taken. Try again.")
                continue

            if self.board.check_winner(current_player.symbol):
                self.board.display()
                print(f"🎉 {current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            # Switch player
            current_player = self.player2 if current_player == self.player1 else self.player1


# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()
