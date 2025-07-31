import streamlit as st
import random
import time

# Utility functions
def scramble_word(word):
    scrambled = list(word)
    while True:
        random.shuffle(scrambled)
        if ''.join(scrambled) != word:
            break
    return ''.join(scrambled)

def calculate_score(difficulty):
    return {'easy': 1, 'medium': 2, 'hard': 3}.get(difficulty, 2)

# Initialize session state
if 'words' not in st.session_state:
    st.session_state.words = []
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'scrambled' not in st.session_state:
    st.session_state.scrambled = ''
if 'original' not in st.session_state:
    st.session_state.original = ''
if 'guess' not in st.session_state:
    st.session_state.guess = ''
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# App layout
st.title("🧠 Word Scramble Game")

with st.expander("📋 Game Setup", expanded=not st.session_state.words):
    st.markdown("Enter at least 5 words to create your word list.")
    word_input = st.text_area("Type words separated by commas (e.g. apple, banana, cherry)", height=100)
    rounds = st.number_input("How many rounds?", 1, 20, 5)
    timer_limit = st.slider("Time limit per round (seconds)", 3, 30, 5)
    difficulty = st.selectbox("Select difficulty", ['easy', 'medium', 'hard'])
    
    if st.button("✅ Start Game"):
        word_list = [w.strip().lower() for w in word_input.split(',') if w.strip().isalpha()]
        if len(word_list) < 5:
            st.warning("Please enter at least 5 valid words.")
        else:
            st.session_state.words = word_list
            st.session_state.rounds = rounds
            st.session_state.time_limit = timer_limit
            st.session_state.difficulty = difficulty
            st.session_state.score = 0
            st.session_state.round = 1
            st.session_state.scrambled = ''
            st.experimental_rerun()

if st.session_state.words:
    st.subheader(f"🔢 Round {st.session_state.round} of {st.session_state.rounds}")

    # Generate new word if needed or if the round has changed
    if st.session_state.scrambled == '':
        word = random.choice(st.session_state.words)
        scrambled = scramble_word(word)
        st.session_state.scrambled = scrambled
        st.session_state.original = word
        st.session_state.start_time = time.time()

    # Display scrambled word and input
    st.write(f"🔤 Scrambled Word: `{st.session_state.scrambled}`")
    time_elapsed = int(time.time() - st.session_state.start_time)
    time_left = st.session_state.time_limit - time_elapsed

    if time_left > 0:
        st.write(f"⏱️ Time left: **{time_left} seconds**")
        guess = st.text_input("Your guess", key=st.session_state.round)

        if guess:
            if guess.lower().strip() == st.session_state.original:
                points = calculate_score(st.session_state.difficulty)
                st.session_state.score += points
                st.success(f"✅ Correct! +{points} point(s)")
            else:
                st.error(f"❌ Wrong! The word was: `{st.session_state.original}`")

            if st.session_state.round == st.session_state.rounds:
                st.balloons()
                st.success(f"🎉 Game Over! Final Score: {st.session_state.score} / {st.session_state.rounds * calculate_score(st.session_state.difficulty)}")
                st.session_state.words = []
            else:
                st.session_state.round += 1
                st.session_state.scrambled = ''
            st.stop()
    else:
        st.warning(f"⏰ Time's up! The word was: `{st.session_state.original}`")

        if st.session_state.round == st.session_state.rounds:
            st.success(f"🏁 Game Over! Final Score: {st.session_state.score} / {st.session_state.rounds * calculate_score(st.session_state.difficulty)}")
            st.session_state.words = []
        else:
            st.session_state.round += 1
            st.session_state.scrambled = ''
        st.stop()
