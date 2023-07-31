# Daniel Shin
# Project: WORDLE console

# import modules
import time
import random
import math
import os
os.system('')

# import wordles (answers) and wordList (possible words) from custom library
from words import wordles, wordList

# game scene
scene = 'check'
running = True

# game settings
settings = {
  'block text': True,
  'animation': False, # experimental
  'keyboard': False # experimental
}

# game responses
responses = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']

# ASNI Escape Codes with reference to https://github.com/tartley/colorama/blob/master/colorama/ansi.py
# list of escape codes for colors
colors = {
  'green': '\33[92m',
  'yellow': '\33[93m',
  'gray': '\33[90m',
  'greenbg': '\33[102m',
  'yellowbg': '\33[103m',
  'graybg': '\33[100m',
  'end': '\33[0m'
}

# function that clears previous line and replaces with text
def clear(text = ''):
  return f'\033[1A{text}\033[K'

# function that changes what line it prints to
def line(y):
  return f'\033[{y};1H'

# function that clears entire screen
def clearScreen(text):
  return f'\033[2J{line(1)}{text}'

# function that colors text with optional argument of whether it is a "block" text with a background
def colorify(text, color, block = True):
  if block == True:
    return colors[color + 'bg'] + text + colors['end']
  else:
    return colors[color] + text + colors['end']

# for game statistics
stats = {
  'played': 0,
  'wins': [0, 0, 0, 0, 0, 0]
}

