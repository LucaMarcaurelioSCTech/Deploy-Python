import pygame
import sys
import random

# 1. Inizializzazione
pygame.init()

# Setup dello schermo
WIDTH, HEIGHT = 600, 400
schermo = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Prima Versione")

# Colori
ROSSO = (255, 0, 0)
NERO = (0, 0, 0)
VERDE = (0, 255, 0)


BLOCK_SIZE = 20 

x_quadrato = WIDTH / 2  
y_quadrato = HEIGHT / 2


cambio_x = 0
cambio_y = 0


velocita = BLOCK_SIZE 

PUNTEGGIO = 0
x_cibo = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
y_cibo = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

# Clock
clock = pygame.time.Clock()

snake_body = []
lunghezza_snake = 1

# --- IL GAME LOOP ---
while True:
    # A. Gestione Eventi (Input)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            # FRECCIA SINISTRA
            if evento.key == pygame.K_LEFT:
                if cambio_x == 0: 
                    cambio_x = -velocita
                    cambio_y = 0

            # FRECCIA DESTRA
            elif evento.key == pygame.K_RIGHT:
                if cambio_x == 0:
                    cambio_x = velocita
                    cambio_y = 0

            # FRECCIA SU
            elif evento.key == pygame.K_UP:
                if cambio_y == 0: 
                    cambio_x = 0
                    cambio_y = -velocita

            
            elif evento.key == pygame.K_DOWN:
                if cambio_y == 0:
                    cambio_x = 0
                    cambio_y = velocita

    
    x_quadrato += cambio_x
    y_quadrato += cambio_y

    testa_react = pygame.Rect(x_quadrato,y_quadrato, BLOCK_SIZE , BLOCK_SIZE)

    snake_body.append(testa_react)

    cibo_react = pygame.Rect(x_cibo,y_cibo, BLOCK_SIZE , BLOCK_SIZE)

    if (testa_react.colliderect(cibo_react)):
        lunghezza_snake +=1
        x_cibo = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y_cibo = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        PUNTEGGIO +=1
        print(PUNTEGGIO)

    


    if (len(snake_body) > lunghezza_snake):
        del snake_body[0]

    for i in snake_body[:-1]:
        if (testa_react.colliderect(i)):
            print("Hai perso coglione")
            pygame.quit()
            sys.exit()
        if x_quadrato < 0 or x_quadrato >= WIDTH or y_quadrato < 0 or y_quadrato >= HEIGHT:
            print("Hai perso!") 
            pygame.quit()
            sys.exit()       
    
    schermo.fill(NERO) 
    
    for pezzo in snake_body:
        pygame.draw.rect(schermo, ROSSO, pezzo)
    
    
    pygame.draw.rect(schermo, VERDE, (x_cibo, y_cibo, BLOCK_SIZE, BLOCK_SIZE))
    
    pygame.display.flip()

    # D. Controllo FPS
    clock.tick(20)