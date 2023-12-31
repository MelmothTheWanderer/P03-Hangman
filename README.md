# HANGMAN

## How to play:

![Hangman app on screens](./images/hangman_screens.png)

The classic game of hangman is a simple one. One has to guess a word by choosing letters that might be in the word. If the letter is in the word , then the letter/letters at their respective positions are revealed and the game continues, however if you guess a letter that is not in the word , there are consequences: a little man representing your "lives" in the game inches one step closer to his grim fate. The game continues until all the letters in the word are guessed, resulting in a victory, the other outcome is that the player runs out of lives, resulting in a loss . 

You can visit the live site on Heroku [here](https://hangman-jamie-simms-aab00bf1f5f3.herokuapp.com/) .

## Features

### Many words to guess from: 
I used an array with many different words of varying length to give the game a lot of room for replayability:

![word_list](./images/list_of_words.png)

### ASCII LOGO:

The game features a nice little logo to go over the top of the screen:

![ascii_art_logo](./images/ascii_logo_hangman.png)

It is made using ASCII art, which is a way of representing pictures using text and characters.

### ASCII Hangman Gallows

Using the same ASCII art that makes the logo for the game possible, I have arranged a little set of art works, saved into it's own array in the game files, that represent the various stages of the poor man that is about to be hung if the player is not successful. There are seven of these designs in total:

![ascii_art_stages_for_the_hangman](./images/hangman_stages.png)

### Letter Display

I included a display to visually represent the word that the player is trying to guess. At first it appears as an array of empty underscores, one for each of the letters in the word that is being guessed. As the player begin to guess letters correctly , the underscores get replaced with the correctly guessed letters.-

#### Empty display:
![word_display_empty](./images/word_display_1.png)

#### Correct letters:
![word_display_full](./images/word_display_2.png)

### Input and Validation:

Users are prompted to input a letter into the terminal , but there is input validation to ensure that the user does not:

- input an empty value
- input a number
- input any character that is not a letter of the alphabet
- input more than one letter

### Varying messages:

The message when the player gets a "hit" or "miss" are not static, they may be different.

#### Hit messages:
![good1](./images/good1.png)

![good2](./images/good2.png)

#### Miss messages:

![bad1](./images/bad1.png)

![bad2](./images/bad2.png)

### Continue screen:

Whether the player is victorious or ends up hanging their unfortunate companion, the player is presented with the choice whether or not they want to continue by way of a simple y/n input. This screen also has input validation to make sure that the player cannot break the game by inputting something other than a "y" or a "n".

### Future features:

In the future I would like to see the following features in addition to the ones that are already available: 

- A difficulty option (easy, medium, hard)
- A display for the letters that have been guessed already.

### Data model:

#### The code is object oriented and almost every aspect of the game is stored within an object simply called "Game". This objects stores the following data:

- The word to be guessed.
- The amount of "lives" that the player has left. 
- The letters and underscores in the display
- The letters that have already been guessed.

#### The game object also houses all of the functions that make the game possible such as:

- Clearing the screen. 
- Creating the word display.
- Refreshing the screen with up-to-date information.
- Displaying validation messages clearly
- Making a validating user guesses
- Checking those guesses to see if it is a hit or a miss
- Resetting the game and restoring default values
- ASking the player whether they would like to continue.

### Testing:

I have done the following to test for my project:

- I passed my code through the PEP8 linter and corrected anything that the linter showed up , which was mostly just whitespace and too many empty lines between code.
- I tried every method of input to mmake sure that the code wasn't throwing any unexpected errors.
- I played the game many many times on my Linux terminal as I was coding my project and many times afterwards, including on Heroku (where the project was deployed)
- I got my friends and family to play the game a couple of times to see if they could see something that I had missed.

### Bugs: 

- At one point there was a bug where the logo would print twice. 
- I had to ammend the code so that special characters like "@" and "!" and so on where not permissible. 
- There was a bug where the user would have to select "n" multiple times in order to exit the program.

#### Remaining bugs: 
No remaining bugs.

### Validator testing: 
-PEP8
    -No errors. Everything good.


### Deployment: 

I deployed my code on Heroku using the CodeInstitute's template. 
The steps involved in doing so were: 


- Create an account of Heroku or just log in if you already have one.
- Create a new app
- Give your app a unique name, it can't be something that has been used before.
- Pick your country and go ahead and click the "Create App" button
- Add the Python3 and NodeJS buildpacks in the settings.
- Click on deploy using Github as the method
- Search for the name of your project in t   he search bar
- Click to enable automatic updates from your Github
- Deploy from main branch

### Credits: 

- Code Institute for the validator and the template.
- My Code Institute Mentor Derek who pointed out bugs and suggested improvements. 
- My wife for the 50 or so cups of tea it took to make this project. 
