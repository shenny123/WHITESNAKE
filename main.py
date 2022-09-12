import pygame
from GameObject import *
pygame.init()
screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("background.jpg").convert()
app = pygame.image.load("lingzhi.png").convert()
app.set_colorkey((0,0,0))
snakeHead = pygame.image.load("snakehead.png").convert()
snakeBody = pygame.image.load("snakebody.png").convert()


screen.blit(background, (0,0))
objects = []


apple = Apple(app, screen_width, screen_height)

head = Head(snakeHead, screen_width, screen_height)

bodies = []

score = 0

run = True
gameOver = False
font = pygame.font.SysFont('yugothic', 24)
font2 = pygame.font.SysFont('yugothic', 48)

def get_gameOverText(score):
    gameOverText = font.render('GAME OVER! SCORE: ' + str(score),True, (255, 255, 255) )
    return gameOverText

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                head.up()
            elif event.key == pygame.K_DOWN:
                head.down()
            elif event.key == pygame.K_LEFT:
                head.left()
            elif event.key == pygame.K_RIGHT:
                head.right()

    img = font.render("SCORE: " + str(score), True, (255, 255, 255))

    if gameOver: screen.blit(background, (0,0))
    else:
        for b in bodies:
            screen.blit(background, b.pos, b.pos)
        screen.blit(background, apple.pos, apple.pos)
        screen.blit(background, head.pos, head.pos)
        screen.blit(background, img.get_rect().move(20,20), img.get_rect().move(20,20))


    #check collisions

    if pygame.Rect.colliderect(head.pos,apple.pos):

        apple.respawn()
        #makes sures apple does not respawn on the snake
        for b in bodies:
            while pygame.Rect.colliderect(b.pos, apple.pos):
                apple.respawn()

        score += 1

        if len(bodies) == 0:
            bodies.append(Body(snakeBody,
                               head.pos.topleft[0],
                               head.pos.topleft[1] ))
        else:
            bodies.append(Body(snakeBody,
                               bodies[-1].pos.topleft[0],
                               bodies[-1].pos.topleft[1]))

    for key, b in enumerate(bodies):
        if key == 0:
            b.nextdx = head.dx
            b.nextdy = head.dy
        else:
            b.nextdx = bodies[key-1].dx
            b.nextdy = bodies[key-1].dy
        b.move()

    for b in bodies:
        b.dx = b.nextdx
        b.dy = b.nextdy
        screen.blit(b.image, b.pos)
        if pygame.Rect.colliderect(head.pos.move(head.dx,head.dy), b.pos):
            print("game over!! Your score was ", score)
            gameOver = True
    if head.pos.top < 0 or head.pos.bottom > screen_height or head.pos.left < 0 or head.pos.right > screen_width:
        gameOver = True

    head.move()
    if gameOver:

        screen.blit(get_gameOverText(score), (screen_width/4, screen_height/4))
        bodies.clear()
    else:
        screen.blit(apple.image, apple.pos)
        screen.blit(head.image, head.pos)
        screen.blit(img, (20, 20))



    pygame.event.pump()
    pygame.display.update()
    pygame.time.delay(300)


quit()