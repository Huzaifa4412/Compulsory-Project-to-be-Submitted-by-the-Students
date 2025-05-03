import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def hangman():
    words = [
        "SEO",
        "Keywords",
        "Backlinks",
        "Traffic",
        "Conversion",
        "CPC",
        "CTR",
        "PPC",
        "Google Ads",
        "Social Media",
        "Content Marketing",
        "Blogging",
        "SEO Audit",
        "On-page SEO",
        "Off-page SEO",
        "Meta Tags",
        "Title Tag",
        "Header Tags",
        "Alt Text",
        "Anchor Text",
        "Rank",
        "SERP",
        "Google Analytics",
        "Bounce Rate",
        "Impressions",
        "Engagement",
        "Click-Through Rate",
        "Audience",
        "Targeting",
        "Reach",
        "Content Creation",
        "Digital Ads",
        "Organic Traffic",
        "Paid Traffic",
        "Landing Page",
        "Call to Action",
        "Email Marketing",
        "Content Strategy",
        "Marketing Funnel",
        "Campaign",
        "Lead Generation",
        "Affiliate Marketing",
        "Influencer Marketing",
        "Google Search Console",
        "Social Media Ads",
        "Brand Awareness",
        "SEO Ranking",
        "Keywords Research",
        "Content Strategy",
        "Marketing Automation",
        "Customer Journey",
        "E-commerce Marketing",
        "Website Optimization",
        "Local SEO",
        "Traffic Sources",
        "Mobile Optimization",
        "User Experience",
        "Conversion Rate Optimization",
        "SEO Tools",
    ]
    random_word = random.choice(words).strip().upper()
    word = ""
    for char in random_word:
        if char == " ":
            continue
        else:
            word += char
    lives = 6
    guess_letters = set()
    guess_word = ["_" for _ in word]
    # print(f"{Style.BRIGHT}{Fore.GREEN}{' '.join(guess_word)}")
    print(f"{Style.BRIGHT}{Fore.RED}The total characters in the word are {len(word)}")
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

    print(word)
    while lives > 0:
        print(hangman_stages[6 - lives])
        print(f"{Style.BRIGHT}{Fore.YELLOW}Word: {' '.join(guess_word)}")
        print(
            "Total remaining characters are",
            len([char for char in guess_word if char == "_"]),
        )
        if len(guess_letters) > 0:
            print(
                f"{Style.BRIGHT}{Fore.CYAN}Guessed Letters: ",
                ", ".join(sorted(guess_letters)),
            )
        guess = input(f"{Style.BRIGHT}{Fore.MAGENTA}Enter a letter: ").upper()

        if (not guess.isalpha()) or (len(guess) != 1):
            print(
                f"{Fore.RED}Invalid input. Please enter a single and a valid alphabet letter."
            )
            continue

        if guess in guess_letters:
            print(f"{Fore.RED}You have already guessed that letter. Try again.")
            continue

        guess_letters.add(guess)

        if guess in word:
            for index, character in enumerate(word):
                if character == guess:
                    guess_word[index] = character
        else:
            lives -= 1
            print(f"{Fore.RED}Wrong guess. You have {lives} lives left.")

        if "_" not in guess_word:
            print(
                f"{Fore.GREEN}{Style.BRIGHT}Congratulations! You guessed the word: {word}"
            )
            break
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Game Over. You ran out of lives.")
        print(f"{Fore.YELLOW}The word was: {word}")


if __name__ == "__main__":
    hangman()
