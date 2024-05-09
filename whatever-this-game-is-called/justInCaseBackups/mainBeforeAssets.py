import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

script = {
  "tutorial": [
    ("Welcome to whatever this game is called\nTry pressing the SPACE key to continue...", "?"),
    ("Now if you hold the SPACE key down\nyou can speed the text up\nNeat, eh?", "?"),
    ("By the way, my name is Tori\nbecause the only reason I exist is to\ngive you this tutorial", "Tori"),
    ("You can also use the UP and DOWN keys\nto choose an option if presented with choices\nGot it?", "Tori"),
    ([
      ("yeah", "tutorialY"),
      ("no", "tutorialN"),
      ("kinda...", "tutorialN")
    ], "Tori"),
  ],
  "tutorialN": [
    ("Let's try resetting.\nLooks like you need to rewind a bit...", "Tori"),
    ("script", "tutorial")
  ],
  "tutorialY": [
    ("Nice, you got it!", "Tori"),
    ("Now without further ado,\nhere is your typical anime dating sim...\n(By the way say hi to my friend\nNarry, the narrator)", "Tori"),
    ("script", "s_0")
  ],
  "s_0": [
    ("I-I have a crush on you Ari!", "Daisuke"), 
    ("Please go out with me!", "Daisuke"), 
    ("Here we have a pathetic attempt\nof a confession to the girl, Ari.", "Narry"),
    ("The man, Daisuke, has finally mustered up\nthe courage to ask her out,\nonly for it to fold out like this.", "Narry"),
    ("I-I’m sorry Daisuke-san,\nbut I cannot accept your confession…\n>///<", "Ari"),
    ([
      ("My apologies, sorry for taking up your time.", "s_1"), 
      ("Please consider again I’m begging you…", "s_2"), 
      ("Could I ask why?", "s_3"), 
      ("WHAT NOOOOOOOOOOOOOOOO", "s_4")
    ], "Daisuke")
  ],
  "s_1": [
    ("Thank you for being so understanding.\nI’m sure one of my friends might like\na guy like you…", "Ari"),
    ([
      ("Oh no that's ok, I was only interested in you.", "s_1_1"), 
      ("Who might that be?", "s_1_2"), 
    ], "Daisuke")
  ],
  "s_1_1": [
    ("If that’s all you need to say to me,\nI’ll be heading back home now.", "Ari"),
    ("Ah ok, I’ll see you at school tomorrow,\nplease act like this didn’t happen at all.", "Daisuke"),
    ("(Well I guess it was worth a shot,\nthere's plenty of fish in the sea after all…)", "Daisuke"),
    ("The defeated Daisuke heads home in solitude,\nperforming coping mechanisms\nto himself along the way.", "Narry"),
    ("GENTLEMAN ENDING", "Ending"),
    ("script", "s_0")
  ],
  "s_1_2": [
    ("She’s in class 3-A and her name is Yukino,\nshe’s had a crush on you for a while.", "Ari"),
    ("Oh well…", "Daisuke"),
    ([
      ("I’ve never heard about her before\nso I’ll have to refuse.", "s_1_2_1"), 
      ("Oh I think she’s in the same club as me.", "s_1_2_2"), 
    ], "Daisuke"),
    ("script", "s_0")
  ],
  "s_1_2_1": [
    ("Oh what a shame…\nI was hoping you two could become close.", "Ari"),
    ("Now if you’ll excuse me I need to leave now.\nThe bus is almost here.", "Ari"),
    ("The defeated Daisuke heads home in solitude,\nmissing his second chance at love…", "Narry"),
    ("NO BITCHES ENDING", "Ending"),
    ("script", "s_0")
  ],
  "s_1_2_2": [
    ("Oh so you do know her,\nthat’s a relief…", "Ari"),
    ("Expect something soon Daisuke…\nI’m rooting for you!", "Ari"),
    ("W-wait!\nWhat do you mean by that!", "Daisuke"),
    ("Ari prances away, leaving Daisuke alone\nto contemplate what just happened to him.", "Narry"),
    ("CLIFFHANGER ENDING\n(or part 2 apparently)", "Ending"),
    ("script", "s_0")
  ],
  "s_2": [
    ("you have arrived to s2", "null"),
    ("script", "s_0")
  ],
  "s_3": [
    ("you have arrived to s3", "null"),
    ("script", "s_0")
  ],
  "s_4": [
    ("HOW COULD YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "Daisuke"),
    ("KYYYAAAAAAAHHHHH!!!", "Ari"),
    ("*runs away*", "Ari"),
    ("*furiously crying*", "Daisuke"),
    ("The defeated Daisuke is later arrested for being\na public nuisance and later sent to a\nmental asylum, never to be heard from again.", "Narry"),
    ("EMOTIONAL DAMAGE ENDING", "Ending"),
    ("script", "s_0")
  ]
}

keys = {
  'space': {
    'pressed': False,
    'pressing': False,
    'stop': False
  },
  'up': {
    'pressed': False,
    'pressing': False,
    'stop': False
  },
  'down': {
    'pressed': False,
    'pressing': False,
    'stop': False
  },
  'enter': {
    'pressed': False,
    'pressing': False,
    'stop': False
  }  
}

text = []

gameScene = 'game'
scriptIndex = 0
textIndex = 0
textSpeed = 0.2
optionSelected = 0
currentScript = 'tutorial'
font = pygame.font.SysFont(None, 30)
speakerColor = (0, 0, 0)

while True:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.KEYDOWN:
      if pygame.key.name(event.key) in ('up', 'down', 'space', 'enter'):
        keys[pygame.key.name(event.key)]['pressing'] = True
    if event.type == pygame.KEYUP:
      if pygame.key.name(event.key) in ('up', 'down', 'space', 'enter'):
        keys[pygame.key.name(event.key)]['pressing'] = False
        keys[pygame.key.name(event.key)]['stop'] = False

  for key in keys:
    if keys[key]['pressing'] == True and keys[key]['stop'] == False:
      keys[key]['pressed'] = True
      keys[key]['stop'] = True
    else:
      keys[key]['pressed'] = False

  #if gameScene == 'endings':
    
  if gameScene == 'game':
    screen.fill((255, 255, 255))
  
    if script[currentScript][scriptIndex][1] == 'Tori' or script[currentScript][scriptIndex][1] == 'Narry':
      speakerColor = (100, 255, 100)
    elif script[currentScript][scriptIndex][1] == 'Daisuke':
      speakerColor = (150, 150, 255)
    elif script[currentScript][scriptIndex][1] == 'Ari':
      speakerColor = (255, 150, 150)
    else:  
      speakerColor = (100, 150, 150)
      
    speakerR = pygame.Rect(0, 0, 100, 30)
    speakerR.centerx = 250
    speakerR.bottom = 365
    pygame.draw.rect(screen, speakerColor, speakerR)
  
    pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(0, 365, 500, 135))
  
    speaker = font.render(script[currentScript][scriptIndex][1], True, (0, 0, 0))
    speakerRect = speaker.get_rect(centerx = 250, centery = 352)
  
    
    h = font.get_height() * 1.35
    for i in range(len(text)):
      dialogue = font.render(text[i], True, (0, 0, 0))
      dialogueRect = dialogue.get_rect(centerx = 250, top = 380 + i * h)
      screen.blit(dialogue, dialogueRect)
    screen.blit(speaker, speakerRect)
  
    if type(script[currentScript][scriptIndex][0]) == list:
      if optionSelected > len(script[currentScript][scriptIndex][0]) - 1:
        optionSelected = 0
      elif optionSelected < 0:
        optionSelected = len(script[currentScript][scriptIndex][0]) - 1
  
      text = []
      
      if len(text) < len(script[currentScript][scriptIndex][0]): #and keys['space']['pressed'] == False:
        for i in range(0, len(script[currentScript][scriptIndex][0])):
          text.extend(f'> {script[currentScript][scriptIndex][0][i][0]} <'.split('\n') if optionSelected is i else script[currentScript][scriptIndex][0][i][0].split('\n'))
      
      if keys['up']['pressed'] == True:
        optionSelected -= 1
      elif keys['down']['pressed'] == True:
        optionSelected += 1
      elif keys['space']['pressed'] == True:
        currentScript = script[currentScript][scriptIndex][0][optionSelected][1]
        scriptIndex = 0
        optionSelected = 0
      
    else:
      text = script[currentScript][scriptIndex][0][0:math.floor(textIndex)].split('\n')
  
      if keys['space']['pressing'] == True:
        textSpeed = 0.6 
      else:
        textSpeed = 0.3
      
      if keys['space']['pressed'] == True and textIndex > len(script[currentScript][scriptIndex][0]):
        scriptIndex += 1
        textIndex = 0
  
      textIndex += textSpeed
  
      if script[currentScript][scriptIndex][0] == 'script':
          currentScript = script[currentScript][scriptIndex][1]
          scriptIndex = 0

  pygame.display.flip()
  clock.tick(60)