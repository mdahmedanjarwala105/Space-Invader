import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Create the Game Screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height)) # Creates Screen

# Set FPS and clock for controlling game speed
FPS = 160
clock = pygame.time.Clock()

# Background Image
background = pygame.image.load("background_image.png")

# Background Music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Create Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("SpaceInvader.png") # Loads image
pygame.display.set_icon(icon)

# colors
WHITE = (255, 255, 255)

# Fonts
LETTER_FONT = pygame.font.Font("freesansbold.ttf", 32)
TITLE_FONT = pygame.font.Font("freesansbold.ttf", 62)

# Checking if the Score is moving after the score is incremented or not
score_state = "not-moving"

# Button Variable
BUTTON_RADIUS = 50
BUTTON_X_Axis = width // 2
BUTTON_Y_Axis = 320

# Creating Scores
high_score = 0

# End Game Text
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

# Function to check if a new enemy position overlaps with existing enemies
def enemy_overlap(new_x_axis, new_y_axis, existing_axis):
    for old_x_axis, old_y_axis in existing_axis:
        distance = math.sqrt((math.pow(old_x_axis - new_x_axis, 2)) + (math.pow(old_y_axis - new_y_axis,2)))
        if distance < 50:
            return False
    return True


# Function to display "Game Ended" text and update high score
def end_game():
    global high_score
    if score > high_score:
        high_score = score
    
    end_game_text = game_over_font.render("GAME ENDED", True, WHITE)
    screen.blit(end_game_text, (200, 250))
    pygame.display.update()
    pygame.time.wait(2000)  # Pause for 2 seconds


# Function to display the current score on the screen
def score_Val(x_axis, y_axis):
    score_value = LETTER_FONT.render("Score: " + str(score), True, WHITE)
    screen.blit(score_value, (x_axis, y_axis))
    

# Function to display the high score on the screen
def high_score_val():
    score_value = LETTER_FONT.render("High Score: " + str(high_score), True, WHITE)
    screen.blit(score_value, (300, 125))


# Function to draw the player on the screen
def player(x_axis, y_axis):
    screen.blit(player_icon, (x_axis, y_axis)) # blit means to draw
    

# Function to draw an enemy on the screen
def enemy(x_axis, y_axis, i):
    screen.blit(enemy_icon[i], (x_axis, y_axis))


# Function to draw a bullet on the screen
def bullet(x_axis, y_axis):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_icon, (x_axis + 16, y_axis + 10))


# Function to check if a bullet collides with an enemy
def collisionChecker(enemy_x_axis, enemy_y_axis, bullet_x_axis, bullet_y_axis):
    distance = math.sqrt((math.pow(enemy_x_axis - bullet_x_axis, 2)) + (math.pow(enemy_y_axis - bullet_y_axis,2)))
    if distance < 27:
        return True


# Function to draw the menu with the "Play" button
def drawBig():
    text = TITLE_FONT.render("SpaceInvader Game", 1, WHITE)
    screen.blit(text, (width/2 - text.get_width()/2, 20))
    pygame.draw.circle(screen, WHITE, (BUTTON_X_Axis, BUTTON_Y_Axis), BUTTON_RADIUS, 3)
    text = LETTER_FONT.render("PLAY", 1, WHITE)
    screen.blit(text, (BUTTON_X_Axis - text.get_width()/2, BUTTON_Y_Axis - text.get_height()/2))


# Function to initialize or reset game variables
def set_game_value():
    global text_x_axis, text_y_axis, score, player_icon, player_x_axis, player_y_axis, player_x_axis_speed, bullet_icon, bullet_y_axis_speed, bullet_x_axis, bullet_y_axis, bullet_state, is_text_moving, enemy_x_axis, enemy_y_axis, existing_axis_enemies, enemy_icon, enemy_x_axis_speed, enemy_y_axis_speed, num_of_enemies

    score = 0
    text_x_axis = 10
    text_y_axis = 10
    
    # Initialize player variables
    player_icon = pygame.image.load("player.png")
    player_x_axis = 370
    player_y_axis = 480
    player_x_axis_speed = 0

    # Initialize bullet variables
    bullet_icon = pygame.image.load("bullet.png")
    bullet_x_axis = 0
    bullet_y_axis = 480
    bullet_y_axis_speed = 3
    bullet_state = "ready" # If the bullet is in ready mode it means it isn't moving yet
    # If the bullet is in fire mode it means it is moving
    
    is_text_moving = False

    # Creating Enemy and showing on screen

    enemy_icon = []
    enemy_x_axis = []
    enemy_y_axis = []
    enemy_x_axis_speed = []
    enemy_y_axis_speed = []
    num_of_enemies = 6

    existing_axis_enemies = []

    # Set initial positions and speeds for enemies
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


# Main game loop
def main():
    set_game_value()
    
    global text_x_axis, player_x_axis, player_x_axis_speed, bullet_x_axis, bullet_y_axis, bullet_state, score, is_text_moving
    
    # Run the Screen and the events performed on the screen
    running = True # When I quit the window I want this to be false so that while loop stops running

    while running:
        
        clock.tick(FPS) # Control game speed
        
        # Fill the screen with a color to prevent ghosting
        screen.fill((WHITE))  # WHITE background
        screen.blit(background, (0, 0)) # Draw the background
        
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
                return
            
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
                
                # Find a new position for the enemy without overlapping
                while True:
                    new_x_axis = random.randint(0, 736)
                    new_y_axis = random.randint(25, 250)

                    if enemy_overlap(new_x_axis, new_y_axis, existing_axis_enemies):
                        enemy_x_axis[i] = new_x_axis
                        enemy_y_axis[i] = new_y_axis
                        existing_axis_enemies[i] = (new_x_axis, new_y_axis)
                        break
                
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
        

# Menu function to display the start screen
def menu():
    FPS = 60
    clock = pygame.time.Clock()
    # Run the Screen and the events performed on the screen
    running = True # When I quit the window I want this to be false so that while loop stops running

    while running:
        
        clock.tick(FPS)
        # Fill the screen with a color to prevent ghosting
        
        screen.fill(WHITE)  # Fill the screen with a color to prevent ghosting
        screen.blit(background, (0, 0))  # Draw the background
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closes the screen
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
                distance = math.sqrt((math.pow(BUTTON_X_Axis - mouse_x_axis,2)) + (math.pow(BUTTON_Y_Axis - mouse_y_axis, 2)))
                if distance < BUTTON_RADIUS:
                    main()
                    
        drawBig()
        high_score_val()
        pygame.display.update()
        
        
menu()  # Call the menu function to start the game
