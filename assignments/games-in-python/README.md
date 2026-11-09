# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. This assignment helps students practice core programming concepts while creating a complete interactive game.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description
Create the initial game state by choosing a random secret word and preparing variables to track guessed letters, incorrect attempts, and the player's progress.

#### Requirements
Completed program should:

- Store a list of words from which the game selects a random choice
- Randomly choose one secret word at the start of the game
- Create a display for the hidden word using underscores for unguessed letters
- Track the number of incorrect guesses and the maximum allowed mistakes
- Initialize a list to record letters the player has already guessed

### 🛠️ Game Loop and Guess Logic

#### Description
Write the main gameplay loop so the player can keep guessing letters until they either solve the word or run out of attempts.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter guess
- Check whether the guessed letter is in the secret word
- Reveal correctly guessed letters in the hidden word display
- Keep track of incorrect guesses and reduce remaining attempts
- Prevent duplicate guesses and inform the player when a letter has already been used
- Continue the game until the player wins or loses

### 🛠️ Win or Lose Outcome

#### Description
Finish the game by displaying the final result and clearly communicating whether the player won or lost.

#### Requirements
Completed program should:

- Show a message when the player correctly guesses the entire word
- Show a message when the player runs out of attempts
- Reveal the secret word at the end of the game
- Print a friendly final result such as "You win!" or "You lose!"
- Use clean, readable output that makes the game easy to follow
