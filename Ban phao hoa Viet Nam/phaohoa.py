import pygame
import random
import math

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fireworks with Vietnamese Flag")

# Màu sắc
white = (255, 255, 255)
red = (255, 0, 0)

# Hình cờ Việt Nam
flag = pygame.image.load("vietnamflag.png")  # Đường dẫn đến hình cờ Việt Nam

# Lớp đại diện cho pháo hoa
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.explosion_radius = 150
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particles = []

    def explode(self):
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            self.particles.append([self.x, self.y, math.cos(angle) * speed, math.sin(angle) * speed])

    def draw(self):
        for particle in self.particles:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[3] += 0.1
            pygame.draw.circle(screen, self.color, (int(particle[0]), int(particle[1])), 3)

# Danh sách các pháo hoa
fireworks = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            fireworks.append(Firework(event.pos[0], event.pos[1]))

    screen.fill(white)

    for firework in fireworks:
        if not firework.particles:
            firework.explode()
        firework.draw()

    # Hiển thị hình cờ Việt Nam
    screen.blit(flag, (width - flag.get_width(), height - flag.get_height()))

    pygame.display.flip()

pygame.quit()
