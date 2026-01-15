import pygame 
import sys
import random

# 1. Inizializzazione
pygame.init()

# Setup dello schermo
WIDTH, HEIGHT = 500, 400
schermo = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Il mio gioco Pygame")

# Colori e coordinate
ROSSO = (255, 0, 0)
NERO = (0, 0, 0)
x_quadrato = 50
y_quadrato = 50
velocita = 5



verde = (0 , 255, 0)
x_cibo = random.randint(0,400)
y_cibo = random.randint(0,400)

# Clock per gestire gli FPS
clock = pygame.time.Clock()

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
                # La tua logica "flag": Posso andare a sx solo se NON vado a dx
                # La logica "codice": Posso cambiare la X solo se la X è ferma (quindi mi muovo su Y)
                if cambio_x == 0: 
                    cambio_x = -velocita
                    cambio_y = 0

            # FRECCIA DESTRA
            elif evento.key == pygame.K_RIGHT:
                if cambio_x == 0: # Accetto il comando solo se non mi sto già muovendo in orizzontale
                    cambio_x = velocita
                    cambio_y = 0

            # FRECCIA SU
            elif evento.key == pygame.K_UP:
                if cambio_y == 0: # Accetto il comando solo se mi sto muovendo in orizzontale
                    cambio_x = 0
                    cambio_y = -velocita

            # FRECCIA GIÙ
            elif evento.key == pygame.K_DOWN:
                if cambio_y == 0:
                    cambio_x = 0
                    cambio_y = velocita
    # B. Logica (Input continuo e Movimento)
    """
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_RIGHT]:
        x_quadrato += velocita*3
    if tasti[pygame.K_LEFT]:
        x_quadrato -= velocita*3
    if tasti[pygame.K_DOWN]:
        y_quadrato += velocita*3
    if tasti[pygame.K_UP]:
        y_quadrato -= velocita*3
    """
        
    # C. Disegno (Rendering)
    schermo.fill(NERO) # 1. Pulisci lo schermo (altrimenti lasci la scia!)
    pygame.draw.rect(schermo, ROSSO, (x_quadrato, y_quadrato, 40, 40)) # 2. Disegna il quadrato
    pygame.draw.rect(schermo,verde,(x_cibo,y_cibo, 40 , 40))
    pygame.display.flip() # 3. Aggiorna il display ("Invia" l'immagine all'utente)

    x_quadrato += cambio_x
    y_quadrato += cambio_y

    # D. Controllo FPS
    clock.tick(2) 