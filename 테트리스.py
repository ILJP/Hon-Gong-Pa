import pygame
import random

pygame.init()

# 게임 화면 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# 블록 크기
BLOCK_SIZE = 40

# 블록의 모양 정보
BLOCKS = [
    [[1, 1, 1], [0, 1, 0]],  # ㅡ 모양
    [[0, 2, 2], [2, 2, 0]],  # ㄱ 모양
    [[3, 3, 0], [0, 3, 3]],  # ㄴ 모양
    [[4, 0, 0], [4, 4, 4]],  # ㅁ 모양
    [[0, 5, 5], [5, 5, 0]],  # z 모양
    [[6, 6, 6, 6]],  # ㅡ 모양
    [[0, 7], [0, 7], [0, 7], [0, 7]]  # ㅣ 모양
]

# 색깔 정보
COLORS = [
    (0, 0, 0),    # 검정
    (0, 255, 255),  # 청록색
    (255, 165, 0),  # 주황색
    (255, 255, 0),  # 노란색
    (0, 255, 0),  # 초록색
    (128, 0, 128),  # 보라색
    (255, 0, 0),  # 빨간색
    (0, 0, 255)  # 파란색
]

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 블록 클래스
class Block:
    def __init__(self, shape):
        self.shape = shape  # 블록 모양 정보
        self.color = random.randint(1, len(COLORS) - 1)  # 색깔
        self.x = SCREEN_WIDTH // 2  # 시작 위치
        self.y = 0

    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] > 0:
                    pygame.draw.rect(screen, COLORS[self.color],
                                     (self.x + j * BLOCK_SIZE, self.y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip)
