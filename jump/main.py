# Daniel Shin and Daniel Kim
# Project: jump!
# a simple game with a simple mechanic for a simple objective: hold and release for a high score

# import necessary modules
import pygame
from random import randrange, choice

# initialize pygame, window, and clock
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('jump!')
clock = pygame.time.Clock()

# theme index
theme = 0

# light platform, dark platform, player, death area, background, bonus platform
themeColors = [[(177, 201, 188), (150, 179, 163), (128, 166, 160), (76, 131, 122), (225, 221, 191), (245, 165, 149)], [(253, 216, 190), (255, 191, 145), (227, 175, 177), (153, 119, 135), (255, 237, 238), (255, 220, 130)], [(177, 188, 201), (
150, 164, 179), (128, 142, 166), (76, 99, 131), (191, 207, 225), (108, 173, 145)], [(160, 160, 160), (140, 140, 140), (100, 100, 100), (50, 50, 50), (180, 180, 180), (215, 215, 215)]]

# score counter class
class score():
  def __init__(this):
    this.reset()

  # display counter
  def display(this):
    textScore = pygame.font.SysFont(None, int(this.s)).render(str(this.score), True, this.textColor)
    textScoreRect = textScore.get_rect(center=(this.x, this.y))
    screen.blit(textScore, textScoreRect)

    # bonus score color change and bonus text
    if this.bonusShow == True:
      textBonus = pygame.font.SysFont(None, int(this.s / 3)).render(f'{this.bonusText}! +{this.scoreAdd}', True, this.textColor)
      textBonusRect = textBonus.get_rect(center=(this.x, this.y + this.s / 2))
      screen.blit(textBonus, textBonusRect)

    # scored animation
    if this.scored == True:
      this.s += this.sv
    if this.s > 100:
      this.scored = False
      this.s = 75

    # death animation
    if this.death == True:
      this.bonusShow = False
      this.textColor = themeColors[theme][3]
      this.y += this.yv
      this.yv *= 0.9
      this.s += this.sv
      this.sv *= 0.9

      if this.sv < 0.1:
        this.yv = 0
        this.sv = 0
  
  # update score
  def update(this):
    if this.bonus == True:
    # double bonus points added if bonus
      this.bonusShow = True
      this.bonusText = choice(this.bonusTexts)
      this.textColor = themeColors[theme][5]
      this.scoreAdd *= 2
    # add one point if no bonus
    else:
      this.bonusShow = False
      this.textColor = themeColors[theme][3]
      this.scoreAdd = 1
    this.score += this.scoreAdd
    this.scored = True

  # reset score counter
  def reset(this):
    this.score = 0
    this.scoreAdd = 1
    this.x = 250
    this.y = 50
    this.yv = 20
    this.s = 75
    this.sv = 2.5
    this.scored = False
    this.death = False
    this.bonus = False
    this.bonusShow = False
    this.bonusText = ''
    this.bonusTexts = ['nice', 'magnificent', 'great', 'good', 'noice']
    this.textColor = themeColors[theme][3]

# box player class
class box():
  def __init__(this):
    this.reset()

  # display box
  def display(this):
    box = pygame.Rect(0, 0, this.w, this.h)
    box.centerx = this.x
    box.bottom = this.y
    pygame.draw.rect(screen, themeColors[theme][2], box)

    # physics
    this.y += this.yv
    this.yv += this.g

    # display restart text if player dies
    if this.death == True:
      restart.display()

  # player collision
  def collision(this, platform):
    global scene
    for p in platform:
      # let player die if it hits the death boundary
      if this.y > 375:
        this.death = True
        this.jumping = False
        this.yv = 2
        scoreCounter.death = True

      # click to restart game
      if this.y > 450 and mouse['clicked'] == True:
          plat1.reset()
          plat2.reset()
          scoreCounter.reset()
          this.reset()
          scene = 'ready'

      # if the player lands on the platform
      if this.y > p.y - p.h and this.x - 25 < p.x + p.w / 2 and this.x + 25 > p.x - p.w / 2:
        # if the player is near the center of the platform give bonus
        if this.x - 25 > p.x - 40 and this.x + 25 < p.x + 40 and p.landed == 0:
          p.bonus = True
          scoreCounter.bonus = True
        else:
          scoreCounter.bonus = False

        # player land on platform
        this.y = p.y - p.h

        # update score if player lands
        if this.yv < 23 and this.death == False:
          if this.jumping == True:
            if p.landed < 1:
              scoreCounter.update()
            else:
              this.platFall = True
            p.landed += 1
          this.jumping = False
        else:
          # if player hits left side of platform
          if p.landed < 1:
            p.x = this.x + 25 + p.w / 2
            p.xv = 0

      # move the platforms if the player is jumping
      if this.jumping == True:
        this.g = 1
        p.xv = this.p
      else:
        this.g = 0
        p.xv = 0

  # player interaction
  def interaction(this):
    # if mouse is held
    if mouse['pressed'] == True:
      if this.platFall == False and this.jumping == False and this.death == False:
        if this.h >= 30 and this.w <= 70 and this.t <= 50:
          this.h -= 0.2
          this.w += 0.2
          this.t += 0.5
          
    # if mouse is released
    if mouse['pressed'] == False:
      this.h = 50
      this.w = 50
      if this.t > 0:
        this.jump = True
        this.jumping = True
        this.p = this.t / 4
        this.t = 0

    # player jump
    if this.jump == True:
      this.yv = -20
      this.jump = False      

  # reset player
  def reset(this):
    this.x = 125
    this.y = 350
    this.w = 50
    this.h = 50
    this.t = 0
    this.p = 0
    this.yv = 0
    this.g = 1
    this.jump = False
    this.jumping = False
    this.platFall = False
    this.death = False

