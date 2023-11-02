import random

HANGMAN_IMAGES = [
    '''
    +---+
        |
        |
        |
       ===''',
    '''
    +---+
    O   |
        |
        |
       ===''',
    '''
    +---+
    O   |
    |   |
        |
       ===''',
    '''
    +---+
    O   |
   /|   |
        |
       ===''',
    '''
    +---+
    O   |
   /|\\  |
        |
       ===''',
    '''
    +---+
    O   |
   /|\\  |
   /    |
       ===''',
    '''
    +---+
    O   |
   /|\\  |
   / \\  |
       ==='''
]

word_list = 'apple banana cherry date elderberry fig grapefruit honeydew'.split()

def get_random_word(wordlist):
    return random.choice(wordlist)

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_IMAGES[len(missed_letters)])
    print()
    print('Missed letters:', ' '.join(missed_letters))
    
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    print(' '.join(blanks))

def get_guess(already_guessed):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def play_hangman():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(word_list)
    game_is_done = False
    
    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        
        if guess in secret_word:
            correct_letters += guess
            found_all_letters = all(letter in correct_letters for letter in secret_word)
            if found_all_letters:
                print(f'Yes! The secret word is "{secret_word}"! You have won!')
                game_is_done = True
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMAN_IMAGES) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was "{secret_word}"')
                game_is_done = True
        
        if game_is_done:
            if input('Do you want to play again? (yes or no): ').lower().startswith('y'):
                missed_letters = ''
                correct_letters = ''
                game_is_done = False
                secret_word = get_random_word(word_list)
            else:
                break

play_hangman()
