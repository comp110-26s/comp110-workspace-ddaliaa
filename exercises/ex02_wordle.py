"""A Wordle game."""
__author__ = "730700758"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, character: str) -> bool:
    """Check if character is in word."""
    assert len(character) == 1, f"len('{character}') is not 1"

    idx: int = 0

    while idx < len(word):
        if word[idx] == character:
            return True
        idx += 1

    return False

def emojified(guess: str, secret: str) -> str:
    """Return emoji result string."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result: str = ""
    idx: int = 0

    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(word=secret, character=guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

        idx += 1

    return result

def input_guess(expected_length: int) -> str:
    """Prompt user for a guess."""
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess

def main(secret: str) -> None:
    """The main game loop."""

    turn: int = 1
    max_turns: int = 6
    won: bool = False

    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/6 ===")

        guess: str = input_guess(expected_length=len(secret))

        print(emojified(guess=guess, secret=secret))

        if guess == secret:
            won = True
        else:
            turn += 1

    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="codes")
