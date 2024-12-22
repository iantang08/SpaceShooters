'''
AUTHORS: IAN T. & KELVIN X.
DATE: NOVEMBER 2, 2020
NAME: SPACE SHOOTERS
DESCRIPTION: THIS PROGRAM IS OUR CULMINATING PROJECT
IT IS A SPACE THEMED GAME WITH A QUIZ AND LESSON TOO.
'''

# import pygame module
import pygame
import sys
import os
import platform
import time
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# # for the program to work on tdsb computers
# if platform.system() == "Windows":
#     os.environ['SDL_VIDEODRIVER'] = 'windib'

# initialize pygame
pygame.init()

# declares time
clock = pygame.time.Clock()

# set screen display
LENGTH = 640
HEIGHT = 480
gameDisplay = pygame.display.set_mode([640, 480])
size = ([LENGTH, HEIGHT])

# Declare some colours
white = (255, 255, 255)
black = (0, 0, 0)

# set the caption
pygame.display.set_caption("Space Shooters")

# load images
titleBackground = pygame.image.load('images/titleBackground.jpg')
titleBackground = pygame.transform.scale(titleBackground, size)
loadingBackground = pygame.image.load('images/loadingBackground.jpeg')
loadingBackground = pygame.transform.scale(loadingBackground, size)
space = pygame.image.load('images/Space.jpg')
spaceship = pygame.image.load('images/spaceship.png')
smallShip = pygame.image.load('images/spaceship2.png')
mars = pygame.image.load('images/mars_transparent.png')
blackHole = pygame.image.load('images/blackHole.png')
saturn = pygame.image.load('images/saturn.png')
jetImg = pygame.image.load('images/jet.png')
laser = pygame.image.load('images/laser.png')
mercury = pygame.image.load('images/mercury.png')
quizBackground = pygame.image.load('images/quizBackground.gif')
quizBackground = pygame.transform.scale(quizBackground, size)
pauseBackground = pygame.image.load('images/pauseBackground.jpg')
pauseBackground = pygame.transform.scale(pauseBackground, size)
mainMenuBackground = pygame.image.load('images/mainMenuBackground.jpg')
mainMenuBackground = pygame.transform.scale(mainMenuBackground, size)
resultsBackground = pygame.image.load('images/resultsBackground.jpg')
resultsBackground = pygame.transform.scale(resultsBackground, size)
lessonBackground = pygame.image.load('images/lessonBackground.jpg')
lessonBackground = pygame.transform.scale(lessonBackground, size)
rocket = pygame.image.load('images/rocket.png')
travellingToMars = pygame.image.load('images/travellingToMars.jpg')

#Load fonts
font = pygame.font.Font('fonts/Chopsic-K6Dp.ttf', 50)
mediumFont = pygame.font.Font('fonts/revamped.ttf', 25)
revamped = pygame.font.Font('fonts/revamped.ttf', 25)
agelast = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 25)
casanova = pygame.font.Font('fonts/CasanovaScotia-Xm0K.ttf', 40)

# declare variables
numCorrect = 1
questionsAnswered = 0
answered = False
finalScore = 0
gameScore = 0
levelEnd = False

# CREATE FUNCTIONS FOR BUTTONS, DISPLAYING TEXT, ETC.


# function to create buttons
def button(text, x, y, length, height, colour, action, font=revamped):
    pos = pygame.mouse.get_pos()  # get the position of the mouse
    click = pygame.mouse.get_pressed()  # see if the mouse was clicked
    text = font.render(text, True, white)  #render the text
    textRect = text.get_rect(topleft=(x, y))

    gameDisplay.blit(text, textRect)  #blit the text
    if x + length > pos[0] > x and y + height > pos[
            1] > y:  #if the mouse is in range of the button:
        if click[0] == 1:  #if clicked:

            if action == 'lesson4':
                lesson4()
            if action == 'lesson3':
                lesson3()
            if action == 'lesson2':
                lesson2()
            if action == 'lesson1':
                lesson1()
            if action == "game":
                game()
            if action == 'howToPlay':
                howToPlay()
            if action == 'quiz':
                quiz()
            if action == 'q1':
                q1()
            if action == 'exit':
                pygame.quit()
            if action == 'mainMenu':
                mainMenu()
            if action == 'results':
                results()
            if action == 'loadingScreen':
                loadingScreen()
            if action == 'correct':
                correct()
            if action == 'incorrect':
                incorrect()
            if action == 'quizPaused':
                quizPaused()
            if action == 'paused':
                paused()
            if action == 'unpause':
                unpause()
            if action == 'level5':
                level5()
            if action == 'level4':
                level4()
            if action == 'level3':
                level3()
            if action == 'level2':
                level2()
            if action == 'level1':
                level1()


