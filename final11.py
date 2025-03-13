import pygame

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Fútbol")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Jugadores
player1 = pygame.Rect(50, HEIGHT//2 - 20, 20, 40)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 20, 20)

# Barra de gol
goal_bar = pygame.Rect(0, HEIGHT//3, 10, HEIGHT//3)

# Velocidades
player1_speed = 3  # Reducida la velocidad del jugador
ball_speed_x, ball_speed_y = 4, 4

# Marcador
score = 0
font = pygame.font.Font(None, 36)

game_active = True
paused = False

# Cargar sonido de gol
#goal_sound = pygame.mixer.Sound("goal.wav")

clock = pygame.time.Clock()

# Bucle del juego
running = True
while running:
    screen.fill(GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pausar con 'P'
                paused = not paused
    
    if not paused and game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player1.top > 0:
            player1.y -= player1_speed
        if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
            player1.y += player1_speed
        
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        
        # Rebote en bordes superior e inferior
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
        
        # Rebote en bordes laterales
        if ball.right >= WIDTH:
            ball_speed_x *= -1
        
        # Rebote en el jugador
        if ball.colliderect(player1):
            ball_speed_x *= -1
        
        # Gol solo si la pelota entra en la barra blanca
        if ball.left <= 0 and goal_bar.top <= ball.centery <= goal_bar.bottom:
            score += 1
            #goal_sound.play()
            ball.x, ball.y = WIDTH//2, HEIGHT//2
            if score >= 10:
                game_active = False
        elif ball.left <= 0:
            ball_speed_x *= -1  # Si no entra en la barra, rebota
        
        # Dibujar
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.ellipse(screen, RED, ball)
        pygame.draw.rect(screen, WHITE, goal_bar)  # Dibujar barra de gol
    
    # Mostrar marcador
    score_text = font.render(f"Goles: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if not game_active:
        game_over_text = font.render("¡Fin del Juego! Presiona R para reiniciar", True, WHITE)
        screen.blit(game_over_text, (WIDTH//4, HEIGHT//2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            score = 0
            game_active = True
            ball.x, ball.y = WIDTH//2, HEIGHT//2
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

