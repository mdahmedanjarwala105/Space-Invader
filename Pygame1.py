import pygame
import random

# Initialize Pygame
pygame.init()

# Create the Game Screen

width, height = 800, 600
screen = pygame.display.set_mode((width, height)) # Creates Screen

# Background Image
background = pygame.image.load("background_image.png")

# Create Title and Icon

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("SpaceInvader.png") # Loads image
pygame.display.set_icon(icon)

# Creating Player and showing on screen

player_icon = pygame.image.load("player.png")
player_x_axis = 370
player_y_axis = 480
player_x_axis_speed = 0

# Creating Enemy and showing on screen

enemy_icon = pygame.image.load("enemy.png")
enemy_x_axis = random.randint(0, 736)
enemy_y_axis = random.randint(50, 300)
enemy_x_axis_speed = 1.5
enemy_y_axis_speed = 30

# Creating Bullets and showing on screen

bullet_icon = pygame.image.load("bullet.png")
bullet_y_axis = 480
bullet_y_axis_speed = 3
bullet_state = "ready" # If the bullet is in ready mode it means it isn't moving yet
# If the bullet is in fire mode it means it is moving

# Player Funtions

def player(x_axis, y_axis):
    screen.blit(player_icon, (x_axis, y_axis)) # blit means to draw
    
# Enemy Funtions

def enemy(x_axis, y_axis):
    screen.blit(enemy_icon, (x_axis, y_axis))

# Enemy Funtions

def bullet(x_axis, y_axis):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, (x_axis + 16, y_axis + 10))

# Run the Screen and the events performed on the screen
running = True

while running:
    
    # Fill the screen with a color to prevent ghosting
    screen.fill((0, 255, 0))  # Black background
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # closes the screen
            running = False
    
        if event.type == pygame.KEYDOWN: # Keydown means key pressed if we use .KEYUP that means key released
            if event.key == pygame.K_LEFT:
                player_x_axis_speed = -2 # Assign a value to move left
            if event.key == pygame.K_RIGHT:
                player_x_axis_speed = 2 # Assign a value to move right
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x_axis = player_x_axis # assigning the old value of player x-axis so that it doesn't take and move constantly with player
                    bullet(bullet_x_axis, bullet_y_axis)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_axis_speed = 0
        
    
    player_x_axis += player_x_axis_speed # Update player position
    
    # Creating Boundaries
    
    if player_x_axis <= 0:
        player_x_axis = 0
    elif player_x_axis >= 736: # using number 736 because of the player image pixel which is 64 (800 - 64)
        player_x_axis = 736
    
    enemy_x_axis += enemy_x_axis_speed # Update player position
    
    # Creating Boundaries
    
    if enemy_x_axis <= 0:
        enemy_x_axis_speed = 1.5
        enemy_y_axis += enemy_y_axis_speed
    elif enemy_x_axis >= 736: # using number 736 because of the player image pixel which is 64 (800 - 64)
        enemy_x_axis_speed = -1.5
        enemy_y_axis += enemy_y_axis_speed
        
    # Moving Bullet
    
    if bullet_y_axis == 0:
        bullet_y_axis = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":
        bullet(bullet_x_axis, bullet_y_axis)
        bullet_y_axis -= bullet_y_axis_speed
    
    player(player_x_axis, player_y_axis) # Draw the player
    enemy(enemy_x_axis, enemy_y_axis) # Draw the enemy
    pygame.display.update() # Update the display