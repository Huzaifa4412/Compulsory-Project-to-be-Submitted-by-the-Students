def computer_guess(range: int):

    print(
        f"Think of a number between 1 and {range} (inclusive), and I will try to guess it."
    )
    input("Press Enter when you're ready...")
    low = 1
    high = range
    guesses = 0
    while True:
        guesses += 1
        comp_guess = (low + high) // 2

        print(f"\nMy guess is: {comp_guess}")
        feedBack: str = input("Is it (h)high, (l)low, or (c)correct? ").lower()

        if feedBack == "c":
            print(print(f"Yay! I guessed your number in {guesses} tries. 🎉"))
            break
        elif feedBack == "h":
            high = comp_guess - 1
        elif feedBack == "l":
            low = comp_guess + 1

        if low > high:
            print("Are you trying to trick me ? 🤔🥱")
            break


if __name__ == "__main__":
    computer_guess(100)
