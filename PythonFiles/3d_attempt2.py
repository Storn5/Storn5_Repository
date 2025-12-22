import sys, pygame
from pygame.math import Vector2, Vector3
from pygame.locals import QUIT
import numpy as np

SCREEN = Vector2(1280, 720)
FPS = 60

FOV = 90
ASPECT = SCREEN.y / SCREEN.x
NEAR = 0.3
FAR = 1000

CAMERA_SPEED = 0.01

BACKGROUND_COLOR = Vector3(10, 10, 10)
LINE_COLOR = Vector3(255, 0, 0)
RAY_COLOR = Vector3(0, 255, 0)
LINE_THICCNESS = 3
FONTSIZE = 30
TUTORIAL_TXT = ('Move camera with WASD, turn with Q/E, change FOV with Z/X',
                'Move cube with IKJL, turn it with U/O')

camera_pos = Vector3(0, 0, 4)
camera_yaw = 0
focal_length = 1/np.tan(np.radians(FOV)/2)

cube_pos = Vector3(0, 0, 0)
cube_yaw = 0

vertices = (
    np.array([-1., -1.,  1.,  1.]), # Bottom-left
    np.array([ 1., -1.,  1.,  1.]), # Bottom-right
    np.array([-1.,  1.,  1.,  1.]), # Top-left
    np.array([ 1.,  1.,  1.,  1.]), # Top-right
    np.array([-1., -1., -1.,  1.]), # Bottom-left
    np.array([ 1., -1., -1.,  1.]), # Bottom-right
    np.array([-1.,  1., -1.,  1.]), # Top-left
    np.array([ 1.,  1., -1.,  1.]), # Top-right
)

# RH coordinates, +Y is up, -Z is away from the camera
#                             
#        6           7        
#                             
#    2           3            
#                             
#        4           5        
#                             
#    0           1            
#                             

triangles = (
    (0, 1, 2), # Front bottom-left
    (1, 3, 2), # Front top-right
    (1, 5, 3), # Right bottom-left
    (5, 7, 3), # Right top-right
    (2, 3, 6), # Top bottom-left
    (3, 7, 6), # Top top-right
    (4, 0, 6), # Left bottom-left
    (0, 2, 6), # Left top-right
    (5, 4, 7), # Back bottom-left
    (4, 6, 7), # Back top-right
    (4, 5, 0), # Bottom bottom-left
    (5, 1, 0), # Bottom top-right
)

# Triangle faces are CCW when looking at them face-on
#                             
#        .-----------.        
#      /  4  \  5  / |        
#    .-----------.  3|        
#    |  \     1  | \ |        
#    |     \     |2  .        
#    |  0     \  | /          
#    .-----------.            
#                             

def handle_input(events):
    global camera_yaw, cube_yaw, focal_length

    for event in events:
        if event.type == QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_pos.z -= CAMERA_SPEED * np.cos(camera_yaw)
        camera_pos.x -= CAMERA_SPEED * np.sin(camera_yaw)
    elif keys[pygame.K_s]:
        camera_pos.z += CAMERA_SPEED * np.cos(camera_yaw)
        camera_pos.x += CAMERA_SPEED * np.sin(camera_yaw)
    if keys[pygame.K_a]:
        camera_pos.x -= CAMERA_SPEED * np.cos(camera_yaw)
        camera_pos.z += CAMERA_SPEED * np.sin(camera_yaw)
    elif keys[pygame.K_d]:
        camera_pos.x += CAMERA_SPEED * np.cos(camera_yaw)
        camera_pos.z -= CAMERA_SPEED * np.sin(camera_yaw)
    if keys[pygame.K_q]:
        camera_yaw += CAMERA_SPEED
    elif keys[pygame.K_e]:
        camera_yaw -= CAMERA_SPEED
    if keys[pygame.K_z]:
        focal_length += CAMERA_SPEED
    elif keys[pygame.K_x]:
        focal_length -= CAMERA_SPEED
        if focal_length < 0.00000000001:
            focal_length = 0.00000000001

    if keys[pygame.K_i]:
        cube_pos.z -= CAMERA_SPEED * np.cos(cube_yaw)
        cube_pos.x -= CAMERA_SPEED * np.sin(cube_yaw)
    elif keys[pygame.K_k]:
        cube_pos.z += CAMERA_SPEED * np.cos(cube_yaw)
        cube_pos.x += CAMERA_SPEED * np.sin(cube_yaw)
    if keys[pygame.K_j]:
        cube_pos.x -= CAMERA_SPEED * np.cos(cube_yaw)
        cube_pos.z += CAMERA_SPEED * np.sin(cube_yaw)
    elif keys[pygame.K_l]:
        cube_pos.x += CAMERA_SPEED * np.cos(cube_yaw)
        cube_pos.z -= CAMERA_SPEED * np.sin(cube_yaw)
    if keys[pygame.K_u]:
        cube_yaw += CAMERA_SPEED
    elif keys[pygame.K_o]:
        cube_yaw -= CAMERA_SPEED

