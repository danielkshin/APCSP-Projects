import pygame
import os

pygame.init()
  
white = (255, 255, 255)
  
display_surface = pygame.display.set_mode((500, 500))
  
pygame.display.set_caption('Image')

assets = {}

scene = 'loadAssets'
running = True

done = 0
total = 0
while running == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if scene == 'loadAssets':
    for assetName in os.listdir('./assets/'):
      assets[assetName] = {}
      total += len(os.listdir(f'./assets/{assetName}'))
      for asset in os.listdir(f'./assets/{assetName}'):
        assets[assetName][asset[:-4]] = pygame.image.load(f'./assets/{assetName}/{asset}')
        done += 1
        print(f"{done}/{total} loaded {assetName}/{asset[:-4]}")
        print(f"loading assets {done / total * 100}%")

    scene = 'display'

  if scene == 'display':
    display_surface.fill(white)
    display_surface.blit(assets['Pheonix']['despair'], (0, 0))
    
    #print(assets)
    pygame.display.flip()