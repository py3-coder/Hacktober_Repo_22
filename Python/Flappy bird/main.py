import random # for generation of random numbers
import sys
from typing import Mapping
import pygame 
from pygame.locals import * # Basic pygame imports
#Global variales for the game
FPS = 20
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/bird2.png'
GROUNDY = SCREENHEIGHT - 90
BACKGROUND = 'gallery/back.png'
PIPE = 'gallery/pipe.png'
BASE = 'gallery/base.png'
def welcomeScreen(): #shows welcome screen on the screen
    playerx = int((SCREENWIDTH/5)/2)
    playery = int((SCREENHEIGHT - (GAME_SPRITES['player1'].get_height()))/2)
    
    basex = 0
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1 :
                mainGame()
            elif event.type==KEYDOWN and event.key==K_RETURN:
                mainGame()
            else:

                SCREEN.blit(GAME_SPRITES['message'],(0,0))
                SCREEN.blit(pygame.image.load(PLAYER).convert_alpha(),(playerx,playery))
                SCREEN.blit(pygame.image.load(BASE).convert(),(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
  
def mainGame():
    score = 0
    playerx = int ((SCREENWIDTH/5)/2)
    playery = int((SCREENHEIGHT - (GAME_SPRITES['player1'].get_height()))/2)
    newpipe1= getRandompipe()
    newpipe2 = getRandompipe()
    upperpipes = [
        {'x' : SCREENWIDTH +200, 'y':newpipe1[0]['y']},
        {'x' : SCREENWIDTH +200 + (SCREENWIDTH/2), 'y':newpipe2[0]['y']}
    ]
    lowerpipes = [
        {'x' : SCREENWIDTH +200, 'y':newpipe1[1]['y']},
        {'x' : SCREENWIDTH +200 + (SCREENWIDTH/2), 'y':newpipe2[1]['y']}
    ]
    pipe_velx = -4
    playerFlapped = False
    player_vely = -11
    playeramaxvel = 10
    
    playeraccy = 1
    playerFlapAcc = -8
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key== K_UP:
                if player_vely>0:
                    player_vely = playerFlapAcc
                    playerFlapped = True
                    GAME_SOUNDS['woosh'].play()

        crashtest = iscollide(playerx,playery,upperpipes,lowerpipes)  #This func will return true if the player is crashed

        if crashtest:
            return False
        #check for score
        playerMidpos =  playerx + GAME_SPRITES['player1'].get_width()/2
        for pipe in upperpipes:
            pipeMIDpos = pipe['x']+ GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMIDpos<=playerMidpos :
                score=score+1
                
        
        if player_vely < playeramaxvel and not playerFlapped:
            player_vely+=playeraccy
        
        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player1'].get_height()
        playery+=min(player_vely,GROUNDY-playery-playerHeight)

        # move pipes to the left
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            upperpipe['x']+=pipe_velx
            lowerpipe['x']+=pipe_velx
        # add a new pipe when the first pipe is about to  go out of the screen..
        if 0<lowerpipes[0]['x']<5:
            newpipe = getRandompipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])
        
        # if the pipe is out of the screen, just remove it..
        if upperpipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)
        # lets start the real code now, blitting our sprites to our game to make it real.
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperpipe['x'],upperpipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerpipe['x'],lowerpipe['y']))
        myDigits = [int(x) for x in list(str(score//26))]

        width = 0
        for digit in myDigits:
            width+=GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2
        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREENHEIGHT*0.12))
            Xoffset+=GAME_SPRITES['numbers'][digit].get_width()
        
        SCREEN.blit(GAME_SPRITES['base'],(0,GROUNDY))
        SCREEN.blit(pygame.image.load(PLAYER).convert_alpha(),(playerx,playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def iscollide(playerx,playery,upperpipes,lowerpipes):
    if playery > GROUNDY-GAME_SPRITES['player1'].get_height()-10 or playery<0:
        return True
    for pipe in upperpipes:

        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (playery<pipeHeight+pipe['y'] and abs(playerx - pipe['x']) <= GAME_SPRITES['pipe'][0].get_width()):
            return True
    for pipe in lowerpipes:
        if (playery+GAME_SPRITES['player1'].get_height()) > pipe['y'] and abs(playerx - pipe['x']) <= GAME_SPRITES['pipe'][0].get_width():
            return True

def getRandompipe():
    """
    Generate positions of the two pipes for blitting on the screen
    """
    pipeheight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/2.5
    y2 = offset + random.randrange(0,int(SCREENHEIGHT- 90 - 1.2*offset))
    pipex = SCREENWIDTH + 20
    y1 = pipeheight - y2 + offset -40
    pipe = [
        {'x': pipex, 'y':-y1}, #upperpipes
        {'x': pipex, 'y':y2}, #lowerpipes
    ]
    return pipe

if __name__=="__main__" :
    #This will be the main point from where our game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Boring Game")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/numbers0.png').convert_alpha(),
        pygame.image.load('gallery/numbers1.png').convert_alpha(),
        pygame.image.load('gallery/number2.png').convert_alpha(),
        pygame.image.load('gallery/numbers3.png').convert_alpha(),
        pygame.image.load('gallery/numbers4.png').convert_alpha(),
        pygame.image.load('gallery/numbers5.png').convert_alpha(),
        pygame.image.load('gallery/numbers6.png').convert_alpha(),
        pygame.image.load('gallery/numbers7.png').convert_alpha(),
        pygame.image.load('gallery/numbers8.png').convert_alpha(),
        pygame.image.load('gallery/numbers9.png').convert_alpha(),
    )
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
    )
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player1'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['message'] = pygame.image.load('gallery/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load(BASE).convert()
    
    # Game Sounds 
    GAME_SOUNDS['woosh'] = pygame.mixer.Sound('gallery/woosh.wav')
    while True:
        welcomeScreen()
        
        


        