# while game is running
while running:
  # first check to see if colored texts work
  if scene == 'check':
    print('WORDLE console\nThis program uses ASNI Escape Codes.\nAre the text below colored with their respective colors? (Y/N)\n')
    print(colorify('GREEN', 'green'), colorify('YELLOW', 'yellow'), colorify('GRAY', 'gray'))
    print(colorify('GREEN', 'green', False), colorify('YELLOW', 'yellow', False), colorify('GRAY', 'gray', False))
    answer = input('\n> ')

    if answer.upper() == 'Y':
      scene = 'check2'
    else: 
      print('Try running this on replit\nhttps://replit.com/@DanielShin11/WORDLE-console')
      running = False

  # second check to see if clearing texts work
  if scene == 'check2':
    print(clearScreen(colorify('WORDLE', 'green') + ' console'))
    print('This program uses ASNI Escape Codes.\nDid the colored text from before disappear? (Y/N)')
    answer = input('\n> ')

    if answer.upper() == 'Y':
      scene = 'reset'
    else: 
      print('Try running this on replit\nhttps://replit.com/@DanielShin11/WORDLE-console')
      running = False

  # game reset including the wordle, attempt, return list, keyboard, and screen
  if scene == 'reset':
    print(clearScreen(colorify('WORDLE', 'green') + ' console'))
    print(line(5) + f"Guess to start.\n[S]etting [H]elp s[T]atistics")
    keyboard = list('Q W E R T Y U I O P A S D F G H J K L Z X C V B N M')
    attempt = 0
    correctWord = random.choice(wordles).upper()
    correctWordList = list(correctWord)
    returnList = list('     ')
    scene = 'guess'

  # statistics screen
  if scene == 'stats':
    print(f"{clearScreen(colorify('WORDLE', 'green'))} console\n\n{stats['played']} Played   {math.floor(sum(stats['wins']) / stats['played'] * 100) if stats['played'] > 0 else '0'} Win %\n")
    if max(stats['wins']) != 0:
      print('Guess Distribution')
      for i in range(0, 6):
        print(f"{i + 1} {colorify(' ', 'gray') * math.floor(stats['wins'][i] / max(stats['wins']) * 15)} {stats['wins'][i]}")
      print('\n')
    answer = input('Press ENTER to exit\n')
    scene = 'reset'

  # help screen with the tutorial text
  if scene == 'help':
    print(f"{clearScreen(colorify('WORDLE', 'green'))} console\n\nGuess the WORDLE in six tries.\n\nEach guess must be a valid five-letter word. Hit the enter button to submit.\n\nAfter each guess, the color of the tiles will change to show how close your guess was to the word.\n\n{colorify('W', 'green')}EARY\nThe letter W is in the word and in the correct spot.\nP{colorify('I', 'yellow')}LLS\nThe letter I is in the word but in the wrong spot.\nVAG{colorify('U', 'gray')}E\nThe letter U is not in the word in any spot.\n")
    answer = input('Press ENTER to continue\n')
    scene = 'reset'
    
  # settings screen
  if scene == 'settings':
    # unnecessary fstring go brrrrr
    print(f"{clearScreen(colorify('WORDLE', 'green'))} console\nSettings that are yellow when enabled are experimental\nand have not been thoroughly tested.\nEnable at your own risk.\n\n1 {colorify('block text', 'green' if settings['block text'] == True else 'gray')}\n2 {colorify('animation', 'yellow' if settings['animation'] == True else 'gray')}\n3 {colorify('keyboard', 'yellow' if settings['keyboard'] == True else 'gray')}\n4 exit")
    setting = input('\n> ')

    if setting == '1':
      settings['block text'] = not settings['block text']
      scene = 'settings'
    elif setting == '2':
      settings['animation'] = not settings['animation']
      scene = 'settings'
    elif setting == '3':
      settings['keyboard'] = not settings['keyboard']
      scene = 'settings'
    else:
      scene = 'reset'

  # you can start guessing
  if scene == 'guess':
    # after your sixth attempt, game is over
    if attempt > 5:
      time.sleep(0.5)
      print('\n  You failed.')
      time.sleep(0.5)
      print(f'  The corect word was {correctWord}')
      time.sleep(0.5)
      answer = input('\n  Restart? (Y/N)\n> ')
      if answer.upper() == 'Y':
        scene = 'reset'
      else:
        running = False
    # if you are on your sixth attempt or below
    else:
      # show keyboard if enabled
      if settings['keyboard'] == True:
        print(line(16) + '  ' + ''.join(keyboard[0:20]) + '\n   ' + ''.join(keyboard[20:38]) + '\n    ' + ''.join(keyboard[38:52]))
        
      guess = input(line(3 + attempt) + '> ')
      guessList = list(guess.upper())

      # S for settings screen
      if guess.upper() == 'S' and attempt == 0:
        scene = 'settings'
      # H for help screen
      elif guess.upper() == 'H' and attempt == 0:
        scene = 'help'
      # T for stats screen
      elif guess.upper() == 'T' and attempt == 0:
        scene = 'stats'
      # anything else is a guess
      else:
        # check if entry is five letters
        if len(list(guess)) == 5:
          # check if guess includes only letters
          if guess.isalpha() == True:
            # check if guess is a valid word
            if guess.lower() in wordles or guess.lower() in wordList:
              # if on first attempt clear screen to get rid of "Guess to start..." text
              if attempt == 0:
                print(line(6) + clear() + line(7) + clear() + line(3))
                stats['played'] += 1

              # increase attempt
              attempt += 1
              # check guess
              scene = 'result'
            # guess is not in the word list
            else:
              print(clear('  Not in word list'))
              time.sleep(0.5)
              print(clear())
          # guess has non-letters
          else:
            print(clear('  Letters only'))
            time.sleep(0.5)
            print(clear())
        # too little letters
        elif len(list(guess)) < 5:
          print(clear('  Not enough letters'))
          time.sleep(0.5)
          print(clear())
        # too much letters
        elif len(list(guess)) > 5:
          print(clear('  Too much letters'))
          time.sleep(0.5)   
          print(clear())

  # result screen to check guess
  if scene == 'result':
    # if the guess is correct
    if guessList == correctWordList:
      # if animation is enabled
      if settings['animation'] == True:
        # mark all letters as green
        for i in range(0, 5):
          returnList[i] = colorify(correctWordList[i], 'green', settings['block text'])
        # play animation
        for i in range(0, 5):
          print(clear('  ' + (''.join(returnList[0:i + 1]) + (''.join(guessList[i + 1:5])))))
          time.sleep(0.5)
      # if animation is disabled
      else:
        print(clear('  ' + colorify(''.join(guessList), 'green', settings['block text'])))
        time.sleep(0.5)

      # show game response based on number of attempts
      print(f'\n  {responses[attempt - 1]}\n')
      # add win to stats
      stats['wins'][attempt - 1] += 1
      time.sleep(0.5)
      answer = input('  Restart? (Y/N)\n> ')
      if answer.upper() == 'Y':
        scene = 'reset'
      else:
        running = False
    else:
      # first check for green (correct position and letter) and gray (not used at all) letters
      # for all the letters in the guess
      for i in range(0, 5):
        # if guess letter is in the correct word
        if guessList[i] in correctWordList:
          # if guess letter is in the correct position as well mark it green
          if guessList[i] == correctWordList[i]:
            returnList[i] = colorify(guessList[i], 'green', settings['block text'])
            keyboard = [colorify(guessList[i], 'green') if key == guessList[i] else key for key in keyboard]
            keyboard = [colorify(guessList[i], 'green') if key == colorify(guessList[i], 'yellow') else key for key in keyboard] # update yellow key to green
            # mark position as correct
            correctWordList[i] = ''
        # if the guess letter is not in correct word mark it gray
        else:
          returnList[i] = colorify(guessList[i], 'gray', settings['block text'])
          keyboard = [colorify(guessList[i], 'gray') if key == guessList[i] else key for key in keyboard]

      # second check for yellow (incorrect position) and gray (incorrect position but repeated) letters
      used = []
      # for all the letters in a word
      for i in range(0, 5):
        # exempt green letters
        if correctWordList[i] != '':
          # check if guess letter is in the word
          if guessList[i] in correctWordList:
            # if guess letter is in the word and has been used less than the amount it is used in the correct word mark it yellow
            if used.count(guessList[i]) < correctWordList.count(guessList[i]):
              returnList[i] = colorify(guessList[i], 'yellow', settings['block text'])
              keyboard = [colorify(guessList[i], 'yellow') if key == guessList[i] else key for key in keyboard] 
              # append letter to mark that it has been used and marked yellow
              used.append(guessList[i])
            # if guess letter is in the word but has been used more that the amount it is used in the correct word mark it gray
            else:
              returnList[i] =  colorify(guessList[i], 'gray', settings['block text'])
              keyboard = [colorify(guessList[i], 'gray') if key == guessList[i] else key for key in keyboard]
          # if guess letter is not used in the correct word mark it gray
          else:
            returnList[i] =  colorify(guessList[i], 'gray', settings['block text'])
            keyboard = [colorify(guessList[i], 'gray') if key == guessList[i] else key for key in keyboard]

      # if animation is enabled
      if settings['animation'] == True:
        for i in range(0, 5):
          print(clear('  ' + (''.join(returnList[0:i + 1]) + (''.join(guessList[i + 1:5])))))
          time.sleep(0.5)
      # if animation is disabled
      else:
        print(clear('  ' + ''.join(returnList)))

      # reset variables for next guess
      guess = ''
      returnList = list('     ')
      correctWordList = list(correctWord)
      scene = 'guess'