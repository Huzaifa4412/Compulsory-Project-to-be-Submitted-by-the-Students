from random import randint
import streamlit as st


def init_state(max_number):
    if "game_over" not in st.session_state:
        st.session_state.update(
            {
                "secrete_number": randint(1, max_number),
                "game_over": False,
                "attempts": 0,
            }
        )


def play_version(name, max_number, max_attempts, form_key):
    st.title(f"{name} Number Guessing Game 🎮")

    rules = [
        f"You have {max_attempts} chances to guess the correct number to win 🏆",
        f"You have to guess the number between 1 to {max_number} 🔢",
    ]
    st.text("Rules:\n\t" + "\n\t".join([f"{i+1} - {r}" for i, r in enumerate(rules)]))

    if not st.session_state["game_over"]:
        with st.form(form_key):
            guess = st.number_input("Guess the number 🤔", 1, max_number, step=1)
            submit = st.form_submit_button("Submit 🏁")

        if submit:
            st.session_state["attempts"] += 1
            secret = st.session_state["secrete_number"]
            attempts = st.session_state["attempts"]

            # Store difference once
            diff = abs(secret - guess)

            if guess == secret:
                st.session_state["game_over"] = True
                st.balloons()
                st.success("You have won the game 🎉")
            elif guess < secret:
                st.warning("The number is greater than your guess 📈")
            else:
                st.warning("The number is less than your guess 📉")

            # Check closeness using the stored diff
            if diff <= 5:
                st.info("You are very close to the actual number 💪")
            elif diff <= 10:
                st.warning("You're not far off! Keep going! 🔥")

            if attempts >= max_attempts and not st.session_state["game_over"]:
                st.session_state["game_over"] = True
                st.error(f"Game Over! The correct number was {secret}")
                st.text("Oooh! Yes you lose the match 🤓🤣")

            st.info(f"Attempts: {attempts}/{max_attempts}")
    else:
        st.info("You're a genius! Let's play again 🎯")
        if st.button("Play Again 🙌"):
            st.session_state.clear()


def main():
    easy_tab, normal_tab = st.tabs(["Easy Version", "Normal Version"])
    with easy_tab:
        init_state(50)
        play_version("Easy", 50, 8, "easy_form")

    with normal_tab:
        init_state(100)
        play_version("Normal", 100, 8, "normal_form")


if __name__ == "__main__":
    main()
