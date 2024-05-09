import pygame
import math
import os

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# WAIT THE PHEONIX WRIGHT SPITS ARE SO GENIUS THEY ALREADY ARE ANIMATED FOR US
# yeah I guess

# the game script
script = {
  "PheonixTest": [
    {
      "script": "(Hmmm... that doesn't sound right)", 
      "character": "Pheonix", 
      "type": "normal",
      "background": "court"
    },
    {
      "script": "(If I refer to Larry's statement back\nwhen I was at the school...)",
      "background": "school"
    },
    {
      "script": "(Something seems off...)"
    },
    {
      "script": "(Should I raise an objection?...)",
      "background": "court"
    },
    {
      "script": [
        ("Raise an objection", "PheonixObject"),
        ("Objection!!!", "PheonixObject"),
        ("There's definitely a contradiction", "PheonixObject")
      ], 
    }    
  ],
  "PheonixObject": [
    {
      "script": "OBJECTION!!!",
      "type": "point"
    },
    {
      "script": "There is definitely a contradiction in the\nwitness' testimony just now, Your Honor",
      "type": "confident"
    },
    {
      "script": "Uh, where you ask?",
      "type": "abash"
    },
    {
      "script": "(Shoot, I lost my train of thought)"
    },
    {
      "script": "(Damn...)",
      "type": "despair",
      "background": "black"
    },
    {
      "script": "(Think Pheonix, think...\nWhat can I do?)", 
      "type": "despair",
      "background": "black"
    },
    {
      "script": "(Oh! I got an idea)",
      "background":"court"
    },
    {
      "script": "My client is guilty af, Your Honor",
      "type": "confident"
    },
    {
      "script": ("PheonixTest",)
    }
  ]
}

# for keyboard interactions
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


gameScene = 'load'
scriptIndex = 0

text = []
textIndex = 0
optionSelected = 0
currentScript = 'PheonixTest'
font = pygame.font.SysFont(None, 30)
speakerColors = {
  'Torry': (100, 255, 100),
  'Narry': (100, 255, 100),
  'Daisuke': (150, 150, 255),
  'Pheonix': (150, 150, 255),
  'Ari': (255, 150, 150),
  '?': (100, 150, 150)
}

currentCharacter = script[currentScript][scriptIndex]['character']
currentType = script[currentScript][scriptIndex]['type']
currentBackground = script[currentScript][scriptIndex]['background']

assets = {}

running = True

while running:
  # keyboard interactions and game exit
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False
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

  # load assets
  if gameScene == 'load':
    screen.fill((0, 0, 0))
    for assetName in os.listdir('./assets/'):
      assets[assetName] = {}
      for asset in os.listdir(f'./assets/{assetName}'):
        assets[assetName][asset[:-4]] = pygame.image.load(f'./assets/{assetName}/{asset}')
    gameScene = 'game'

  # start game
  if gameScene == 'game':
    # if background changed from previous line update background
    if 'background' in script[currentScript][scriptIndex].keys():
      if currentBackground != script[currentScript][scriptIndex]['background']:
        currentBackground = script[currentScript][scriptIndex]['background']

    # if character changed from previous line update character
    if 'character' in script[currentScript][scriptIndex].keys():
      if currentCharacter != script[currentScript][scriptIndex]['character']:
        currentCharacter = script[currentScript][scriptIndex]['character']

    # if type changed from previous line update type
    if 'type' in script[currentScript][scriptIndex].keys():
      if currentType != script[currentScript][scriptIndex]['type']:
        currentType = script[currentScript][scriptIndex]['type']

    # screen.fill((255, 255, 255))
  
    speakerColor = speakerColors[currentCharacter]
      
    screen.blit(assets['Backgrounds'][currentBackground], (0, 0))

    # 300 / assets[currentCharacter][currentType].get_height() * assets[currentCharacter][currentType].get_width

    image = pygame.transform.scale(assets[currentCharacter][currentType], (math.floor(math.floor(300 / assets[currentCharacter][currentType].get_height() * assets[currentCharacter][currentType].get_width())), 300))
    imageR = image.get_rect()
    imageR.centerx = 235
    imageR.bottom = 365
    screen.blit(image, imageR)
      
    speakerR = pygame.Rect(0, 0, 100, 30)
    speakerR.centerx = 250
    speakerR.bottom = 365
    pygame.draw.rect(screen, speakerColor, speakerR)
  
    pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(0, 365, 500, 135))
  
    speaker = font.render(currentCharacter, True, (0, 0, 0))
    speakerRect = speaker.get_rect(centerx = 250, centery = 352)
  
    
    h = font.get_height() * 1.35
    for i in range(len(text)):
      dialogue = font.render(text[i], True, (0, 0, 0))
      dialogueRect = dialogue.get_rect(centerx = 250, top = 380 + i * h)
      screen.blit(dialogue, dialogueRect)
    screen.blit(speaker, speakerRect)

    # if script is a list it is an options dialogue where user can choose
    if type(script[currentScript][scriptIndex]['script']) == list:
      if optionSelected > len(script[currentScript][scriptIndex]['script']) - 1:
        optionSelected = 0
      elif optionSelected < 0:
        optionSelected = len(script[currentScript][scriptIndex]['script']) - 1
  
      text = []
      if len(text) < len(script[currentScript][scriptIndex]['script']):
        for i in range(0, len(script[currentScript][scriptIndex]['script'])):
          text.extend(f"> {script[currentScript][scriptIndex]['script'][i][0]} <".split('\n') if optionSelected is i else script[currentScript][scriptIndex]['script'][i][0].split('\n'))
      
      if keys['up']['pressed'] == True:
        optionSelected -= 1
      elif keys['down']['pressed'] == True:
        optionSelected += 1
      elif keys['space']['pressed'] == True:
        currentScript = script[currentScript][scriptIndex]['script'][optionSelected][1]
        scriptIndex = 0
        optionSelected = 0
    # if script is a tuple it is a transition to the scene specified
    elif type(script[currentScript][scriptIndex]['script']) == tuple:
        currentScript = script[currentScript][scriptIndex]['script'][0]
        scriptIndex = 0
    # if script is a string it is normal dialogue
    elif type(script[currentScript][scriptIndex]['script']) == str:
      text = script[currentScript][scriptIndex]['script'][0:math.floor(textIndex)].split('\n')
  
      if keys['space']['pressing'] == True:
        textSpeed = 0.6 
      else:
        textSpeed = 0.3
      
      if keys['space']['pressed'] == True and textIndex > len(script[currentScript][scriptIndex]['script']):
        scriptIndex += 1
        textIndex = 0
  
      textIndex += textSpeed

  pygame.display.flip()
  clock.tick(60)