# function to render text
def textObject(text, font):
    textSurface = font.render(text, True, white)
    return textSurface


# procedure to display text centered
def center_display(text, x, y, font=font):
    message = font.render(text, True, white)
    textRect = message.get_rect(center=(320, y))
    gameDisplay.blit(message, textRect)


# Procedure to display text
def message_display(text, x, y, font, colour):
    message = font.render(text, True, colour)
    gameDisplay.blit(message, (x, y))


def paused():
    global pause
    pause = True
    while pause:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        #display some text and a button
        center_display('Paused', LENGTH, 240, casanova)
        button('Play', 500, 400, 75, 25, white, 'unpause', agelast)
        button('Main Menu', 60, 400, 140, 25, white, 'mainMenu', agelast)
        pygame.display.flip()


# function for title screen
def titleScreen():
    title = True
    while title:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(titleBackground, (0, 0))
        message_display('Ian T. and Kelvin X.', 50, 100, revamped, white)
        message_display('ICS207', 50, 150, revamped, white)
        button('Next', 510, 400, 85, 28, white, 'loadingScreen')
        pygame.display.flip()


# function for the entire loading screen
def loadingScreen():
    loading = True
    while loading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        loadingScreenAnimation()


# function for the loading bar to move
def loadingScreenAnimation():
    global jetx, jety, loadingBar
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #declare starting points for the jet
    jetx = 100
    jety = 250
    clock.tick(60)
    #blit everything to the screen
    gameDisplay.fill(white)
    gameDisplay.blit(loadingBackground, (0, 0))
    pygame.draw.rect(gameDisplay, black, (120, 300, 400, 5))
    center_display('Loading...', 10, 250, revamped)
    #generate the amont of pixels the jet will move
    jetxIncrease = random.randint(5, 20)
    jetx += jetxIncrease
    loadingBar = 40
    gameDisplay.blit(jetImg, (jetx, jety))
    pygame.display.flip()
    time.sleep(1)
    #while the jet hasn't reached the end of the loading bar:
    while jetx < 440:
        gameDisplay.blit(loadingBackground, (0, 0))
        pygame.draw.rect(gameDisplay, black, (120, 300, 400, 5))
        center_display('Loading...', 10, 250, revamped)
        jetxIncrease = random.randint(10, 30)
        jetx += jetxIncrease
        pygame.draw.rect(gameDisplay, (255, 0, 0), (120, 300, loadingBar, 5))
        loadingBar += jetxIncrease
        gameDisplay.blit(jetImg, (jetx, jety))
        pygame.display.flip()
        time.sleep(0.2)
    time.sleep(1)
    loadingScreenStatic()


# function for after the loading bar has moved
def loadingScreenStatic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill(white)
    gameDisplay.blit(loadingBackground, (0, 0))
    pygame.draw.rect(gameDisplay, black, (120, 300, 400, 5))
    pygame.draw.rect(gameDisplay, (255, 0, 0), (120, 300, loadingBar, 5))
    gameDisplay.blit(jetImg, (jetx, jety))
    center_display('Welcome to...', 10, 350, revamped)
    pygame.display.flip()
    time.sleep(3)
    mainMenu()


###############################################################
# section for quiz


#pause and unpause functions for the quiz
def unpause():
    global pause
    pause = False


def quizPaused():
    global pause
    pause = True
    while pause:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if user hit p, unpause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        #blit and display background, text and buttons
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        center_display('Paused', LENGTH, 240, casanova)
        button('Play', 500, 400, 75, 28, white, 'unpause', agelast)
        button('Main Menu', 60, 400, 140, 25, white, 'mainMenu', agelast)
        pygame.display.update()


