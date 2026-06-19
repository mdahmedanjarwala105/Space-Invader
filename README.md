# Space Invader

A classic Space Invaders arcade game built with Python and Pygame featuring player movement, enemy waves, shooting mechanics, and sound effects.

## Features

- Player spaceship movement with arrow keys
- Shooting mechanics with laser projectiles
- Enemy waves with increasing difficulty
- Real-time score tracking
- Background music and sound effects
- Explosion animations

## Controls

- **Left/Right Arrow Keys**: Move the spaceship
- **Spacebar**: Shoot lasers
- The game runs automatically with enemy waves

## Installation

### Using Pipenv

```bash
pip install pipenv
pipenv install
pipenv run python Pygame1.py
```

### Using pip

```bash
pip install -r requirements.txt
python Pygame1.py
```

## File Structure

```
Space-Invader/
├── Pygame1.py               # Main game script
├── Pipfile                  # Pipenv dependencies
├── Pipfile.lock             # Pipenv lock file
├── Player.png               # Player spaceship sprite
├── SpaceInvader.png         # Enemy sprite
├── enemy.png                # Enemy sprite
├── bullet.png               # Bullet sprite
├── background_image.png     # Game background
├── background.wav           # Background music
├── laser.wav                # Laser sound effect
├── explosion.wav            # Explosion sound effect
├── Image 1.png              # Screenshot
├── Image 2.png              # Screenshot
├── Image3.png               # Screenshot
└── README.md                # Project documentation
```

## Tech Stack

- **Python** - Core game logic
- **Pygame** - Graphics, sound, and input handling

## License

MIT License - see the [LICENSE](LICENSE) file for details.
