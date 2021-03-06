import pygame

pygame.init()
#Colores
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
size_screen = (800,600)
ancho_jugador = 15
alto_jugador = 90

#Generar pantalla
pantalla = pygame.display.set_mode(size_screen)
#Reloj:FPS
reloj = pygame.time.Clock()
#Coordenadas player1
player1_x = 50
player1_y = 300 - (alto_jugador//2)
#Coordenadas player2
player2_x = 750 - ancho_jugador
player2_y = 300 - (alto_jugador//2)
#Movimientos de players
mov_p1 = 0
mov_p2 = 0
#Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
mov_pelota_x = 3
mov_pelota_y = 3
#Flag: Bandera fin del juego
game_over = False
#Puntajes
puntaje_p1 = 0
puntaje_p2 = 0
#Fuente
font = pygame.font.SysFont('impact.ttf',30)
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT :
            game_over = True
        #Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            #Player1
            if evento.key == pygame.K_w:
                mov_p1 = -4
            if evento.key == pygame.K_s:
                mov_p1 = 4
            #Player2
            if evento.key == pygame.K_UP:
                mov_p2 = -4
            if evento.key == pygame.K_DOWN:
                mov_p2 = 4
        #Si se deja de presionar la tecla
        if evento.type == pygame.KEYUP:
            #Player1
            if evento.key == pygame.K_w:
                mov_p1 = 0
            if evento.key == pygame.K_s:
                mov_p1 = 0
            #Player2
            if evento.key == pygame.K_UP:
                mov_p2 = 0
            if evento.key == pygame.K_DOWN:
                mov_p2 = 0
    #Validación de la pelota
    if pelota_y > 590 or pelota_y < 10:
        mov_pelota_y *= -1
    #Si la pelota se va por extremo derecho o izquierdo
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        puntaje_p1 += 1
        #Si sale de pantalla
        mov_pelota_x *= -1
        mov_pelota_y *= -1
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        puntaje_p2 += 1
        # Si sale de pantalla
        mov_pelota_x *= -1
        mov_pelota_y *= -1
    #Texto puntajes
    texto_p1 = font.render('PLAYER1: {}'.format(puntaje_p1), True, white)
    texto_p2 = font.render('PLAYER2: {}'.format(puntaje_p2), True, white)
    #Texto Game Over
    texto_game_over = font.render('GAME OVER', True, white)
    #Mover jugadores
    player1_y += mov_p1
    player2_y += mov_p2
    #Mover pelota
    pelota_x += mov_pelota_x
    pelota_y += mov_pelota_y
    #Dibujo
    pantalla.fill((black))
    #Dibujar player1
    player_1 = pygame.draw.rect(pantalla,white,(player1_x,player1_y,ancho_jugador,alto_jugador))
    #Dibujar player2
    player_2 = pygame.draw.rect(pantalla,white,(player2_x, player2_y, ancho_jugador, alto_jugador))
    #Dibujar pelota
    pelota = pygame.draw.circle(pantalla,white,(pelota_x,pelota_y),10)
    #Dibujar texto
    pantalla.blit(texto_p1, (10,10))
    pantalla.blit(texto_p2,(680,10))
    #Colisiones
    if pelota.colliderect(player_1) or pelota.colliderect(player_2):
        mov_pelota_x *= -1
    pygame.display.flip()
    reloj.tick(120)
    #Game over
    if puntaje_p1 == 10 or puntaje_p2 == 10:
        break
pygame.quit()
