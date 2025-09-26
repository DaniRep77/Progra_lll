import pygame
import sys
import math
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Serpiente Seguidora de Mouse")

# Colores
BACKGROUND = (10, 10, 40)
SNAKE_HEAD = (0, 255, 100)
SNAKE_BODY = (0, 200, 80)
TRAIL = (0, 150, 60, 50)  # Con transparencia
MOUSE_COLOR = (255, 100, 100)
TEXT_COLOR = (255, 255, 255)


# Clase para la serpiente
class Snake:
    def __init__(self):
        self.segments = []
        self.length = 20
        self.speed = 4
        self.max_speed = 8
        self.growth_rate = 0.2

        # Inicializar segmentos
        for i in range(self.length):
            self.segments.append([WIDTH // 2, HEIGHT // 2])

    def update(self, target_x, target_y):
        # Mover la cabeza hacia el objetivo (mouse)
        head_x, head_y = self.segments[0]

        # Calcular ángulo hacia el objetivo
        angle = math.atan2(target_y - head_y, target_x - head_x)

        # Mover la cabeza
        self.segments[0][0] += math.cos(angle) * self.speed
        self.segments[0][1] += math.sin(angle) * self.speed

        # Mover los segmentos del cuerpo
        for i in range(1, self.length):
            seg_x, seg_y = self.segments[i]
            prev_x, prev_y = self.segments[i - 1]

            # Calcular ángulo hacia el segmento anterior
            angle = math.atan2(prev_y - seg_y, prev_x - seg_x)

            # Distancia al segmento anterior
            dist = math.sqrt((prev_x - seg_x) ** 2 + (prev_y - seg_y) ** 2)

            # Mover el segmento si está demasiado lejos
            if dist > 8:
                self.segments[i][0] += math.cos(angle) * (dist - 6)
                self.segments[i][1] += math.sin(angle) * (dist - 6)

    def draw(self, surface):
        # Dibujar el cuerpo
        for i, (x, y) in enumerate(self.segments):
            if i == 0:
                # Cabeza
                pygame.draw.circle(surface, SNAKE_HEAD, (int(x), int(y)), 12)
                # Ojos
                angle = math.atan2(self.segments[0][1] - self.segments[1][1],
                                   self.segments[0][0] - self.segments[1][0])
                eye1_x = x + math.cos(angle + 0.3) * 8
                eye1_y = y + math.sin(angle + 0.3) * 8
                eye2_x = x + math.cos(angle - 0.3) * 8
                eye2_y = y + math.sin(angle - 0.3) * 8
                pygame.draw.circle(surface, (255, 255, 255), (int(eye1_x), int(eye1_y)), 4)
                pygame.draw.circle(surface, (255, 255, 255), (int(eye2_x), int(eye2_y)), 4)
            else:
                # Cuerpo (más delgado hacia la cola)
                size = max(10 - i * 0.3, 3)
                pygame.draw.circle(surface, SNAKE_BODY, (int(x), int(y)), int(size))

        # Dibujar estela
        for i in range(1, len(self.segments)):
            alpha = 150 - i * 5
            if alpha < 0:
                alpha = 0
            trail_color = (0, 150, 60, alpha)
            trail_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, trail_color, (10, 10), 8 - i * 0.2)
            surface.blit(trail_surface, (self.segments[i][0] - 10, self.segments[i][1] - 10))


# Función principal
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 24)

    # Partículas
    particles = []

    running = True
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Añadir longitud al presionar espacio
                    snake.length += 5

        # Actualizar serpiente
        snake.update(mouse_x, mouse_y)

        # Añadir partículas aleatorias
        if random.random() < 0.3:
            particles.append({
                'x': random.randint(0, WIDTH),
                'y': random.randint(0, HEIGHT),
                'size': random.randint(2, 6),
                'color': (random.randint(100, 200), random.randint(200, 255), random.randint(100, 200)),
                'life': random.randint(20, 50)
            })

        # Actualizar partículas
        for p in particles:
            p['life'] -= 1

        # Eliminar partículas muertas
        particles = [p for p in particles if p['life'] > 0]

        # Dibujar fondo
        screen.fill(BACKGROUND)

        # Dibujar partículas
        for p in particles:
            pygame.draw.circle(screen, p['color'], (int(p['x']), int(p['y'])), p['size'])

        # Dibujar serpiente
        snake.draw(screen)

        # Dibujar objetivo (mouse)
        pygame.draw.circle(screen, MOUSE_COLOR, (mouse_x, mouse_y), 8)
        pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 8, 2)

        # Dibujar información
        length_text = font.render(f"Longitud: {snake.length}", True, TEXT_COLOR)
        screen.blit(length_text, (10, 10))

        help_text = small_font.render("Presiona ESPACIO para crecer - ESC para salir", True, TEXT_COLOR)
        screen.blit(help_text, (10, HEIGHT - 30))

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main() 