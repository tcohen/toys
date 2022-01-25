import random

letters = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
board = [
    [letter for letter in letters],
    [letter for letter in letters],
    [letter for letter in letters],
    [letter for letter in letters],
    [letter for letter in letters],
]
required = ""

def apply_score(word, score):
    global letters, board, required

    for index in range(len(word)):
        letter = word[index]
        letter_score = score[index]
        if letter_score == "y": #right place
            #only letter at index
            board[index] = [letter]
            #letter is required
            if not letter in required:
                required = required + letter
        elif letter_score == "n": #not a letter
            #letter is not in any place
            for place in range(len(board)):
                if letter in board[place]:
                    board[place].remove(letter)
        elif letter_score == "w": #wrong place
            #letter is not at current index
            if letter in board[index]:
                board[index].remove(letter)
            #but it is required
            if not letter in required:
                required = required + letter

def word_is_valid(word):
    global board

    for place in range(len(word)):
        letter = word[place]
        if not letter in board[place]:
            return False

    for letter in required:
        if not letter in word:
            return False

    return True

def do_guess(words):

    guess_index = random.randrange(0, len(words))
    guess = words[guess_index]
    print("My guess: " + guess.upper())
    score = input("What's my score? [(Y)es, (N)o, (W)rong position]: ").lower()
    apply_score(guess, score)
    return (guess, score)
    
def update_words(words, guess, score):

    new_list = []

    for word in words:

        if word_is_valid(word):
            new_list.append(word)

    return new_list


print("\n** WORDLE! **\n")

# read-in the list of words
file = open("words.list", "r")
words = [word[:5] for word in file.readlines()]

num_words = len(words)
guesses = 0

while num_words > 1:
    if num_words < 10:
        print("I've narrowed it down to one of these words:")
        for word in words:
            print(f"    {word.upper()}")
    elif num_words < 100:
        print(f"I've narrowed it down to {str(len(words))} words")

    (guess, score) = do_guess(words)
    guesses = guesses + 1
    words = update_words(words, guess, score)
    num_words = len(words)

if num_words == 0:
    print("You got me. I can't figure it out!")
elif num_words == 1:
    print(f"I got it in {guesses} guesses! The word is: {words[0].upper()}")



