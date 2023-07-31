# Gomoku (5-in-a-row)

# import module
import turtle

debug = True

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
white.speed(0)
white.shape('circle')
white.shapesize(1.25)
white.color('white')
white.up()
white.hideturtle()

black = white.clone()
black.color('black')

board = [[' '] * 15 for i in range(15)]
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
    text = turn + '\'s turn'
  elif win == True:
    text = turn + ' wins!'

  turnText.write(text, False, align, ('monospace', 10))

# check for five in a row
def check(b):
  for c in range(0, 48):
    for r in range(0, 48):
      if c < 11 and r < 15:
        s = b[r][c] + b[r][c + 1] + b[r][c + 2] + b[r][c + 3] + b[r][c + 4]
      elif c >= 11 and c < 26 and r >= 15 and r < 26:
        s = b[r - 15][c - 11] + b[r + 1 - 15][c - 11] + b[r + 2 - 15][c - 11] + b[r + 3 - 15][c - 11] + b[r + 4 - 15][c - 11]
      elif c >= 26 and c < 37 and r >= 26 and r < 37:
        s = b[r - 26][c - 26] + b[r + 1 - 26][c + 1 - 26] + b[r + 2 - 26][c + 2 - 26] + b[r + 3 - 26][c + 3 - 26] + b[r + 4 - 26][c + 4 - 26]
      elif c >= 37 and r >= 37:
        s = b[r + 4 - 37][c - 37] + b[r + 3 - 37][c + 1 - 37] + b[r + 2 - 37][c + 2 - 37] + b[r + 1 - 37][c + 3 - 37] + b[r - 37][c + 4 - 37]

      if s == 'wwwww':
        return 'white'
        break
      elif s == 'bbbbb':
        return 'black'
        break
      
  '''
  # horizontal check
  for c in range(0, 11):
    for r in range(0, 15):
      s = b[r][c] + b[r][c + 1] + b[r][c + 2] + b[r][c + 3] + b[r][c + 4]

      if s == 'wwwww':
        return 'white'
        break
      elif s == 'bbbbb':
        return 'black'
        break
  
  # vertical check
  for c in range(0, 15):
    for r in range(0, 11):
      s = b[r][c] + b[r + 1][c] + b[r + 2][c] + b[r + 3][c] + b[r + 4][c]

      if s == 'wwwww':
        return 'white'
        break
      elif s == 'bbbbb':
        return 'black'
        break

  # diagonal check
  for r in range(0, 11):
    for c in range(0, 11):
      s = b[r][c] + b[r + 1][c + 1] + b[r + 2][c + 2] + b[r + 3][c + 3] + b[r + 4][c + 4]

      if s == 'wwwww':
        return 'white'
        break
      elif s == 'bbbbb':
        return 'black'
        break

  for r in range(0, 11):
    for c in range(0, 11):
      s = b[r + 4][c] + b[r + 3][c + 1] + b[r + 2][c + 2] + b[r + 1][c + 3] + b[r][c + 4]

      if s == 'wwwww':
        return 'white'
        break
      elif s == 'bbbbb':
        return 'black'
        break
  '''

# place stones
def place(x, y):
  # prevent placing outside border
  if x > -220 and x < 220 and y > -220 and y < 220:
    global turn
    placex = round(x / 30) * 30
    placey = round(y / 30) * 30
    row = int(abs(placey - 210) / 30)
    column = int((placex + 210) / 30)

    if debug == True:
      print('\nturn = ' + str(turn))
      print('mousePos = (' + str(x) + ', ' + str(y) + ')')
      print('placePos = (' + str(placex) + ', ' + str(placey) + ')')
      print('row = ' + str(row))
      print('column = ' + str(column))

    if(board[row][column] == ' '):
      if turn == 'white':
        board[row][column] = 'w'
        white.goto(placex, placey)
        white.stamp()
        turn = None # prevent user from placing multiple times by clicking fast

        if(check(board) == 'white'):
          turnWrite('white', True)
        else:
          turnWrite('black', False)
          turn = 'black'
      elif turn == 'black':
        board[row][column] = 'b'
        black.goto(placex, placey)
        black.stamp()
        turn = None # prevent user from placing multiple times by clicking fast

        if(check(board) == 'black'):
          turnWrite('black', True)
        else:
          turnWrite('white', False)
          turn = 'white'
    else:
      if debug == True:
        print('stone exists')
    if debug == True:
      print('winner = ' + str(check(board)))
  else:
    if debug == True:
      print('mouse out of bounds')

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
