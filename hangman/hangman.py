import random
import streamlit as st
import time

# List of programming languages
words = [
    "ActionScript",
    "Ada",
    "Algol",
    "Android",
    "Angular",
    "Apache",
    "AppleScript",
    "Assembly",
    "AutoHotkey",
    "Bash",
    "Basic",
    "C",
    "C#",
    "C++",
    "Clojure",
    "COBOL",
    "CoffeeScript",
    "ColdFusion",
    "CSS",
    "D",
    "Dart",
    "Delphi",
    "Erlang",
    "F#",
    "Fortran",
    "Go",
    "Groovy",
    "Haskell",
    "Html",
    "Java",
    "Javascript",
    "Julia",
    "Kotlin",
    "Lisp",
    "Lua",
    "Maven",
    "Matlab",
    "MySQL",
    "Node.js",
    "Objective-C",
    "OCaml",
    "Oracle",
    "Pascal",
    "Perl",
    "PHP",
    "PostgreSQL",
    "PowerShell",
    "Prolog",
    "Python",
    "R",
    "Racket",
    "Ruby",
    "Rust",
    "SAS",
    "Scala",
    "Shell",
    "SQL",
    "Swift",
    "TypeScript",
    "VB.Net",
    "Visual Basic",
    "XML",
]


# Initialize game state
def initialize_state():
    if "secret_word" not in st.session_state:
        st.session_state.secret_word = random.choice(words).upper()
    if "lives" not in st.session_state:
        st.session_state.lives = 6
    if "guess_word" not in st.session_state:
        st.session_state.guess_word = ["_" for _ in st.session_state.secret_word]
    if "guessed_letters" not in st.session_state:
        st.session_state.guessed_letters = set()


# Main function
def main():
    initialize_state()
    st.title("🎯 Welcome to Hangman Game")
    st.subheader("👨‍💻 Guess the Programming Language")

    rules = [
        "You have 6 lives to guess the correct word.",
        "Each letter can be guessed only once.",
        "Only alphabetic characters are allowed.",
    ]
    st.subheader("Rules:")
    for rule in rules:
        st.markdown(f"- {rule}")

    # Hangman stages
    hangman_stages = [
        """
         ------
         |    |
         |    
         |   
         |   
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |   
         |   
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |    |
         |   
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |   
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        _|_
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        _|_
        """,
    ]

    # Check if game is already won
    if "_" not in st.session_state.guess_word:
        st.success(
            f"🎉 Congratulations! You guessed the Language: {st.session_state.secret_word}"
        )
        st.balloons()
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
        return

    # Check if game over
    if st.session_state.lives == 0:
        st.error("💀 Game Over. You ran out of lives!")
        st.info(f"The correct word was: {st.session_state.secret_word}")
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
        return

    # Game continues
    st.subheader(f"Stage {6 - st.session_state.lives}")
    stage = hangman_stages[6 - st.session_state.lives]
    st.code(stage, language="")
    st.subheader("Current Word:")
    st.text(" ".join(st.session_state.guess_word))
    st.write(f"Word Length: {len(st.session_state.secret_word)} letters")

    if st.session_state.guessed_letters:
        st.write(
            "Guessed Letters: ", ", ".join(sorted(st.session_state.guessed_letters))
        )

    with st.form("guess_form"):
        guess: str = st.text_input("Enter a letter: ").upper()
        submit = st.form_submit_button("Submit Guess")

    if submit:
        if guess.isalnum() and len(guess) != 1:
            st.error(
                f"❌ Invalid input '{guess}'. Please enter a single alphabetic letter."
            )
            time.sleep(1)
            st.rerun()

        if guess in st.session_state.guessed_letters:
            st.info(f"⚠️ You've already guessed '{guess}'. Try a new letter.")
            time.sleep(1)
            st.rerun()

        st.session_state.guessed_letters.add(guess)

        if guess in st.session_state.secret_word:
            st.success(f"✅ Correct guess: '{guess}'")
            for idx, char in enumerate(st.session_state.secret_word):
                if char == guess:
                    st.session_state.guess_word[idx] = guess
        else:
            st.session_state.lives -= 1
            st.error(f"❌ Wrong guess! Lives left: {st.session_state.lives}")

        time.sleep(1)
        st.rerun()


if __name__ == "__main__":
    main()
