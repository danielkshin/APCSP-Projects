# import modules
import math
import pygame

# print introduction and ask for user input
print('\ncolors\na simple platformer game based around the concept of color created with pygame\n\nHow to play:\nUse either the WAS or arrow keys to move your player.\nUse the SPACE key to change the color of your player. Your player is able to go through a block if their colors are alike.\nIf you are stuck, press H for a hint.\n')
input('Press ENTER to start game...')  # required input
print('Open the pygame window. Keep the console window open for hints and directions.')

# initialize and set up pygame
pygame.init()
screen = pygame.display.set_mode((700, 550))
pygame.display.set_caption('colors')
clock = pygame.time.Clock()

# list of colors
allColors = [
    (0, 0, 0),  # Black (solid block)
    (140, 140, 140),  # Gray (player)
    (60, 60, 60),  # Dark Gray
    (255, 80, 80),  # R
    (255, 180, 100),  # O
    (230, 210, 100),  # Y
    (120, 170, 120),  # G
    (100, 150, 170),  # B
    (60, 60, 60),  # Dark Gray
    (60, 60, 60)  # Dark Gray
]  # required list
colors = allColors[0:4]

# level info and level data
#   p = player
#   o = portal
#   numbers = block with color index of allColors
levels = [
    {
        "name": "the two tranquil trees",
        "hint": "Instead of going through the trees, climb over them.",
        "level": [
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                1111        ",
            "              1111111       ",
            "             11121111       ",
            "        222  111211111      ",
            "       22222 122101121      ",
            "      222222  11000121      ",
            "      222222    11001       ",
            "      212122      20        ",
            "        11        20        ",
            "  p      1       2220    o  ",
            " 000     1     2222220  000 ",
            "0000000000000000000000000000",
            "0000000000000000000000000000",
            "0000000000000000000000000000"
        ]
    },
    {
        "name": "the secret below the volcano",
        "color": "red",
        "hint": "Take the darker path down the volcano.",
        "level": [
            "    221111122               ",
            "    211111112               ",
            "     11111111               ",
            "      111111                ",
            "      11111                 ",
            "     0333332                ",
            "    0033333222              ",
            " p 0023333322222            ",
            " 0002333333322222           ",
            "00222333333322222221        ",
            "222233333333222222111       ",
            "22223333333332223222111     ",
            "222233333333322233222211    ",
            "2223333003333322233222211   ",
            "223333000033332223322222111 ",
            "2333330020333322222222221111",
            "3333332222333332222222211111",
            "3333332222333332222222211111",
            "3333332222233322222211111111",
            "3333322222233322222111111111",
            "33333222o2233322221111111133",
            "3333332000223222111113113333",
            "0000000000222222033330000000",
            "0000000000000000000000000000"
        ]
    },
    {
        "name": "rising with the flame",
        "color": "orange",
        "hint": "Take the right path up the smoke.",
        "level": [
            "                            ",
            "                            ",
            "            1     o1        ",
            "           11     111       ",
            "           11  4   11       ",
            "       3                    ",
            "              1     3       ",
            "             11     43      ",
            "             1      43      ",
            "         3                  ",
            "        343    3   4   11   ",
            "         3    333 43  111   ",
            "              3433    111   ",
            "             3344333 111    ",
            "             3444443        ",
            "        2   334444433       ",
            "        22  3444444443      ",
            "      4 22  3444444443      ",
            "     24422  3444444443      ",
            "     222222234444422222221  ",
            "      222222222222222222111 ",
            " p 44 222222222222222222211 ",
            "0000000000000000000000000000"
        ]
    },
    {
        "name": "the tricky path up the pyramid",
        "color": "yellow",
        "hint": "Be patient and think before moving.",
        "level": [
            "                            ",
            "   44                       ",
            "  4554       111       444  ",
            "  4o5411    11111   4444    ",
            " 14411111                   ",
            "  111111                    ",
            "                 5    4     ",
            "               555   544    ",
            "             555    55454   ",
            "                   4554554  ",
            " 55  p      555   455544554 ",
            "55   22    55    55555545554",
            "     22   55    455555545555",
            "   2 22 2      4555555544555",
            "   2 2222     55555555554555",
            "   222222    555555555554555",
            "     22     4555555555554555",
            "     22    45555555555554555",
            "5555 22   444444555555554444",
            "5555555555555544444444444555",
            "5555555555555555555555555555",
            "5555555555555555555555555555"
        ]
    },
    {
        "name": "the starry night of the fruitful forrest",
        "color": "green",
        "hint": "Climb the orange tree by carefully navigating.",
        "level": [
            "2222222222222222222222222222",
            "2222225222222222222o22222222",
            "2222222222522222222222222252",
            "2225222225 22252222666662222",
            "2222222225 22222266466666222",
            "2222222222522222666664666622",
            "     22222      646666664622",
            " p              6666666666  ",
            "65     6663     6646666466  ",
            "66     63666     66661666   ",
            "666   6666663       1264    ",
            "6665  3663666    4  11      ",
            "5666  6666666   111 11      ",
            "666    66166      1111      ",
            "66       11         111166  ",
            "11 5     1111       12 66   ",
            "1111     21         11      ",
            "11       11        6112     ",
            "11      2111      6611166  6",
            "111     1111    4 6111111666",
            "2226666622226666662222222266",
            "6666666666666666666666666666"
        ]
    },
    {
        "name": "hidden within the waterfall",
        "color": "blue",
        "hint": "Climb the tree to climb the waterfall.",
        "level": [
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "                            ",
            "55                          ",
            "455                 66666666",
            "5545                2  00000",
            "5555               2222200 0",
            "5454              77222 0000",
            "4555      7      777722000  ",
            "55     7       2277772220   ",
            "2            7   7777       ",
            "2 22  7          7777       ",
            "222       1   1117777       ",
            "2       1111111117777       ",
            "2        111111117777       ",
            "22           7  77777       ",
            "222 p          777777     o ",
            "666666777772277777777    000",
            "6666666777777777777722222000",
            "6666666667777777772222222200",
            "7777777777777777777777777777"
        ]
    },
    {
        "name": "someplace familiar",
        "hint": "This is the end. Thank you for playing.",
        "level":  [
            "7777777777777777777777777777",
            "7777447777777777777777777777",
            "7774554777777777777777777777",
            "7774554  7777777777777777777",
            "777744    777777777777777777",
            "7777777777777777777777777777",
            "77777777777        777777777",
            "7777777                77777",
            "                3666        ",
            "              6666666       ",
            "             63626366       ",
            "        666  666266666      ",
            "       36666 622626626      ",
            "      666636  66222623      ",
            "      366666    36226       ",
            "      626263      22        ",
            "        22        22        ",
            "  p      2       2222       ",
            " 000     2     2222222      ",
            "6666666666666666666666666666",
            "6666666666666666666666666666",
            "6666666666666666666666666666",
            "0000000000000000000000000000",
            "000000000000000000000000000o"
        ]
    }
]