# function to count number of correct questions and display number of correct answers
def correct():
    global numCorrect, questionsAnswered, finalScore
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    numCorrect += 1
    questionsAnswered += 1
    #blit everything to screen
    gameDisplay.fill(white)
    gameDisplay.blit(quizBackground, (0, 0))
    center_display('Correct!', 10, 240, agelast)
    pygame.display.flip()
    time.sleep(2)
    #see how many questions were answered and bring the user to that page
    if questionsAnswered == 1:
        q2()
    if questionsAnswered == 2:
        q3()
    if questionsAnswered == 3:
        q4()
    if questionsAnswered == 4:
        q5()
    if questionsAnswered == 5:
        q6()
    if questionsAnswered == 6:
        finalScore = numCorrect
        returnMainMenu()


# function to display incorrect answers
def incorrect():
    global questionsAnswered
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    questionsAnswered += 1
    gameDisplay.fill(white)
    gameDisplay.blit(quizBackground, (0, 0))
    center_display('Incorrect!', 10, 240, agelast)
    pygame.display.flip()
    time.sleep(2)
    if questionsAnswered == 1:
        q2()
    if questionsAnswered == 2:
        q3()
    if questionsAnswered == 3:
        q4()
    if questionsAnswered == 4:
        q5()
    if questionsAnswered == 5:
        returnMainMenu()


# function for the Quiz starting page
def quiz():
    global numCorrect, questionsAnswered
    numCorrect = 1
    questionsAnswered = 0
    quiz = True
    while quiz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit everything to screen
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        center_display('It\'s', 10, 100, casanova)
        center_display('QUIZ', 10, 140, casanova)
        center_display('Time!', 10, 180, casanova)
        button('Back', 100, 400, 80, 25, black, 'mainMenu', agelast)
        button('Start', 500, 400, 87, 25, black, 'q1', agelast)
        pygame.display.flip()
        clock.tick(60)


# Question pages
def q1():
    answered == False
    while not answered:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        #blit everything to screen
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 10, 10, agelast,
                        white)
        # question
        center_display('How many moons does Saturn have?', LENGTH, 100,
                       agelast)
        # options
        button('a) 1', 200, 190, 50, 25, black, 'incorrect', agelast)
        button('b) 24', 200, 230, 73, 25, black, 'incorrect', agelast)
        button('c) 79', 200, 270, 73, 25, black, 'incorrect', agelast)
        button('d) 82', 200, 310, 73, 25, black, 'correct', agelast)
        pygame.display.flip()


def q2():
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 10, 10, agelast,
                        white)
        # question
        center_display('In our solar system, which', LENGTH, 100, agelast)
        center_display('planet is the most dense?', LENGTH, 130, agelast)
        # options
        button('a) Earth', 200, 190, 125, 25, black, 'correct', agelast)
        button('b) Jupiter', 200, 230, 150, 25, black, 'incorrect', agelast)
        button('c) Mars', 200, 270, 120, 25, black, 'incorrect', agelast)
        button('d) Neptune', 200, 310, 155, 25, black, 'incorrect', agelast)
        pygame.display.flip()
        clock.tick(60)


def q3():
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 10, 10, agelast,
                        white)
        # question
        center_display('True or False: Pluto is a planet:', LENGTH, 100,
                       agelast)
        # options
        button('a) True', 200, 190, 110, 25, black, 'incorrect', agelast)
        button('b) False', 200, 230, 120, 25, black, 'correct', agelast)
        button('c) All of the above', 200, 270, 290, 25, black, 'incorrect',
               agelast)
        pygame.display.flip()
        clock.tick(60)


def q4():
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 10, 10, agelast,
                        white)
        # question
        center_display('How much weight of the solar system does', LENGTH, 100,
                       agelast)
        center_display('the sun account for(approximate)?', LENGTH, 130,
                       agelast)
        # options
        button('a) 50%', 200, 190, 100, 25, black, 'incorrect', agelast)
        button('b) 99%', 200, 230, 100, 25, black, 'correct', agelast)
        button('c) 80%', 200, 270, 100, 25, black, 'incorrect', agelast)
        button('d) 25%', 200, 310, 100, 25, black, 'incorrect', agelast)
        pygame.display.flip()
        clock.tick(60)


