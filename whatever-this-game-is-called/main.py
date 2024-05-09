# Daniel Kim and Daniel Shin
# whatever this game is called: an interactive novel

# programmed by Daniel Shin

# import modules
import pygame
import math
import os

# import script
from gameScript import script

# initialize pygame
pygame.init()
pygame.display.set_caption('whatever this game is called')
pygame.display.set_icon(pygame.image.load('icon.png'))
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

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
    }
}

# game variables
gameScene = 'load'
currentScript = 't'
scriptIndex = 0
text = []
textIndex = 0
optionSelected = 0
font = pygame.font.SysFont(None, 30)
speakerColors = {
    'Tori': (100, 255, 100),
    'Ending': (100, 255, 100),
    'Narrator': (100, 255, 100),
    'Daisuke': (150, 150, 255),
    'Pheonix': (150, 150, 255),
    'Ari': (255, 150, 150),
    'Unknown': (100, 150, 150)
}
assets = {}
endings = {
    'GENTLEMAN': False,
    'DENSE AS A BRICK WALL': False,
    'SEQUEL?': False,
    'FRIENDSHIP RUINED': False,
    'OUTCAST AT SCHOOL': False,
    'BETA MALE': False,
    'TRUE': False,
    'EMOTIONAL DAMAGE': False,
    'SECRET': False
}

# current character, action, background displayed
current = {
    'character': script[currentScript][scriptIndex]['character'],
    'action': script[currentScript][scriptIndex]['action'],
    'background': script[currentScript][scriptIndex]['background']
}


# update background, character, action if it is different from previous line in script
def update(a):
    if a in script[currentScript][scriptIndex].keys():
        if current[a] != script[currentScript][scriptIndex][a]:
            current[a] = script[currentScript][scriptIndex][a]


# load assets function just for meeting the "have multiple functions" requirement
def loadAssets():
    for assetName in os.listdir('./assets/'):
        assets[assetName] = {}
        for asset in os.listdir(f'./assets/{assetName}'):
            assets[assetName][asset[:-4]] = pygame.image.load(
                f'./assets/{assetName}/{asset}').convert_alpha()


while True:
    # keyboard interactions and game exit
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) in ('up', 'down', 'space'):
                keys[pygame.key.name(event.key)]['pressing'] = True
        if event.type == pygame.KEYUP:
            if pygame.key.name(event.key) in ('up', 'down', 'space'):
                keys[pygame.key.name(event.key)]['pressing'] = False
                keys[pygame.key.name(event.key)]['stop'] = False

    for key in keys:
        if keys[key]['pressing'] == True and keys[key]['stop'] == False:
            keys[key]['pressed'] = True
            keys[key]['stop'] = True
        else:
            keys[key]['pressed'] = False

    # load assets from folder into a dictionary
    if gameScene == 'load':
        loadAssets()
        gameScene = 'game'

    # start game
    if gameScene == 'game':
        # check and update endings dictionary
        if len(script['e']) < len(endings):
            script['e'].append({
                "script":
                (f"Endings\n{list(endings.values()).count(True)}/{len(endings)} Completed"
                 )
            })
            for i in endings:
                script['e'].append({
                    "script":
                    f"[X] {i} ENDING"
                    if endings[i] is True else f"[   ] {i} ENDING"
                })
            script['e'].append({"script": ("r", )})

        # update these if they changed from previous line in script
        update('background')
        update('character')
        update('action')

        # set the speaker rectangle color
        speakerColor = speakerColors[current['character']]

        # set background image according to current background
        screen.blit(assets['Backgrounds'][current['background']], (0, 0))

        # show character image according to current character and action
        characterImage = pygame.transform.scale(
            assets[current['character']][current['action']], (math.floor(
                math.floor(300 / assets[current['character']][
                    current['action']].get_height() * assets[
                        current['character']][current['action']].get_width())),
                                                              300))
        characterRectangle = characterImage.get_rect()
        characterRectangle.centerx = 235
        characterRectangle.bottom = 365
        screen.blit(characterImage, characterRectangle)

        # colored speaker rectangle with name
        speakerRectangle = pygame.Rect(0, 0, 100, 30)
        speakerRectangle.centerx = 250
        speakerRectangle.bottom = 365
        pygame.draw.rect(screen, speakerColor, speakerRectangle)
        speakerName = font.render(current['character'], True, (0, 0, 0))
        speakerNameRectangle = speakerName.get_rect(centerx=250, centery=352)
        screen.blit(font.render(current['character'], True, (0, 0, 0)),
                    speakerNameRectangle)

        # dialogue rectangle
        pygame.draw.rect(screen, (230, 230, 230),
                         pygame.Rect(0, 365, 500, 135))

        # render text separated by lines
        h = font.get_height() * 1.35
        for i in range(len(text)):
            dialogue = font.render(text[i], True, (0, 0, 0))
            dialogueRectangle = dialogue.get_rect(centerx=250, top=380 + i * h)
            screen.blit(dialogue, dialogueRectangle)

        # if script is a list it is an options dialogue where user can choose
        if type(script[currentScript][scriptIndex]['script']) == list:
            # loop options so it goes from last option to first option
            if optionSelected > len(
                    script[currentScript][scriptIndex]['script']) - 1:
                optionSelected = 0
            elif optionSelected < 0:
                optionSelected = len(
                    script[currentScript][scriptIndex]['script']) - 1

            # complicated jumble but in essence just showing the > and < around the selected option
            text = []
            if len(text) < len(script[currentScript][scriptIndex]['script']):
                for i in range(
                        0, len(script[currentScript][scriptIndex]['script'])):
                    text.extend(
                        f"> {script[currentScript][scriptIndex]['script'][i][0]} <"
                        .split('\n') if optionSelected is i else
                        script[currentScript][scriptIndex]['script'][i][0].
                        split('\n'))

            # selecting an option
            if keys['up']['pressed'] == True:
                optionSelected -= 1
            elif keys['down']['pressed'] == True:
                optionSelected += 1
            elif keys['space']['pressed'] == True:
                currentScript = script[currentScript][scriptIndex]['script'][
                    optionSelected][1]
                scriptIndex = 0
                optionSelected = 0
        # if script is a tuple it is a transition to the scene specified
        elif type(script[currentScript][scriptIndex]['script']) == tuple:
            currentScript = script[currentScript][scriptIndex]['script'][0]
            scriptIndex = 0
        # if script is a string it is normal dialogue
        elif type(script[currentScript][scriptIndex]['script']) == str:
            # if it is an ending update endings dictionary
            if 'ending' in script[currentScript][scriptIndex]:
                if endings[script[currentScript][scriptIndex]
                           ['ending']] == False:
                    endings[script[currentScript][scriptIndex]
                            ['ending']] = True
                    script['e'] = []

            # split text by line breaks so text can render properly
            text = script[currentScript][scriptIndex]['script'][
                0:math.floor(textIndex)].split('\n')

            # if space is being held faster speed
            if keys['space']['pressing'] == True:
                textSpeed = 0.6
            else:
                textSpeed = 0.3

            # if space if pressed and text is done go to next line
            if keys['space']['pressed'] == True and textIndex > len(
                    script[currentScript][scriptIndex]['script']):
                scriptIndex += 1
                textIndex = 0
            textIndex += textSpeed

    pygame.display.flip()
    clock.tick(60)