# portal class
class portal:
    def __init__(this, x, y, colorIndex):
        # portal attributes
        this.colorIndex = colorIndex
        this.color = allColors[this.colorIndex]
        this.rect = pygame.Rect(x, y, 25, 25)


# block class
# render optimization with reference to https://stackoverflow.com/questions/53660333/pygame-drawing-multiple-rectangles
class block(pygame.sprite.Sprite):
    def __init__(this, x, y, colorIndex):
        # block attributes
        super().__init__()
        this.colorIndex = colorIndex
        this.color = colors[this.colorIndex]
        this.image = pygame.Surface((25, 25))
        this.image.fill(this.color)
        this.rect = this.image.get_rect(x=x, y=y)

# player class
class player:
    def __init__(this, x, y):
        # player attributes
        this.rect = pygame.Rect(x, y, 25, 25)
        this.colorIndex = 1
        this.color = colors[this.colorIndex]

        # player status
        this.onGround = False
        this.inBlock = False
        this.colorChanged = False
        this.xv = 0
        this.yv = 0
        this.speed = 3
        this.g = 0.5

    # player interaction
    def interaction(this):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            this.xv = this.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            this.xv = -this.speed
        else:
            this.xv = 0

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and this.onGround == True:
            this.yv = -8.75

        if keys[pygame.K_SPACE]:
            if this.colorChanged == False:
                this.changeColor()
        else:
            this.colorChanged = False

    # player color change function
    def changeColor(this):
        # if player is not in a block, they can change colors
        if this.inBlock == False:
            this.colorIndex += 1
            this.colorChanged = True
            if this.colorIndex > len(colors) - 2:
                this.colorIndex = 1
            this.color = colors[this.colorIndex]

    # update character
    def update(this):
        if this.inBlock == True:
            this.color = (240, 240, 240)
        else:
            this.color = colors[this.colorIndex]
        this.interaction()