# platform class
class platform():
  def __init__(this, x, landed):
    this._x = x
    this.w = randrange(70, 120, 5)
    this._landed = landed
    this.reset()

  # display platforms
  def display(this):
    platform = pygame.Rect(0, 0, this.w, this.h)
    platform.centerx = this.x
    platform.bottom = this.y
    pygame.draw.rect(screen, this.color, platform)

    # physics
    this.x -= this.xv
    this.y += this.yv

    # raise platform
    if this.h < this.oh:
      this.h += 1

    # deny player from landing on platform twice
    if this.landed == 1:
      this.color = themeColors[theme][1]
    elif this.landed > 1:
      this.yv = 3

    # platform bonus color
    if this.bonus == True:
      this.color = themeColors[theme][5]
      
    # regenerate platforms if it is out of the screen
    if this.x + this.w / 2 < 0:
      if this.xv == 0:
        this.landed = 0
        this.y = 375
        this.yv = 0
        this.color = themeColors[theme][0]
        this.w = randrange(70, 120, 5)
        this.x = randrange(400, 490, 10)
        this.h = 0
        this.bonus = False

  # reset platform
  def reset(this):
    this.y = 375
    this.x = this._x
    this.oh = 25
    this.h = 25
    this.xv = 0
    this.yv = 0
    this.color = themeColors[theme][0]
    this.bonus = False
    this.landed = this._landed

# jumping text
class jumpText():
  def __init__(this, text, x, y, s, textColorTheme):
    this.x = x
    this.oy = y
    this.yv = 0
    this.s = s
    this.text = text
    this.textColorTheme = textColorTheme
    this.reset()

  # display jumping text
  def display(this):
    text = pygame.font.SysFont(None, this.s).render(this.text, True, themeColors[theme][this.textColorTheme])
    textRect = text.get_rect(centerx = this.x, bottom = this.y)
    screen.blit(text, textRect)

    this.y += this.yv
    this.yv += this.g
    this.t += 1

    if this.y > this.oy:
      this.y = this.oy

    # jump at a random time and a random height
    if this.t > randrange(100, 150):
      this.yv = -randrange(7, 10)
      this.t = 0

  # reset jumping text
  def reset(this):
    this.y = this.oy
    this.g = 0.5
    this.t = 200

# jumping texts
title = jumpText('jump!', 250, 175, 75, 3)
click = jumpText('hold and release to start', 250, 200, 20, 3)
restart = jumpText('click to restart', 250, 300, 25, 1)

# create objects
player = box()
plat1, plat2 = platform(125, 1), platform(375, 0)
scoreCounter = score()

# game scene
scene = 'intro'
introAlpha = 0
quit = False

# mouse interaction variables
mouse = {
  'stop': False,
  'clicked': False,
  'pressed': False,
  'type': None
}

# run while the program is not quit
while quit == False:
  # if user quits or mouse interactions
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

  # intro
  if scene == 'intro':
    screen.fill((0, 0, 0))
    text = pygame.font.SysFont(None, 40).render('created by daniel shin & kim', True, (255, 255, 255))
    text.set_alpha(introAlpha)
    textRect = text.get_rect(centerx = 250, centery = 250)
    screen.blit(text, textRect)

    # fade in animation
    introAlpha += 5
    if introAlpha > 750:
      scene = 'ready'

  # ready to start
  if scene == 'ready':
    screen.fill(themeColors[theme][4])
    title.display()
    click.display()
    restart.reset()
    pygame.draw.rect(screen, themeColors[theme][3], (0, 375, 500, 250))
    text = pygame.font.SysFont(None, 20).render('tip: right-click to change theme!', True, themeColors[theme][0])
    textRect = text.get_rect(right = 480, bottom = 485)
    screen.blit(text, textRect)
    player.display()
    player.collision([plat1, plat2])
    plat1.display()
    plat2.display()

    if mouse['clicked'] == True:
      # right click changes theme
      if mouse['type'] == 3:
        theme += 1
        if theme > len(themeColors) - 1:
          theme = 0
        plat1.reset()
        plat2.reset()
        scoreCounter.reset()
        player.reset()
      # other click starts game
      else:
        scene = 'start'

  # start game
  if scene == 'start':
    title.reset()
    click.reset()

    screen.fill(themeColors[theme][4])
    scoreCounter.display()
    pygame.draw.rect(screen, themeColors[theme][3], (0, 375, 500, 250))
    
    player.display()
    player.collision([plat1, plat2])
    plat1.display()
    plat2.display()
    player.interaction()
    
  # display game and set clock at 60 fps
  pygame.display.flip()
  clock.tick(60)