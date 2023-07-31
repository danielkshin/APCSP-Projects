# Omok (aka 5-in-a-row)

# import module
import turtle

# set up window
turtle.title('Turtle Gomoku')
turtle.setup(500, 550)
turtle.bgcolor('Goldenrod')

# create turtles
lines = turtle.Turtle()
lines.hideturtle()
lines.speed(0)

turnText = turtle.Turtle()
turnText.hideturtle()
turnText.up()    

white = turtle.Turtle()
white.hideturtle()
white.speed(0)
white.shape('circle')
white.shapesize(1.25)
white.color('white')
white.up()

black = white.clone()
black.color('black')

board = [[' '] * 17 for i in range(17)]
turn = 'white'

# write player turn
def turnWrite(turn, win):
  turnText.clear()
  turnText.color(turn)
  if turn == 'white':
    turnText.goto(-200, 230)
    align = 'left'
  elif turn == 'black':
    turnText.goto(200, 230)
    align = 'right'
  if win == False:
    text = f'{turn}\'s turn'
  elif win == True:
    text = f'{turn} wins!'
  turnText.write(text, False, align, ('monospace', 10))

# check for exact five in a row (not fully optimized)
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

# place stones
def place(x, y):
  # prevent placing outside border
  if x > -220 and x < 220 and y > -220 and y < 220:
    global turn
    placex, placey = round(x / 30) * 30, round(y / 30) * 30
    row, column = int(abs(placey - 210) / 30), int((placex + 210) / 30)
    if(board[row + 1][column + 1] == ' '):
      if turn == 'white':
        turn = None
        board[row + 1][column + 1] = 'w'
        white.goto(placex, placey)
        white.stamp()
        if(check(board) == 'white'):
          turnWrite('white', True)
        else:
          turnWrite('black', False)
          turn = 'black'
      elif turn == 'black':
        turn = None
        board[row + 1][column + 1] = 'b'
        black.goto(placex, placey)
        black.stamp()
        if(check(board) == 'black'):
          turnWrite('black', True)
        else:
          turnWrite('white', False)
          turn = 'white'

# create lines for rows and columns
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

turnWrite('white', False)

turtle.Screen().onclick(place)
turtle.Screen().mainloop()
