"""EX03 - Structured Wordle."""

__author__ = "730482571"


def contains_char(any_length: str, single_char: str) -> bool:
    """Determines if a charcter is found in the word."""
    assert len(single_char) == 1
    i = 0
    exists_anywhere = False
    while i < len(str(any_length)):
        if single_char == any_length[i]:
            exists_anywhere = True
        i += 1
    if exists_anywhere is True:
        return True
    if exists_anywhere is False:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns a string of emojis depending on accuracy of guess."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_guess: str = ""
    track_index: int = 0
    while track_index < len(str(secret_word)):
        if guess[track_index] == secret_word[track_index]:
            emoji_guess += GREEN_BOX 
        else:
            if contains_char(secret_word, guess[track_index]):
                emoji_guess += YELLOW_BOX
            else: 
                emoji_guess += WHITE_BOX
        track_index += 1
    return emoji_guess                    


def input_guess(guess_length: int) -> str:
    """Given an integer of wrong 'expected length' prompts retry."""
    chr_word = input(f"Enter a {guess_length} character word: ")
    while guess_length != len(str(chr_word)):
        chr_word = input(f"That wasn't {guess_length} chars! Try again ")
    return chr_word    


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    # Your code will go here
    turn_number: int = 1
    secret_word: str = "codes"
    you_won: bool = False
    while turn_number <= 6 and you_won is False:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn_number}/6 turns !")
            you_won = True
        else:
            turn_number += 1
    if you_won is False:
        print("X/6 - Sorry, try again tomorrow!")
 
 
if __name__ == "__main__":
    main()