# Returns intersect between a ray and a triangle
def intersect(ray_origin, ray_dir, v1, v2, v3):
    tri_norm = np.cross(v2 - v1, v3 - v1)

    det = -(ray_dir @ tri_norm)
    if abs(det) < 0.0001:
        return None
    
    invDet = 1. / det

    a0 = ray_origin - v1
    u = invDet * ((v3 - v1) @ np.cross(a0, ray_dir))
    v = invDet * (ray_dir @ np.cross(a0, v2 - v1))
    t = invDet * ((v2 - v1) @ np.cross(a0, v3 - v1))

    if t >= 0 and u >= 0 and v >= 0 and u + v <= 1:
        return ray_origin + (t * ray_dir)

    return None

def render_faces(screen):
    # Matrices are row-major, so they're written as they would be on paper
    model_matrix = np.array([
        [ np.cos(cube_yaw), 0., np.sin(cube_yaw), cube_pos.x],
        [ 0.              , 1., 0.              , cube_pos.y],
        [-np.sin(cube_yaw), 0., np.cos(cube_yaw), cube_pos.z],
        [ 0.              , 0., 0.              , 1.        ],
    ])

    camera_matrix = np.array([
        [ np.cos(camera_yaw), 0., np.sin(camera_yaw), camera_pos.x],
        [ 0.                , 1., 0.                , camera_pos.y],
        [-np.sin(camera_yaw), 0., np.cos(camera_yaw), camera_pos.z],
        [ 0.                , 0., 0.                , 1.          ],
    ])

    view_matrix = np.linalg.inv(camera_matrix)
    
    proj_matrix = np.array([
        [focal_length, 0.                 , 0.                      , 0.                      ],
        [0.          , focal_length/ASPECT, 0.                      , 0.                      ],
        [0.          , 0.                 , -((FAR+NEAR)/(FAR-NEAR)), -(2*FAR*NEAR/(FAR-NEAR))],
        [0.          , 0.                 , -1.                     , 0.                      ],
    ])

    mvp_matrix = proj_matrix @ view_matrix @ model_matrix

    for triangle in triangles:
        transformed_vertices = (mvp_matrix @ np.array([
            vertices[triangle[0]],
            vertices[triangle[1]],
            vertices[triangle[2]],
        ]).T).T
        transformed_vertices /= transformed_vertices[:, 3, np.newaxis]
        transformed_vertices = transformed_vertices[:, :3]

        view_intersect = intersect(np.array([0, 0, 0]), np.array([0, 0, -1]), transformed_vertices[0], transformed_vertices[1], transformed_vertices[2])
        if view_intersect is not None:
            view_intersect = (view_intersect + 1)[:2] * np.array([SCREEN.x / 2, SCREEN.y / 2])
            pygame.draw.circle(screen, RAY_COLOR, view_intersect, LINE_THICCNESS, LINE_THICCNESS)

        for vertex1 in transformed_vertices:
            for vertex2 in transformed_vertices:
                if not np.array_equal(vertex1, vertex2):
                    if abs(vertex1[2]) < 1 and abs(vertex2[2]) < 1:
                        v1 = (vertex1 + 1)[:2] * np.array([SCREEN.x / 2, SCREEN.y / 2])
                        v2 = (vertex2 + 1)[:2] * np.array([SCREEN.x / 2, SCREEN.y / 2])
                        pygame.draw.line(screen, LINE_COLOR, v1, v2, LINE_THICCNESS)

def render(screen, screen_font):
    screen.fill(BACKGROUND_COLOR)
    render_faces(screen)

    fov = np.degrees(2*np.atan(1/focal_length))
    text_surfaces = [screen_font.render(i, True, (250, 250, 250)) for i in TUTORIAL_TXT]
    text_surfaces.append(screen_font.render(f'FOV: {fov}', True, (250, 250, 250)))
    for (i, text_surf) in enumerate(text_surfaces):
        screen.blit(text_surf, (10, 10 + i*(FONTSIZE + 10)))
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode(SCREEN)
    clock = pygame.time.Clock()
    pygame.font.init()
    screen_font = pygame.font.SysFont('Century Gothic', FONTSIZE)

    while True:
        dt = clock.tick(FPS)
        handle_input(pygame.event.get())
        render(screen, screen_font)


if __name__ == '__main__':
    main()
