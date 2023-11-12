import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Tạo màn hình game
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Load ảnh nhân vật và chướng ngại vật
player_image = pygame.image.load("coin_gold.png").convert()
obstacle_image = pygame.image.load("carrot.png").convert()

# Thiết lập vị trí ban đầu của nhân vật
player_rect = player_image.get_rect()
player_rect.centerx = screen_width // 2
player_rect.bottom = screen_height - 10

# Thiết lập tốc độ di chuyển của nhân vật
player_speed = 5

# Tạo đối tượng nhân vật
class Player(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def update(self):
        # Kiểm tra phím mũi tên và di chuyển nhân vật
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= player_speed
            if self.rect.left < 0:
                self.rect.left = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += player_speed
            if self.rect.right > screen_width:
                self.rect.right = screen_width
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= player_speed
            if self.rect.top < 0:
                self.rect.top = 0
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += player_speed
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

# Tạo đối tượng chướng ngại vật
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect
        self.speed = random.randint(3, 8)

    def update(self):
        # Di chuyển chướng ngại vật xuống dưới màn hình
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.kill()

# Tạo group cho nhân vật và chướng ngại vật
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Thêm nhân vật và chướng ngại vật vào group
player = Player(player_image, player_rect)
all_sprites.add(player)

# Tạo chướng ngại vật mới mỗi 1 giây
obstacle_timer = pygame.time.get_ticks()
obstacle_interval = 1000

# Biến đếm số chướng ngại vật đã né được
score = 0

# Vòng lặp chính của game
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tạo chướng ngại vật mới
    now = pygame