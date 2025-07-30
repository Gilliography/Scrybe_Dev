import streamlit as st

# Board class to manage game state
class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def update(self, position, symbol):
        if self.cells[position] == " ":
            self.cells[position] = symbol
            return True
        return False

    def is_full(self):
        return " " not in self.cells

    def check_winner(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.cells[pos] == symbol for pos in condition) for condition in win_conditions)


# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = Board()
    st.session_state.current_symbol = "X"
    st.session_state.winner = None

st.title("🎮 Tic-Tac-Toe (Streamlit Version)")

# Player labels
st.write(f"Current Turn: **{st.session_state.current_symbol}**")

# Display game grid
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        cell = st.session_state.board.cells[index]
        if cell == " " and not st.session_state.winner:
            if cols[j].button(" ", key=index):
                if st.session_state.board.update(index, st.session_state.current_symbol):
                    # Check winner
                    if st.session_state.board.check_winner(st.session_state.current_symbol):
                        st.session_state.winner = st.session_state.current_symbol
                    elif st.session_state.board.is_full():
                        st.session_state.winner = "Draw"
                    else:
                        # Switch turns
                        st.session_state.current_symbol = "O" if st.session_state.current_symbol == "X" else "X"
        else:
            cols[j].button(cell, key=index, disabled=True)

# Display result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")

# Restart game
if st.button("🔄 Restart Game"):
    st.session_state.board = Board()
    st.session_state.current_symbol = "X"
    st.session_state.winner = None
