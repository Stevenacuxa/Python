import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vibora Persiguiendo Manzanas')

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Tamaño de la celda de la cuadrícula (dimensiones de la vibora y manzanas)
CELL_SIZE = 20

# Crear la clase de la serpiente
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # La serpiente empieza en el centro
        self.direction = 'RIGHT'  # Dirección inicial
        self.growing = False  # La serpiente no crece al principio
        self.target_x = self.body[0][0]
        self.target_y = self.body[0][1]
        self.speed = 10  # Velocidad de movimiento de la serpiente

    def update(self, mouse_pos):
        # Ajustar el "retraso" para el movimiento hacia el mouse
        head_x, head_y = self.body[0]

        # Mover la serpiente hacia el punto objetivo (mouse) con retraso
        if head_x < self.target_x:
            head_x += self.speed
        elif head_x > self.target_x:
            head_x -= self.speed

        if head_y < self.target_y:
            head_y += self.speed
        elif head_y > self.target_y:
            head_y -= self.speed
        
        # Establecer el objetivo para el siguiente movimiento
        self.target_x = mouse_pos[0]
        self.target_y = mouse_pos[1]

        # Mover el cuerpo de la serpiente
        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]  # No eliminar el segmento de la cola al moverse

        # Si la serpiente está creciendo, agregar una nueva sección al final
        if self.growing:
            self.body.append(self.body[-1])  # No eliminamos segmentos, solo añadimos al final
            self.growing = False

    def grow(self):
        self.growing = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Crear la clase de la manzana
class Apple:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        self.y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE))

# Función principal del juego
def game():
    # Inicialización
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()
    score = 0
    running = True
    paused = False  # Variable para controlar el estado de pausa
    congratulations_displayed = False  # Para evitar que el mensaje se muestre más de una vez

    while running:
        screen.fill(WHITE)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused  # Pausar o continuar al presionar "P"

        # Si el juego está pausado, mostrar el mensaje y no hacer nada más
        if paused:
            font = pygame.font.SysFont('Arial', 50)
            pause_text = font.render('PAUSADO. Pulsa P para continuar', True, BLACK)
            screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            continue  # Salir de este ciclo y esperar a que se presione "P" nuevamente

        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Actualizar la serpiente
        snake.update(mouse_pos)

        # Comprobar si la serpiente toca los bordes
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False  # Terminar el juego si la serpiente toca un borde

        # Comprobar si la serpiente come una manzana
        if snake.body[0] == (apple.x, apple.y):
            apple = Apple()  # Generar una nueva manzana aleatoria
            snake.grow()  # Hacer que la serpiente crezca
            score += 1  # Aumentar el puntaje

        # Dibujar la serpiente y la manzana
        snake.draw()
        apple.draw()

        # Mostrar el puntaje
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f'Puntaje: {score}', True, BLACK)
        screen.blit(score_text, (20, 20))

        # Mostrar mensaje de felicitaciones al alcanzar 10 puntos
        if score >= 10 and not congratulations_displayed:
            congratulations_font = pygame.font.SysFont('Arial', 50)
            congratulations_text = congratulations_font.render('¡Felicidades! Has alcanzado 10 puntos!', True, BLACK)
            screen.blit(congratulations_text, (WIDTH // 2 - congratulations_text.get_width() // 2, HEIGHT // 2))
            congratulations_displayed = True  # Evitar que se muestre más de una vez

        # Actualizar la pantalla
        pygame.display.update()

        # Limitar los FPS
        clock.tick(15)

    # Finalizar el juego
    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    game()
