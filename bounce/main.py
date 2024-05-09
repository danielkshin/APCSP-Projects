 # Daniel Shin
# Final Project: bounce!

# import necessary modules
import pygame
from random import randint

# initialize pygame, window, and clock
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('bounce!')
clock = pygame.time.Clock()

# theme and colors
theme = 0
themeColors = [[(25, 75, 75), (250, 120, 105), (175, 185, 180)], [(225, 221, 191), (151, 176, 162), (76, 131, 122)], [(253, 216, 190), (227, 175, 177), (153, 119, 135)], [(241, 173, 136), (252, 106, 93), (121, 57, 55)], [(30, 30, 30), (215, 215, 215), (90, 90, 90)]]

# pipe class
class pipe():
  def __init__(this, x):
    this.pipex = x
    this.reset()

  # draw pipe
  def display(this):
    pygame.draw.rect(screen, this.pipeColor, (this.x, 0, this.w, this.h))
    pygame.draw.rect(screen, this.pipeColor, (this.x, this.space + this.h, this.w, this.h + 500))
    this.x -= this.xv

    # reset pipe position and random space/height
    if this.x + this.w < 0:
      this.h = randint(110, 290)
      this.space = randint(150, 200)
      this.x = 500

  # stop pipe when player dies
  def death(this):
    this.xv = 0
  
  # reset pipe
  def reset(this):
    this.x = this.pipex
    this.xv = 1
    this.w = 75
    this.h = randint(110, 290)
    this.space = randint(150, 200)
    this.pipeColor = themeColors[theme][2]

# ball class (player)
class ball():
  def __init__(this):
    this.reset()

  # draw ball
  def display(this):
    pygame.draw.circle(screen, this.ballColor, (this.x, this.y), this.s)
  
  # start and move ball
  def start(this):
    if mouse['clicked'] == True and this.death == False and this.yv > 0:
      this.yv = -7

    this.y += this.yv 
    this.yv += this.g

    # boundaries
    if this.y < 100:
      this.yv = 0
      this.y = 100
  
    if this.y > 480:
      this.y = 480

  # reset ball
  def reset(this):
    this.x = 250
    this.y = 250
    this.xv = 0
    this.yv = -7
    this.g = 0.3
    this.s = 20
    this.sv = 5
    this.death = False
    this.ballColor = themeColors[theme][1]

  # collision with pipe
  def collision(this, pipes):
    global scene

    for pipe in pipes:
      # update score if pipe passes player
      if pipe.x == 150:
        scoreCounter.update()

      # player collides with pipe results in death
      if this.x + this.s > pipe.x and this.x - this.s < pipe.x + pipe.w and (this.y - this.s < pipe.h or this.y + this.s > pipe.h + pipe.space):
        this.death = True
      if this.death == True:
        pipe.death() 

    # start death animation
    if this.death == True:
      this.g = 0
      this.yv = 0
      this.s += this.sv
      this.sv *= 1.25
      scoreCounter.death = True
      restartText.display()

    # click to restart
    if this.s >= 600:
      this.sv = 0
      this.s = 600
      if mouse['clicked'] == True:
        this.reset() 
        scene = 'ready'

# score counter class
class score():
  def __init__(this):
    this.reset()

  # draw score counter
  def display(this):
    textScore = pygame.font.SysFont(None, int(this.s)).render(str(this.score), True, this.textColor)
    text_rect = textScore.get_rect(center=(this.x, this.y))
    screen.blit(textScore, text_rect)

    # scored animation
    if this.scored == True:
      this.s += this.sv
    if this.s > 100:
      this.scored = False
      this.s = 75

    # death animation
    if this.death == True:
      this.textColor = themeColors[theme][2]
      this.y += this.yv
      this.yv *= 0.9
      this.s += this.sv
      this.sv *= 0.9

      if this.sv < 0.1:
        this.yv = 0
        this.sv = 0

  # update score by adding one
  def update(this):
    this.score += 1
    this.scored = True

  # reset score counter
  def reset(this):
    this.score = 0
    this.x = 250
    this.y = 50
    this.yv = 20
    this.s = 75
    this.sv = 2.5
    this.scored = False
    this.death = False
    this.textColor = themeColors[theme][1]

