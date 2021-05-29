# "Rock, Paper, Scissors" Exercise

This README file has been adapted from Professor Rossetti's "Rock, Paper, Scissors" and "My First Python App" README files. 

## Goal

Iteratively develop a command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent.

## Setup

### Repo Setup

Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub online interface, add a "README.md" file and a Python-flavored ".gitignore" file during the repo creation process. After this process is complete, you should be able to view the repo on GitHub at an address like `https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise`.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like Documents.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Documents/GitHub/rock-paper-scissors-exercise
```

Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

```py
# game.py

print("Rock, Paper, Scissors, Shoot!")
```

Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

### Environment Setup

Create and activate a new project-specific Anaconda virtual environment:

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```sh
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, you're ready to move on to project development. 

Use your text editor to create two additional files. The first file will be called "requirements.txt" and the second file will be called ".env". 

In the "requirements.txt" file, type in: python-dotenv. Save. 

In the ".env" file, you will choose a player name, ex: Carina. Type in: PLAYER_NAME="Carina". Save. 

To install the package dependencies from the requirements.txt file, type the below into your command line and press enter: 

```sh
pip install -r requirements.txt
```


## Requirements

Once you have completed the setup section above, you are ready to tackle the implementation of this exercise. Aim to make a separate commit after completing each section.

### Processing User Inputs

The application should prompt the user to input, or otherwise select, an option (i.e. "rock", "paper", or "scissors") via command-line interface (CLI). It should store the user's selection in a variable for later reference.

> HINT: use [the `input()` function](/notes/python/inputs.md) to capture user inputs.

### Validating User Inputs

The application should compare the user's selection against the list of valid options (i.e. "rock", "paper", "scissors") to determine whether the user has selected a valid option.

If the selection is invalid, the program should fail gracefully by displaying a friendly message to the user, and preventing further program execution. The program should not try to further process an invalid input, as it may lead to runtime errors.

> HINT: use the `exit()` or `quit()` keywords to stop the program.

### Simulating Computer Selection

The application should select one of the options (i.e. "rock", "paper", or "scissors") at random, and assign that as the computer player's choice.

> HINT: use the `choice()` function provided by [the `random` module](/notes/python/modules/random.md).

> HINT: ensure the valid choices are stored in a ["list" datatype](/notes/python/datatypes/lists.md), and then pass that list to the random choice function.

### Determining the Winner

The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

  1. Rock beats Scissors
  2. Paper beats Rock
  3. Scissors beats Paper
  4. Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

> HINT: use one or more [`if` statements](/notes/python/control-flow.md#if-statements) (recommended approach for beginners), or it may also be possible to use a pre-configured ["dictionary" datatype](/notes/python/datatypes/dictionaries.md) containing all possible outcomes.

### Displaying Results

After determining the winner, the application should display the results to the user. Desired information outputs (from start to finish) should include at least the following:

  + A friendly welcome message, including the player's name (by default, use "Player One").
  + The user's selected option
  + The computer's selected option
  + Whether the user or the computer was the winner
  + A friendly farewell message

Example desired output after one round of game-play:

```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': rock
You chose: 'rock'
The computer chose: 'paper'
-------------------
Oh, the computer won. It's ok.
-------------------
Thanks for playing. Please play again!
```

### Customizing the Player Name

Finally, update your program to allow the user to configure their own player name by passing the environment variable called "PLAYER_NAME" stored in the ".env" file. Instead of 'Player One', the game should welcome the player name specifed in the .env file. 
