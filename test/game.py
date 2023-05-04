import pygame  
import random  
  
# 初始化 Pygame  
pygame.init()  
  
# 设置游戏窗口的大小和标题  
screen = pygame.display.set_mode((800, 600))  
pygame.display.set_caption("推箱子游戏")  
  
# 定义游戏元素的大小和颜色  
block_size = 20  
block_color = (0, 0, 0)  
  
# 定义游戏元素的初始位置和状态  
blocks = []  
player_block = []  
player_position = []  
  
# 定义游戏元素的旋转角度和速度  
player_angle = 0  
player_speed = 5  
  
# 定义游戏元素的碰撞检测函数  
def check_collision(block1, block2):  
    x1, y1 = block1  
    x2, y2 = block2  
    x3, y3 = player_position[0]  
    x4, y4 = player_position[1]  
  
    if (x1 >= x3 and x1 <= x3 + block_size and  
        y1 >= y3 and y1 <= y3 + block_size and  
        x2 >= x4 and x2 <= x4 + block_size and  
        y2 >= y4 and y2 <= y4 + block_size):  
        return True  
    else:  
        return False  
  
# 定义游戏元素的移动函数  
def move_block(block):  
    if block == player_block:  
        return  
  
    if check_collision(block, player_block):  
        return  
  
    player_block.append(block)  
    player_position.append((player_position[0] + block[0], player_position[1] + block[1]))  
  
    if len(player_block) > 10:  
        player_block.pop()  
  
# 定义游戏元素的生成函数  
def generate_block():  
    return random.choice(["A", "B", "C", "D", "E"])  
  
# 定义游戏元素的更新函数  

if check_collision(block, player_block[1:]):  
        return  
  
    player_block = player_block[1:]  
    player_position = player_position[:-1]  
    player_angle = player_angle - 90  
  
# 游戏主循环  
running = True  
clock = pygame.time.Clock()  
  
while running:  
  
    # 处理事件  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:  
                if player_block:  
                    move_block(player_block)  
                    if len(player_block) == 10:  
                        player_block.pop()  
                        continue  
                    player_speed = -player_speed  
  
    # 清空屏幕  
    screen.fill((0, 0, 0))  
  
    # 更新游戏元素的位置和状态  
    for block in blocks:  
        if block == player_block:  
            continue  
  
        move_block(block)  
  
        if block == player_block[0]:  
            player_position[0] += player_speed  
            if player_position[0] > screen[4]:  
                player_position[0] = screen[4]  
                player_speed = -player_speed  
            if player_position[0] < 0:  
                player_position[0] = 0  
               