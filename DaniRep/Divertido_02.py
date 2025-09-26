import pygame
import sys
import math
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌸 Generador de Flores Coloridas")

# Colores
BACKGROUND = (10, 15, 30)
COLORS = [
    (255, 100, 100),  # Rojo
    (255, 150, 50),  # Naranja
    (255, 200, 50),  # Amarillo
    (100, 255, 100),  # Verde
    (50, 200, 255),  # Azul
    (200, 100, 255),  # Púrpura
    (255, 100, 255),  # Rosa
]


# Clase para pétalos de flor
class Petal:
    def __init__(self, x, y, size, color, angle):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.angle = angle
        self.original_size = size
        self.pulse_speed = random.uniform(0.05, 0.1)
        self.pulse_factor = 0

    def update(self):
        # Animación de pulsación
        self.pulse_factor += self.pulse_speed
        self.size = self.original_size * (1 + 0.1 * math.sin(self.pulse_factor))

    def draw(self, surface):
        # Dibujar un pétalo elíptico
        points = []
        for i in range(8):
            angle = self.angle + (i * math.pi / 4)
            dx = math.cos(angle) * self.size
            dy = math.sin(angle) * (self.size * 0.5)
            points.append((self.x + dx, self.y + dy))

        pygame.draw.polygon(surface, self.color, points)
        pygame.draw.polygon(surface, (255, 255, 255, 50), points, 2)


# Clase para la flor completa
class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.petals = []
        self.center_color = random.choice(COLORS)
        self.center_size = random.randint(15, 25)
        self.petal_count = random.randint(6, 12)
        self.petal_size = random.randint(30, 50)
        self.petal_color = random.choice(COLORS)

        # Crear pétalos
        for i in range(self.petal_count):
            angle = (i * 2 * math.pi / self.petal_count)
            self.petals.append(Petal(x, y, self.petal_size, self.petal_color, angle))

    def update(self):
        for petal in self.petals:
            petal.update()

    def draw(self, surface):
        # Dibujar pétalos
        for petal in self.petals:
            petal.draw(surface)

        # Dibujar centro de la flor
        pygame.draw.circle(surface, self.center_color, (int(self.x), int(self.y)), self.center_size)

        # Detalles en el centro
        for i in range(8):
            angle = i * math.pi / 4
            dx = math.cos(angle) * (self.center_size * 0.7)
            dy = math.sin(angle) * (self.center_size * 0.7)
            pygame.draw.circle(surface, (255, 255, 100),
                               (int(self.x + dx), int(self.y + dy)),
                               self.center_size // 4)


# Clase para partículas (polen)
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = random.choice(COLORS)
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2 * math.pi)
        self.life = 100

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1

    def draw(self, surface):
        alpha = min(255, self.life * 2)
        color_with_alpha = (*self.color, alpha)
        particle_surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(particle_surface, color_with_alpha, (self.size, self.size), self.size)
        surface.blit(particle_surface, (int(self.x - self.size), int(self.y - self.size)))


# Función principal
def main():
    clock = pygame.time.Clock()
    flowers = []
    particles = []
    font = pygame.font.SysFont(None, 36)

    # Crear algunas flores iniciales
    for _ in range(5):
        flowers.append(Flower(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_c:
                    # Limpiar flores
                    flowers = []
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Crear una nueva flor donde se hace clic
                x, y = pygame.mouse.get_pos()
                flowers.append(Flower(x, y))

                # Crear partículas de polen
                for _ in range(20):
                    particles.append(Particle(x, y))

        # Actualizar flores
        for flower in flowers:
            flower.update()

        # Actualizar partículas
        for particle in particles:
            particle.update()

        # Eliminar partículas muertas
        particles = [p for p in particles if p.life > 0]

        # Añadir partículas aleatorias
        if random.random() < 0.1 and flowers:
            random_flower = random.choice(flowers)
            particles.append(Particle(random_flower.x, random_flower.y))

        # Dibujar fondo
        screen.fill(BACKGROUND)

        # Dibujar partículas
        for particle in particles:
            particle.draw(screen)

        # Dibujar flores
        for flower in flowers:
            flower.draw(screen)

        # Dibujar instrucciones
        instructions = font.render("Haz clic para crear una flor - C para limpiar - ESC para salir", True,
                                   (200, 200, 255))
        screen.blit(instructions, (10, HEIGHT - 40))

        # Dibujar contador de flores
        count_text = font.render(f"Flores: {len(flowers)}", True, (200, 255, 200))
        screen.blit(count_text, (10, 10))

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()