def q5():
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 0, 10, agelast,
                        white)
        # question
        center_display('Which planet is the only planet that ', LENGTH, 50,
                       agelast)
        center_display('would float on water?', LENGTH, 80, agelast)
        # options
        button('a) Saturn', 200, 190, 138, 25, black, 'correct', agelast)
        button('b) Jupiter', 200, 230, 150, 25, black, 'incorrect', agelast)
        button('c) Mercury', 200, 270, 160, 25, black, 'incorrect', agelast)
        button('d) Venus', 200, 310, 125, 25, black, 'incorrect', agelast)
        pygame.display.flip()
        clock.tick(60)


def q6():
    answered = False
    while not answered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    quizPaused()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        message_display('Correct: ' + str(numCorrect - 1), 0, 10, agelast,
                        white)
        # question
        center_display('How many planets are there in?', LENGTH, 100, agelast)
        center_display('the solar system?', LENGTH, 130, agelast)
        # options
        button('a) 9', 200, 190, 60, 25, black, 'incorrect', agelast)
        button('b) 10', 200, 230, 63, 25, black, 'incorrect', agelast)
        button('c) 12', 200, 270, 63, 25, black, 'incorrect', agelast)
        button('d) 8', 200, 310, 60, 25, black, 'correct', agelast)
        pygame.display.flip()
        clock.tick(60)


# To return to the main menu
def returnMainMenu():
    global numCorrect, questionsAnswered
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(quizBackground, (0, 0))
        center_display('Good Job!', 10, 100, agelast)
        center_display('You finished the quiz!', 10, 150, agelast)
        button('Main Menu', 144, 400, 160, 25, black, 'mainMenu', agelast)
        button('Results', 400, 400, 125, 25, black, 'results', agelast)
        pygame.display.flip()


#################################################################################
#function for how to play screen
def howToPlay():
    smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
    howToPlay = True
    while howToPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(lessonBackground, (0, 0))
        center_display('How To Play', LENGTH, 50, casanova)
        center_display('WELCOME TO ', LENGTH, 100, agelast)
        center_display('SPACE SHOOTERS! ', LENGTH, 130, agelast)
        center_display("Along your way, you see many rockets flying at you.",
                       LENGTH, 275, smallText)
        center_display("Dodge those rockets!", LENGTH, 300, smallText)
        center_display(
            "Use the arrow keys to travel in the respective directions",
            LENGTH, 350, smallText)
        button('Back', 270, 400, 100, 50, black, 'mainMenu')
        pygame.display.flip()
        clock.tick(60)


##################################################################################
#SECTION FOR GAME


# function that runs when the player dies
def LevelEnd():
    global levelEnd
    levelEnd = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit messages to the screen
        center_display('Game over', LENGTH, 240, casanova)
        center_display('Try again next time!', LENGTH, 300, agelast)
        button('Main Menu', 60, 400, 140, 25, white, 'mainMenu', agelast)
        pygame.display.flip()


def notLevelEnd():
    global levelEnd
    levelEnd = False


#enemy class
class Enemy(pygame.sprite.Sprite):
    #initialize the class
    def __init__(self):
        #generate random locations for the rockets to spawn at
        posY = random.randint(0, HEIGHT)
        posX = random.randint(LENGTH, LENGTH + 100)
        pygame.sprite.Sprite.__init__(self)
        self.surf = rocket.convert()
        self.surf.set_colorkey(black)
        self.rect = self.surf.get_rect(center=(posX, posY))

    def update(self):
        global gameScore
        #move the rocket 5 pixels to the left everytime
        self.rect.move_ip(-5, 0)
        #if the rocket moves off the screen, remove it from the class
        if self.rect.right < 0:
            self.kill()
            #add 50 to game score
            gameScore += 50


#player
class Player(pygame.sprite.Sprite):
    #initialize class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = spaceship.convert()
        self.surf.set_colorkey(black)
        self.rect = self.surf.get_rect()

    #move the spaceship depending on the user input
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        #check to see if the spaceship is out of the screen
        if self.rect.left < 0:
            self.rect.left = 5
        if self.rect.right > LENGTH:
            self.rect.right = LENGTH - 5
        if self.rect.top <= 0:
            self.rect.top = 5
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - 5


