# Import needed libraries
import random
import pygame as pg
import sys

# Initiate pyGame
pg.init()

# Set default colours
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Set window size
size = width, height = 400, 400
screen = pg.display.set_mode(size)

# Define message
def message(msg, w, h):
    screen.blit(pg.font.SysFont(None, 30).render(msg, True, green), [width / w, height / h])
    pg.display.update()

while True:
    # Setting inital positions
    xPos = 200
    yPos = 200
    square = 20
    xSnake = [xPos]
    ySnake = [yPos]
    snakeLength = 1

    # Setting initial conditions
    apple = False
    gameOver = False
    randomx = 0
    randomy = 0
    score = 0
    pauseGame = False
    gameEnd = False

    # Movement
    xChange = 0
    yChange = 0
    speed = 10

    # Loop for game
    while gameEnd == False:

        # Spawn new apple
        if apple == False or gameOver == True:
            randomx = round(random.randrange(square, width - square) / square) * square
            randomy = round(random.randrange(square, height - square) / square) * square

            # Check to make sure apple not spawned on snake
            if round(xPos / square) != round(randomx / square) and round(yPos / square) != round(randomy / square):
                apple = True
        
        # Check if apples are eaten
        if xPos == randomx and yPos == randomy:
            apple = False
            score += 1
            speed += 1

            xSnake.append(xPos - xChange)
            ySnake.append(yPos - yChange)
            snakeLength += 1

        # Set border
        if xPos >= width or xPos < 0 or yPos >= height or yPos < 0:
            gameOver = True

        # Ending condition
        if gameOver == True:
            screen.fill(black)
            message("Q = Quit, R = Retry", 4, 4)

        # Event loop
        if gameOver == False:
            for event in pg.event.get():
                # Quit
                if event.type == pg.QUIT:
                    sys.exit()
                
                # Change directions
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        xChange = 0
                        yChange = -20
                    elif event.key == pg.K_DOWN:
                        xChange = 0
                        yChange = 20
                    elif event.key == pg.K_RIGHT:
                        xChange = 20
                        yChange = 0
                    elif event.key == pg.K_LEFT:
                        xChange = -20
                        yChange = 0
                    # Create pause menu
                    elif event.key == pg.K_ESCAPE:
                        pauseGame = True
                        while pauseGame == True:
                            screen.fill(black)
                            message("Score: " + str(score), 10, 10)
                            message("Q = Quit, C = Continue", 4, 4)
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    sys.exit()
                                elif event.type == pg.KEYDOWN:
                                    if event.key == pg.K_q:
                                        sys.exit()
                                    elif event.key == pg.K_c:
                                        pauseGame = False
            
            
        while gameOver == True:
            # Quit or restart
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        sys.exit()
                    if event.key == pg.K_r:
                        gameOver = False
                        gameEnd = True
        
        # Movement
        xPos += xChange
        yPos += yChange
        xSnake.append(xPos)
        ySnake.append(yPos)

        # Remove end of snake
        while len(xSnake) > snakeLength:
            del xSnake[0] 
            del ySnake[0]

        # Check for overlapping
        for i in range(snakeLength - 1):
            if (xSnake[snakeLength - 1] == xSnake[i] and ySnake[snakeLength - 1] == ySnake[i]):
                gameOver = True

        # Refresh screen
        screen.fill(black)
        for i in range(snakeLength):
            pg.draw.rect(screen, green, [xSnake[i], ySnake[i], square, square])
        pg.draw.rect(screen, red, [randomx, randomy, square, square])
        message("Score: " + str(score), 10, 10)

        pg.time.Clock().tick(speed)