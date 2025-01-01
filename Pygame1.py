import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Create the Game Screen

width, height = 800, 600
screen = pygame.display.set_mode((width, height)) # Creates Screen

# Background Image

background = pygame.image.load("background_image.png")

# Background Music

mixer.music.load("background.wav")
mixer.music.play(-1)

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

enemy_icon = []
enemy_x_axis = []
enemy_y_axis = []
enemy_x_axis_speed = []
enemy_y_axis_speed = []
num_of_enemies = 6

existing_axis_enemies = []

# Check if the new position of enemy doesn't overlap

def enemy_overlap(new_x_axis, new_y_axis, existing_axis):
    for old_x_axis, old_y_axis in existing_axis:
        distance = math.sqrt((math.pow(old_x_axis - new_x_axis, 2)) + (math.pow(old_y_axis - new_y_axis,2)))
        if distance < 50:
            return False
    return True
    

for i in range(num_of_enemies):
    enemy_icon.append(pygame.image.load("enemy.png"))
    while True:
        new_x_axis = random.randint(0, 736)
        new_y_axis = random.randint(25, 250)
        
        if enemy_overlap(new_x_axis, new_y_axis, existing_axis_enemies): # if not overlapping then give the x-axis and y-axis to enemy or else since it's while true it will again give new value and check the overlapping
            enemy_x_axis.append(new_x_axis)
            enemy_y_axis.append(new_y_axis)
            existing_axis_enemies.append((new_x_axis, new_y_axis))
            break
        
    enemy_x_axis_speed.append(1.5)
    enemy_y_axis_speed.append(30)

# Creating Bullets and showing on screen

bullet_icon = pygame.image.load("bullet.png")
bullet_x_axis = 0
bullet_y_axis = 480
bullet_y_axis_speed = 3
bullet_state = "ready" # If the bullet is in ready mode it means it isn't moving yet
# If the bullet is in fire mode it means it is moving

score_state = "not-moving"

# Creating Scores

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

text_x_axis = 10
text_y_axis = 10

# End Game Text

game_over_font = pygame.font.Font("freesansbold.ttf", 64)

# End Game Funtion

def end_game():
    end_game_text = game_over_font.render("GAME ENDED", True, (255, 255, 255))
    screen.blit(end_game_text, (200, 250))

# Score Function

def score_Val(x_axis, y_axis):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x_axis, y_axis))

# Player Funtions

def player(x_axis, y_axis):
    screen.blit(player_icon, (x_axis, y_axis)) # blit means to draw
    
# Enemy Funtions

def enemy(x_axis, y_axis, i):
    screen.blit(enemy_icon[i], (x_axis, y_axis))

# Enemy Funtions

def bullet(x_axis, y_axis):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, (x_axis + 16, y_axis + 10))

# Collision between the bullet and enemy 

def collisionChecker(enemy_x_axis, enemy_y_axis, bullet_x_axis, bullet_y_axis):
    distance = math.sqrt((math.pow(enemy_x_axis - bullet_x_axis, 2)) + (math.pow(enemy_y_axis - bullet_y_axis,2)))
    if distance < 27:
        return True

is_text_moving = False

# Run the Screen and the events performed on the screen
running = True # When I quit the window I want this to be false so that while loop stops running

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
                    
                    mixer.Sound("laser.wav").play() # sound of firing
                    
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
    
    # Creating Boundaries
    for i in range(num_of_enemies):
        
        # End Game
        if enemy_y_axis[i] > 440:
            for j in range(num_of_enemies):
                enemy_y_axis[j] = 2000
            end_game()
            break
        
        enemy_x_axis[i] += enemy_x_axis_speed[i] # Update player position
        
        if enemy_x_axis[i] <= 0:
            enemy_x_axis_speed[i] = 1.5
            enemy_y_axis[i] += enemy_y_axis_speed[i]
        elif enemy_x_axis[i] >= 736: # using number 736 because of the player image pixel which is 64 (800 - 64)
            enemy_x_axis_speed[i] = -1.5
            enemy_y_axis[i] += enemy_y_axis_speed[i]
            
        # Collision Checking
    
        collision = collisionChecker(enemy_x_axis[i], enemy_y_axis[i], bullet_x_axis, bullet_y_axis)
        
        if collision:
            
            mixer.Sound("explosion.wav").play()
            
            bullet_y_axis = 480
            bullet_state = "ready"
            
            score += 1
            is_text_moving = True
            
            enemy_x_axis[i] = random.randint(0, 736)
            enemy_y_axis[i] = random.randint(25, 250)
            
        enemy(enemy_x_axis[i], enemy_y_axis[i], i) # Draw the enemy
        
    # Moving Bullet
    
    if bullet_y_axis == 0:
        bullet_y_axis = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":
        bullet(bullet_x_axis, bullet_y_axis)
        bullet_y_axis -= bullet_y_axis_speed
      
    # Moving Text
        
    if is_text_moving:
        text_x_axis += 2
    
    if text_x_axis > 800:
        text_x_axis = 10
        is_text_moving = False
    
    player(player_x_axis, player_y_axis) # Draw the player
    score_Val(text_x_axis, text_y_axis) # Render the score
    pygame.display.update() # Update the display
    
pygame.quit()