#same as class Player() but the spaceship is smaller
class smallPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = smallShip.convert()
        self.surf.set_colorkey(black)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 5
        if self.rect.right > LENGTH:
            self.rect.right = LENGTH - 5
        if self.rect.top <= 0:
            self.rect.top = 5
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT - 5


# function for the game starting page
def game():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        button('Back', 40, 420, 100, 50, black, 'mainMenu')
        button('Start Game', LENGTH // 2 - 100, HEIGHT // 2, 100, 50, black,
               'level1')
        pygame.display.flip()
        clock.tick(500)


# function to start level 1 of the game
def level1():
    global gameScore
    global player
    global enemies
    gameScore = 0
    notLevelEnd()
    inLevel = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    allSprites.add(player)

    #ADDENEMY is a custom event that adds an enemy to the sprite groups every few milliseconds
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)

    #blit the background instantly
    gameDisplay.blit(travellingToMars, (0, 0))
    pygame.display.flip()

    while inLevel:
        # events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user hit the exit button
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # if user hit the p button
                    paused()
            if event.type == ADDENEMY:  # If ADDENEMY is true:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                allSprites.add(new_enemy)

        # if they beat the level
        if gameScore >= 700:
            beatLevel1()

        # update the user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        for entity in allSprites:
            gameDisplay.blit(entity.surf, entity.rect)
        enemies.update()

        # This is for collision detection
        collide = pygame.sprite.spritecollideany(player, enemies)
        if collide:
            # If so, then remove the player and stop the loop
            LevelEnd()

        pygame.display.flip()
        clock.tick(60)


def level2():
    global gameScore
    global player
    global enemies
    gameScore = 0
    notLevelEnd()
    inLevel = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)

    while inLevel:

        # events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user hit the exit button
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # if user hit the p button
                    paused()
            if event.type == ADDENEMY:  # ADDENEMY is a custom event to add an enemy
                new_enemy = Enemy()
                enemies.add(new_enemy)
                allSprites.add(new_enemy)

        # if they beat the level
        if gameScore >= 1200:
            beatLevel2()
        # update the user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        for entity in allSprites:
            gameDisplay.blit(entity.surf, entity.rect)
        enemies.update()

        # This is for collision detection
        collide = pygame.sprite.spritecollideany(player, enemies)
        if collide:
            # If so, then remove the player and stop the loop
            LevelEnd()
        pygame.display.flip()
        clock.tick(60)


def level3():
    global gameScore
    global player
    global enemies
    gameScore = 0
    notLevelEnd()
    inLevel = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)

    while inLevel:

        # events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user hit the exit button
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # if user hit the p button
                    paused()
            if event.type == ADDENEMY:  # ADDENEMY is a custom event to add an enemy
                new_enemy = Enemy()
                enemies.add(new_enemy)
                allSprites.add(new_enemy)

        # if they beat the level
        if gameScore >= 2000:
            beatLevel3()
        # update the user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        for entity in allSprites:
            gameDisplay.blit(entity.surf, entity.rect)
        enemies.update()

        # This is for collision detection
        collide = pygame.sprite.spritecollideany(player, enemies)
        if collide:
            # If so, then remove the player and stop the loop
            LevelEnd()
        pygame.display.flip()
        clock.tick(60)


def level4():
    global gameScore
    global player
    global enemies
    gameScore = 0
    notLevelEnd()
    inLevel = True
    player = smallPlayer()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)

    while inLevel:

        # events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user hit the exit button
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # if user hit the p button
                    paused()
            if event.type == ADDENEMY:  # ADDENEMY is a custom event to add an enemy
                new_enemy = Enemy()
                enemies.add(new_enemy)
                allSprites.add(new_enemy)

        # if they beat the level
        if gameScore >= 3000:
            beatLevel4()
        # update the user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        for entity in allSprites:
            gameDisplay.blit(entity.surf, entity.rect)
        enemies.update()

        # This is for collision detection
        collide = pygame.sprite.spritecollideany(player, enemies)
        if collide:
            # If so, then remove the player and stop the loop
            LevelEnd()
        pygame.display.flip()
        clock.tick(60)