# level class
class level:
    def __init__(this, levelIndex):
        # level attributes and print necessary info
        this.levelIndex = levelIndex
        this.deaths = 0
        this.hintRevealed = False
        print(
            f"\nLevel {this.levelIndex + 1} - {levels[this.levelIndex]['name']}")
        this.reset(False)

    # level generation from string
    def generate(this, level):
        this.blocks = pygame.sprite.Group()
        for row in range(len(level)):
            for column in range(len(level[row])):
                if level[row][column] == 'p':
                    this.player = player(column * 25, row * 25)
                elif level[row][column] == 'o':
                    this.portal = portal(
                        column * 25, row * 25, this.levelIndex + 3)
                elif level[row][column] != ' ':
                    this.blocks.add(
                        block(column * 25, row * 25, int(level[row][column])))

    # reset level and check whether it was just a death or a level completion
    def reset(this, completed):
        # if level is completed proceed to next level and print level info
        if completed == True:
            # sequencing
            this.deaths = 0
            this.hintRevealed = False
            this.levelIndex += 1
            print(
                f"\nLevel {this.levelIndex + 1} - {levels[this.levelIndex]['name']}")
            # iteration
            for i in levels[this.levelIndex]:
                # selection
                if i == 'color':
                    print(f"Avoid {levels[this.levelIndex]['color']}!")
        # regenerate level
        this.level = levels[this.levelIndex]['level']
        this.generate(this.level)

    # check for game collisions
    def collision(this):
        # horizontal player movement
        this.player.rect.x += this.player.xv

        # horizontal bounds
        if this.player.rect.left < 0:
            this.player.rect.left = 0
        elif this.player.rect.right > 700:
            this.player.rect.right = 700

        # horizontal collision
        for block in this.blocks:
            if this.player.colorIndex != block.colorIndex and block.colorIndex != len(colors) - 1:
                if block.rect.colliderect(this.player.rect):
                    if this.player.xv < 0:
                        this.player.rect.left = block.rect.right
                    elif this.player.xv > 0:
                        this.player.rect.right = block.rect.left

        # vertical movement
        this.player.rect.y += this.player.yv
        this.player.yv += this.player.g

        # vertical collision
        for block in this.blocks:
            if this.player.colorIndex != block.colorIndex and block.colorIndex != len(colors) - 1:
                if block.rect.colliderect(this.player.rect):
                    if this.player.yv > 0:
                        this.player.onGround = True
                        this.player.yv = 0
                        this.player.rect.bottom = block.rect.top
                    elif this.player.yv < 0:
                        this.player.yv = 0
                        this.player.rect.top = block.rect.bottom

        # check for death block collision (if not first level as there are no death blocks in it)
        if this.levelIndex != 0:
            for block in this.blocks:
                if block.colorIndex == len(colors) - 1:
                    if block.rect.colliderect(this.player.rect):
                        this.deaths += 1
                        this.reset(False)

        # check for portal collision and print necessary info when required
        if this.portal.rect.colliderect(this.player.rect):
            print(
                f"Level completed{f' with {this.deaths} deaths.' if this.deaths != 0 else '!'}")
            if 'color' in levels[this.levelIndex]:
                pygame.time.wait(2000)
                print(
                    f"Discovered the color {levels[this.levelIndex]['color']}. You can now change to {levels[this.levelIndex]['color']}!")
            pygame.time.wait(2000)
            if this.levelIndex != 0:
                colors.append(allColors[len(colors)])
            this.reset(True)

        # check whether player is in a block
        for block in this.blocks:
            if block.colorIndex == this.player.colorIndex:
                if block.rect.colliderect(this.player.rect):
                    this.player.inBlock = True
                    break
                else:
                    this.player.inBlock = False

        # check whether player is on ground
        if this.player.onGround == True and (this.player.yv < 0 or this.player.yv > 1):
            this.player.onGround = False

    # level hint function
    def hint(this):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h] == True and this.hintRevealed == False:
            print(f"Hint: {levels[this.levelIndex]['hint']}")
            this.hintRevealed = True

    # display level
    def display(this):
        this.blocks.draw(screen)
        pygame.draw.rect(screen, this.portal.color, this.portal.rect, width=2)

        this.collision()
        this.player.update()
        pygame.draw.rect(screen, this.player.color, this.player.rect)

        this.hint()


Level = level(0)

# running the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((240, 240, 240))
    Level.display()

    pygame.display.update()
    clock.tick(60)