# bouncing text class
class bounceText():
  def __init__(this, text, x, y, by, s, textAlign, textColorTheme):
    this.x = x
    this.oy = y
    this.by = by
    this.s = s
    this.text = text
    this.textAlign = textAlign
    this.textColorTheme = textColorTheme
    this.reset()
  
  # draw bouncing text
  def display(this):
    text = pygame.font.SysFont(None, this.s).render(this.text, True, themeColors[theme][this.textColorTheme])
    if this.textAlign == 'right':
      textRect = text.get_rect(right = this.x, bottom = this.y)
    elif this.textAlign == 'center':
      textRect = text.get_rect(centerx = this.x, bottom = this.y)
    screen.blit(text, textRect)

    this.y += this.yv
    this.yv += this.g

    if this.y > this.by:
      this.bounce += 1
      this.yv *= -0.5

    if this.bounce > 1:
      this.yv = 0
      this.y = this.by
  
  # reset bouncing text
  def reset(this):
    this.y = this.oy
    this.yv = 3
    this.g = 0.3
    this.bounce = 0

# create objects using class
titleText = bounceText('b   unce!', 460, 0, 281, 100, 'right', 1)
startText = bounceText('click to start', 455, -20, 300, 25, 'right', 1)
tipText = bounceText('tip: right-click to change theme!', 480, 25, 485, 20, 'right', 2)
restartText = bounceText('click to restart', 250, -10, 300, 25, 'center', 2)
scoreCounter = score()
pipe1 = pipe(500)
pipe2 = pipe(787)
player = ball()

# for mouse interaction
mouse = {
  'stop': False,
  'pressed': False,
  'clicked': False,
  'type': None
}

# game scene and other variables
scene = 'intro'
quit = False
introAlpha = -100

# run while the user does not quit 
while quit == False:
  # if user quits and mouse interactions
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse['pressed'] = True
      mouse['type'] = event.button
    if event.type == pygame.MOUSEBUTTONUP:
      mouse['type'] = None
      mouse['stop'] = False
      mouse['pressed'] = False

  if mouse['pressed'] == True and mouse['stop'] == False:
    mouse['clicked'] = True
    mouse['stop'] = True
  else:
    mouse['clicked'] = False

  # intro scene
  if scene == 'intro':
    screen.fill((0, 0, 0))
    text = pygame.font.SysFont(None, 50).render('created by daniel shin', True, (255, 255, 255))
    text.set_alpha(introAlpha)
    textRect = text.get_rect(centerx = 250, centery = 250)
    screen.blit(text, textRect)

    # fade in animation
    introAlpha += 5
    if introAlpha > 750:
      scene = 'ready'

  # ready to play scene
  if scene == 'ready':
    screen.fill(themeColors[theme][0])
    pipe1.reset()
    pipe2.reset()
    scoreCounter.reset()
    restartText.reset()
    startText.display()
    titleText.display()
    tipText.display()
    player.display()

    if mouse['clicked'] == True:
      # right click changes theme
      if mouse['type'] == 3:
        theme += 1
        if theme > len(themeColors) - 1:
          theme = 0
        pipe1.reset()
        pipe2.reset()
        scoreCounter.reset()
        player.reset()
      # other click starts game
      else:
        scene = 'start'

  # game start scene
  if scene == 'start':
    titleText.reset()
    startText.reset()
    tipText.reset()
    screen.fill(themeColors[theme][0])
    pipe1.display()
    pipe2.display()
    player.display()
    player.start()
    player.collision([pipe1, pipe2])
    scoreCounter.display()

  # display game and set clock at 60 fps
  pygame.display.flip()
  clock.tick(60)