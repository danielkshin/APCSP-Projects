# Daniel Shin
# omok (aka 5-in-a-row)
# added themes cause bored (personal favorite: light mint)

# import module
import turtle

# set up window
turtle.title('omok (aka 5-in-a-row)')
turtle.setup(500, 550)
turtle.colormode(255)

# create and initialize turtles
lines = turtle.Turtle()
lines.hideturtle()
lines.pensize(1.5)
lines.speed(0)

turnText = turtle.Turtle()
turnText.hideturtle()
turnText.up()    
themeText = turnText.clone()

white = turtle.Turtle()
white.hideturtle()
white.speed(0)
white.shape('circle')
white.shapesize(1.25)
white.color('white')
white.up()
black = white.clone()
black.color('black')

# set variables
board = [[' '] * 17 for i in range(17)]
turn = 'Player one' # Player one = white, Player two = black
theme = 0
started = False
changing = False
themeColors = [['Goldenrod', 'black', 'black', 'white', 'classic'], [(23, 74, 69), (175, 184, 179),(252, 118, 106), (175, 184, 179), 'dark mint'], [(30, 30, 30), (215, 215, 215), (90, 90, 90), (215, 215, 215), 'dark'], [(225, 221, 191), (151, 176, 162), (76, 131, 122), (151, 176, 162), 'light mint'], [(241, 173, 136), (121, 57, 55), (121, 57, 55), (252, 106, 93), 'cherry'], [(253, 216, 190), (153, 119, 135), (227, 175, 177), (153, 119, 135), 'flowers']]

# write player turn
def turnWrite(turn, win):
  turnText.clear()
  if turn == 'Player one':
    turnText.color(themeColors[theme][3])
    turnText.goto(-200, 230)
    align = 'left'
  elif turn == 'Player two':
    turnText.color(themeColors[theme][2])
    turnText.goto(200, 230)
    align = 'right'
  if win == False:
    text = f'{turn}\'s turn'
  elif win == True:
    text = f'{turn} wins!'
  turnText.write(text, False, align, ('monospace', 10))

# check for exact five in a row no six, seven etc in a row
def check(b):
  for c in range(0, 48):
    for r in range(0, 48):
      # horizontal check
      if c < 11 and r < 15:
        s = b[r + 1][c] + b[r + 1][c + 1] + b[r + 1][c + 2] + b[r + 1][c + 3] + b[r + 1][c + 4] + b[r + 1][c + 5] + b[r + 1][c + 6]
      # vertical check
      elif c >= 11 and c < 26 and r >= 15 and r < 26:
        s = b[r - 15][c + 1 - 11] + b[r + 1 - 15][c + 1 - 11] + b[r + 2 - 15][c + 1 - 11] + b[r + 3 - 15][c + 1 - 11] + b[r + 4 - 15][c + 1 - 11] + b[r + 5 - 15][c + 1 - 11] + b[r + 6 - 15][c + 1 - 11]
      # diagonal check (NW to SE)
      elif c >= 26 and c < 37 and r >= 26 and r < 37:
        s = b[r - 26][c - 26] + b[r + 1 - 26][c + 1 - 26] + b[r + 2 - 26][c + 2 - 26] + b[r + 3 - 26][c + 3 - 26] + b[r + 4 - 26][c + 4 - 26] + b[r + 5 - 26][c + 5 - 26] + b[r + 6 - 26][c + 6 - 26]
      # diagonal check (NE to SW)
      elif c >= 37 and r >= 37:
        s = b[r + 6 - 37][c - 37] + b[r + 5 - 37][c + 1 - 37] + b[r + 4 - 37][c + 2 - 37] + b[r + 3 - 37][c + 3 - 37] + b[r + 2 - 37][c + 4 - 37] + b[r + 1 - 37][c + 5 - 37] + b[r - 37][c + 6 - 37]
      # if exact five-in-a-row
      if s == ' wwwww ' or s == 'bwwwww ' or s == ' wwwwwb' or s == 'bwwwwwb':
        return 'white'
        break
      elif s == ' bbbbb ' or s == 'wbbbbb ' or s == ' bbbbbw' or s == 'wbbbbbw':
        return 'black'
        break

# change theme
def themeChange(theme):
  # change theme text and color at bottom right
  themeText.clear()
  themeText.color(themeColors[theme][3])
  themeText.goto(210, -250)
  themeText.write(f'omok {themeColors[theme][4]}', False, 'right', ('monospace', 15))
  themeText.goto(210, -260)
  themeText.write('(click here to change)', False, 'right', ('monospace', 8))
  # change turn text
  turnWrite('Player one', False)
  # clear lines and redraw with theme colors
  lines.clear()
  turtle.bgcolor(themeColors[theme][0])
  lines.pencolor(themeColors[theme][1])
  black.color(themeColors[theme][2])
  white.color(themeColors[theme][3])
  lines.setheading(0)
  for row in range(0, 15):
    lines.up()
    lines.goto(-210, row * 30 - 210)
    lines.down()
    lines.forward(420)
  lines.setheading(90)
  for column in range(0, 15):
    lines.up()
    lines.goto(column * 30 - 210, -210)
    lines.down()
    lines.forward(420)

# place stones
def place(x, y):
  global theme
  global started
  global changing
  # prevent clicking when theme changing
  if changing == False:
    # prevent placing outside border
    if x > -220 and x < 220 and y > -220 and y < 220:
      started = True
      global turn
      themeText.clear()
      # get stone position and row and column from it
      placex, placey = round(x / 30) * 30, round(y / 30) * 30
      row, column = int(abs(placey - 210) / 30), int((placex + 210) / 30)
      # check if board position is empty in array
      if(board[row + 1][column + 1] == ' '):
        if turn == 'Player one':
          turn = None
          # replace space in board position with "stone"
          board[row + 1][column + 1] = 'w'
          # visually stamp the turtle in the position
          white.goto(placex, placey)
          white.stamp()
          # check if player got 5-in-a-row
          if(check(board) == 'white'):
            turnWrite('Player one', True)
          else:
            turnWrite('Player two', False)
            turn = 'Player two'
        elif turn == 'Player two':
          turn = None
          # replace space in board position with "stone"
          board[row + 1][column + 1] = 'b'
          # visually stamp the turtle in the position
          black.goto(placex, placey)
          black.stamp()
          # check if player got 5-in-a-row
          if(check(board) == 'black'):
            turnWrite('Player two', True)
          else:
            turnWrite('Player one', False)
            turn = 'Player one'
    # change theme if clicked in that area
    elif x > 20 and x < 220 and y < -230:
      # to prevent changing themes when game started
      if started == False:
        changing = True
        theme += 1
        if theme > len(themeColors) - 1:
          theme = 0
        themeChange(theme)
        changing = False

# create lines for rows and columns
themeChange(theme)

turtle.Screen().onclick(place)
turtle.Screen().mainloop()