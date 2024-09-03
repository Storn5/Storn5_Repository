import pygame
import math

width = 800
height = 900
screen_color = (0, 0, 0)
line_color = (220, 220, 0)
player_color = (220, 220, 220)
border_color = (100, 100, 100)

wall_left = pygame.math.Vector3(400, 120, 0)
wall_right = pygame.math.Vector3(420, 180, 0)
wall_left_trans = pygame.math.Vector3()
wall_right_trans = pygame.math.Vector3()
wall_left_3d = pygame.math.Vector2()
wall_right_3d = pygame.math.Vector2()
wall_left_3d_top = pygame.math.Vector2()
wall_right_3d_top = pygame.math.Vector2()

player = pygame.math.Vector3(300, 150, 0)
player_angle = 0
player_speed = 0.25
player_turn_speed = 0.0025
running = True

aspect_ratio = 300 / width
fov = 60
fov_scaling_factor = 1 / math.tan(math.radians(60)/2)

def move_player(keys):
    global player, player_angle, running
    # Movement
    if keys[pygame.K_w]:
        player.x += player_speed * math.cos(player_angle)
        player.y += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player.x -= player_speed * math.cos(player_angle)
        player.y -= player_speed * math.sin(player_angle)
    # Rotation
    if keys[pygame.K_a]:
        player_angle -= player_turn_speed
    if keys[pygame.K_d]:
        player_angle += player_turn_speed
    # Quitting
    if keys[pygame.K_ESCAPE]:
        running = False
    # Stop player from crosmath.sing borders
    player.x = max(0, player.x)
    player.x = min(800, player.x)
    player.y = max(0, player.y)
    player.y = min(300, player.y)

def main():
    global wall_left, wall_right, player, player_angle, running
    screen=pygame.display.set_mode((width, height))
    screen1 = screen.subsurface(pygame.Rect((0, 0), (800, 300)))
    screen2 = screen.subsurface(pygame.Rect((0, 300), (800, 300)))
    screen3 = screen.subsurface(pygame.Rect((0, 600), (800, 300)))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys=pygame.key.get_pressed()
        move_player(keys)
        screen.fill(screen_color)
        
        # Draw borders
        pygame.draw.line(screen, border_color, (0, 300), (800, 300))
        pygame.draw.line(screen, border_color, (0, 600), (800, 600))
        
        #                   2D
        # Draw wall
        pygame.draw.line(screen1, line_color, (wall_left.x, wall_left.y), (wall_right.x, wall_right.y))
        # Draw player
        pygame.draw.circle(screen1, player_color, (player.x, player.y), 5)
        pygame.draw.line(screen1, player_color,
            (player.x, player.y),
            (player.x + 20 * math.cos(player_angle), player.y + 20 * math.sin(player_angle)))
        
        #                   2D (POV)
        # Transform wall relative to player
        wall_left_trans = pygame.math.Vector3(wall_left.x - player.x, wall_left.y - player.y, 0)
        wall_right_trans = pygame.math.Vector3(wall_right.x - player.x, wall_right.y - player.y, 0)
        wall_left_trans = pygame.math.Vector3(
            wall_left_trans.x * math.sin(player_angle) - wall_left_trans.y * math.cos(player_angle),
            wall_left_trans.y,
            wall_left_trans.x * math.cos(player_angle) + wall_left_trans.y * math.sin(player_angle)
        )
        wall_right_trans = pygame.math.Vector3(
            wall_right_trans.x * math.sin(player_angle) - wall_right_trans.y * math.cos(player_angle),
            wall_right_trans.y,
            wall_right_trans.x * math.cos(player_angle) + wall_right_trans.y * math.sin(player_angle)
        )
        # Draw wall
        pygame.draw.line(screen2, line_color, 
            (400 - wall_left_trans.x, 150 - wall_left_trans.z),
            (400 - wall_right_trans.x, 150 - wall_right_trans.z))
        # Draw player
        pygame.draw.circle(screen2, player_color, (400, 150), 5)
        pygame.draw.line(screen2, player_color, (400, 130), (400, 150))
        
        #                   3D (POV)
        # Project wall in 3D
        wall_left_3d = pygame.math.Vector2(
            -50 * wall_left_trans.x / wall_left_trans.z,
            -500 / wall_left_trans.z
        )
        wall_right_3d = pygame.math.Vector2(
            -50 * wall_right_trans.x / wall_right_trans.z,
            -500 / wall_right_trans.z
        )
        wall_left_3d_top = pygame.math.Vector2(
            -50 * wall_left_trans.x / wall_left_trans.z,
            500 / wall_left_trans.z
        )
        wall_right_3d_top = pygame.math.Vector2(
            -50 * wall_right_trans.x / wall_right_trans.z,
            500 / wall_right_trans.z
        )
        # Draw wall bottom
        pygame.draw.line(screen3, line_color, 
            (400 + wall_left_3d.x, 150 + wall_left_3d.y),
            (400 + wall_right_3d.x, 150 + wall_right_3d.y)
        )
        # Draw wall top
        pygame.draw.line(screen3, line_color, 
            (400 + wall_left_3d_top.x, 150 + wall_left_3d_top.y),
            (400 + wall_right_3d_top.x, 150 + wall_right_3d_top.y)
        )
        # Draw wall left
        pygame.draw.line(screen3, line_color, 
            (400 + wall_left_3d_top.x, 150 + wall_left_3d_top.y),
            (400 + wall_left_3d.x, 150 + wall_left_3d.y)
        )
        # Draw wall right
        pygame.draw.line(screen3, line_color, 
            (400 + wall_right_3d_top.x, 150 + wall_right_3d_top.y),
            (400 + wall_right_3d.x, 150 + wall_right_3d.y)
        )
        
        pygame.display.flip()

if __name__ == '__main__':
    main()
