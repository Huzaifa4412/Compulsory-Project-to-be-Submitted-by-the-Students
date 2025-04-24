# What is Mad Libs?
# Mad Libs aik fun game hota hai jisme aap kuch blanks fill karte ho with different types of words like noun, verb, adjective, etc.
# Phir wo words aik story mein insert kiye jaate hain, jo end mein funny lagti hai.


def main():
    print("Mad Libs Game 😁")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    clothing_item = input("Enter a clothing item: ")
    song_name = input("Enter a song name: ")
    obj = input("Enter an object: ")
    verb = input("Enter a verb: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    emotion = input("Enter an emotion: ")
    famous_person = input("Enter a famous person: ")
    vehicle = input("Enter a vehicle: ")
    random_quote = input("Enter a random quote: ")
    type_of_dream = input("Enter a type of dream: ")

    story = f"""
    Yesterday, I went to the {place} to meet a {adjective} {animal}.
    It was wearing a {color} {clothing_item} and singing "{song_name}" at the top of its lungs.

    Suddenly, it pulled out a {obj} and started to {verb} like there was no tomorrow.
    Everyone around started {verb_ing}, and I couldn’t stop feeling {emotion}.

    Then {famous_person} showed up, riding a {vehicle}, and shouted:
    "{random_quote}"

    That’s when I realized it was all just a {type_of_dream}.
    """

    print("\n🧾 Your Mad Libs Story:")
    print(story)


if __name__ == "__main__":
    main()