def level5():
    global gameScore
    global player
    global enemies
    gameScore = 0
    notLevelEnd()
    inLevel = True
    player = smallPlayer()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    allSprites.add(player)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)

    while inLevel:

        # events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user hit the exit button
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # if user hit the p button
                    paused()
            if event.type == ADDENEMY:  # ADDENEMY is a custom event to add an enemy
                new_enemy = Enemy()
                enemies.add(new_enemy)
                allSprites.add(new_enemy)

        # if they beat the level
        if gameScore >= 4000:
            beatLevel5()
        # update the user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        # blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(space, (0, 0))
        for entity in allSprites:
            gameDisplay.blit(entity.surf, entity.rect)
        enemies.update()

        # This is for collision detection
        collide = pygame.sprite.spritecollideany(player, enemies)
        if collide:
            # If so, then remove the player and stop the loop
            LevelEnd()
        pygame.display.flip()
        clock.tick(60)


# function to display screen after the first level is beaten
def beatLevel1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        center_display("CONGRATULATIONS!", 50, 50, casanova)
        center_display("You have beat Level 1", 50, 110, casanova)
        button('Next Level', 450, 400, 85, 28, white, 'level2')
        pygame.display.flip()


def beatLevel2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        center_display("CONGRATULATIONS!", 50, 50, casanova)
        center_display("You have beat Level 2", 50, 110, casanova)
        button('Next Level', 450, 400, 85, 28, white, 'level3')
        pygame.display.flip()


def beatLevel3():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        center_display("CONGRATULATIONS!", 50, 50, casanova)
        center_display("You have beat Level 3", 50, 110, casanova)
        button('Next Level', 450, 400, 85, 28, white, 'level4')
        pygame.display.flip()


def beatLevel4():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        center_display("CONGRATULATIONS!", 50, 50, casanova)
        center_display("You have beat Level 4", 50, 110, casanova)
        button('Next Level', 450, 400, 85, 28, white, 'level5')
        pygame.display.flip()


def beatLevel5():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        center_display("CONGRATULATIONS!", 50, 50, casanova)
        center_display("YOU BEAT THE GAME!", 50, 110, casanova)
        button('Home', 450, 400, 85, 28, white, 'mainMenu')
        pygame.display.flip()


###############################################################################
#SECTION FOR LESSONS


def lesson1():
    lesson = True
    while lesson:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        #declare a font
        smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
        #blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(lessonBackground, (0, 0))
        center_display("FUN FACTS!", LENGTH, 100, casanova)
        message_display("- Earth is the planet we live on ", 50, 200,
                        smallText, white)
        message_display(
            "- Out of all the planets in our solar system, Earth is the ", 50,
            250, smallText, white)
        message_display("  most dense.", 50, 270, smallText, white)
        message_display("- 70% of Earth's surface is covered by water", 50,
                        300, smallText, white)
        pygame.display.flip()
        #after 15 seconds, switch to the next slide
        time.sleep(15)
        lesson2()


def lesson2():
    lesson = True
    while lesson:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
        gameDisplay.fill(white)
        gameDisplay.blit(lessonBackground, (0, 0))
        center_display("Fun FACTS!", LENGTH, 100, casanova)
        message_display("- In our solar system, there are 8 planets", 50, 200,
                        smallText, white)
        message_display("- Pluto is not considered a planet anymore", 50, 250,
                        smallText, white)
        message_display("- In our solar system, there are 8 planets.", 50, 300,
                        smallText, white)
        message_display(
            "- The largest planet is Jupiter while the smallest is Mercury",
            50, 350, smallText, white)
        pygame.display.flip()
        time.sleep(15)
        lesson3()


def lesson3():
    lesson = True
    while lesson:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
        gameDisplay.fill(white)
        gameDisplay.blit(travellingToMars, (0, 0))
        center_display("FUN FACTS!", LENGTH, 100, casanova)
        message_display("-Saturn has 82 moons!", 50, 200, smallText, white)
        message_display("-99% of the solar systems weight comes from the sun",
                        50, 250, smallText, white)
        message_display("- The sun is the only star in the solar system", 50,
                        300, smallText, white)
        pygame.display.flip()
        time.sleep(15)
        lesson4()


def lesson4():
    lesson = True
    while lesson:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused()
        smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
        gameDisplay.fill(white)
        gameDisplay.blit(travellingToMars, (0, 0))
        center_display("FUN FACTS!", LENGTH, 100, casanova)
        message_display(
            "-Saturn is the only planet that would float on water.", 50, 200,
            smallText, white)
        message_display("- There are 5 dwarf planets, Pluto being one of them",
                        50, 250, smallText, white)
        button("Back", 450, 400, 100, 50, black, 'mainMenu')
        pygame.display.flip()


########################################################################################
#display the results from the quiz
def results():
    #declare a font
    smallText = pygame.font.Font('fonts/MandatoryPlaything-nRRd0.ttf', 15)
    results = True
    while results:
        #events loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(resultsBackground, (0, 0))
        #give an appropriate message based off of what their score was
        if finalScore == 7:
            center_display('Great Job!', LENGTH, 100, casanova)
            center_display('You got all of the questions correct!', LENGTH,
                           200, smallText)
            center_display('Yay!', LENGTH, 225, smallText)
        if finalScore == 6:
            center_display('Good Job!', LENGTH, 100, casanova)
            center_display('You got 5/6 of the questions correct!', LENGTH,
                           200, smallText)
            center_display('You\'re almost there!', LENGTH, 225, smallText)
        if finalScore == 5:
            center_display('Close!', LENGTH, 100, casanova)
            center_display('You got 4/6 of the questions right!', LENGTH, 200,
                           smallText)
            center_display('Keep working and you\'ll get there!', LENGTH, 225,
                           smallText)
        if finalScore == 4:
            center_display('Almost!', LENGTH, 100, casanova)
            center_display('You got half of the questions correct.', LENGTH,
                           200, smallText)
            center_display('You should go back and review the lesson!', LENGTH,
                           225, smallText)
        if finalScore == 3:
            center_display('Oh no!', LENGTH, 100, casanova)
            center_display('You only got 2 of the 6 questions correct.',
                           LENGTH, 200, smallText)
            center_display('You need to improve your knowledge!', LENGTH, 225,
                           smallText)
        if finalScore == 2:
            center_display('Oh no!', LENGTH, 100, casanova)
            center_display('You only got 1 of the 6 questions correct.',
                           LENGTH, 200, smallText)
            center_display('You need to improve your knowledge!', LENGTH, 225,
                           smallText)
            center_display('Go back and read through the lesson.', LENGTH, 250,
                           smallText)
        if finalScore == 1:
            center_display('Oh no!', LENGTH, 100, casanova)
            center_display('You got no questions right!', LENGTH, 200,
                           smallText)
            center_display('You need to improve your knowledge!', LENGTH, 225,
                           smallText)
            center_display('Go back and read through the lesson.', LENGTH, 250,
                           smallText)
        if finalScore == 0:
            center_display('Hey!', LENGTH, 100, casanova)
            center_display('You didn\'t take the test yet!', LENGTH, 200,
                           smallText)
            center_display('What are you waiting for?', LENGTH, 250, smallText)
        button('Back', 100, 400, 100, 25, black, 'mainMenu')
        pygame.display.flip()
        clock.tick(60)


# function for the main menu
def mainMenu():
    notLevelEnd()
    #increase recursion limit
    x = 10000000
    sys.setrecursionlimit(x)
    running = True
    while running:
        #events loop
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #blit everything to the screen
        gameDisplay.fill(white)
        gameDisplay.blit(mainMenuBackground, (0, 0))
        center_display("SPACE", 50, 50)
        center_display("SHOOTERS", 50, 110)
        button('LEARN!', 270, 250, 110, 28, black, 'lesson1')
        button('Game', 170, 300, 90, 28, black, 'game')
        button('Quiz', 400, 300, 75, 28, black, 'quiz')
        button('How To Play', 230, 350, 200, 28, black, 'howToPlay')
        button('Results', 144, 400, 145, 28, black, 'results')
        button('Exit', 400, 400, 75, 28, black, 'exit')
        pygame.display.flip()
        clock.tick(60)


# function to start the program loop
def programLoop():
    programLoop = True
    while programLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                programLoop = False
        titleScreen()


# Run the program
programLoop()
pygame.quit()
quit()
