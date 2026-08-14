import pygame
import random
import math
import sys

# --- Configuration ---
WIDTH, HEIGHT = 1024, 768
FPS = 120 

# Colors (Neon Palette)
CLR_BG = (10, 10, 18)
CLR_PLAYER = (0, 255, 255) # Cyan
CLR_ENEMY = (255, 50, 50)  # Red
CLR_BULLET = (255, 255, 100) # Yellow
CLR_PARTICLE = (255, 100, 50) # Orange

# --- New Global Sprite Groups ---
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

class Particle:
    """A custom particle system for explosion physics."""
    def __init__(self, x, y, color):
        self.pos = pygame.math.Vector2(x, y)
        dir_x, dir_y = random.uniform(-1, 1), random.uniform(-1, 1)
        self.vel = pygame.math.Vector2(dir_x, dir_y)
        if self.vel.length() > 0:
            self.vel = self.vel.normalize() * random.uniform(80, 400) # Increased speed
            
        self.lifetime = random.uniform(0.1, 0.4) # Faster decay
        self.age = 0
        self.color = color

    def update(self, dt):
        self.pos += self.vel * dt
        self.vel *= 0.95 # Add some drag/friction
        self.age += dt

    def draw(self, surface):
        if self.age < self.lifetime:
            # Shrink and fade
            alpha = int(255 * (1 - self.age / self.lifetime))
            radius = max(0, 4 * (1 - self.age / self.lifetime))
            
            # Draw circle with alpha support requires a workaround in older pygame
            p_surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            pygame.draw.circle(p_surf, (*self.color, alpha), (radius, radius), radius)
            surface.blit(p_surf, (int(self.pos.x - radius), int(self.pos.y - radius)))

class Projectile(pygame.sprite.Sprite):
    """A bullet that moves along a defined vector."""
    def __init__(self, x, y, direction_vector):
        super().__init__()
        # Visual: A small yellow line pointing in direction of travel
        self.image = pygame.Surface((10, 4), pygame.SRCALPHA)
        self.image.fill(CLR_BULLET)
        
        # Rotate image to match direction vector
        angle = math.degrees(math.atan2(-direction_vector.y, direction_vector.x))
        self.image = pygame.transform.rotate(self.image, angle)
        
        self.rect = self.image.get_rect(center=(x, y))
        
        # Physics setup
        self.pos = pygame.math.Vector2(x, y)
        self.vel = direction_vector * 800 # Velocity = direction * speed
        
    def update(self, dt):
        # Move along velocity vector
        self.pos += self.vel * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        
        # Kill sprite if it leaves the screen
        if not pygame.Rect(0, 0, WIDTH, HEIGHT).contains(self.rect):
            self.kill()

class Player(pygame.sprite.Sprite):
    """Player class utilizing Vector2 for smooth movement and mouse aiming."""
    def __init__(self):
        super().__init__()
        # Use simple triangle, but we will rotate it later
        self.original_image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.polygon(self.original_image, CLR_PLAYER, [(16, 0), (0, 32), (32, 32)])
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))
        
        # Movement physics
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 450
        
        # Shooting mechanics
        self.shoot_cooldown = 0.15 # Seconds between shots
        self.cooldown_timer = 0

    def update(self, dt, particles):
        # 1. Handle Movement Input
        keys = pygame.key.get_pressed()
        move_dir = pygame.math.Vector2(0, 0)
        
        if keys[pygame.K_w]: move_dir.y = -1
        if keys[pygame.K_s]: move_dir.y = 1
        if keys[pygame.K_a]: move_dir.x = -1
        if keys[pygame.K_d]: move_dir.x = 1

        if move_dir.length() > 0:
            move_dir = move_dir.normalize()
        
        self.pos += move_dir * self.speed * dt
        
        # Clamp to screen
        self.pos.x = max(16, min(WIDTH - 16, self.pos.x))
        self.pos.y = max(16, min(HEIGHT - 16, self.pos.y))
        
        # 2. Handle Rotation (Aiming)
        # Find vector from player to mouse
        mouse_pos = pygame.mouse.get_pos()
        aim_vec = pygame.math.Vector2(mouse_pos) - self.pos
        
        # Calculate angle (in degrees) for pygame rotation
        # Use -aim_vec.y because pygame Y axis is inverted
        target_angle = math.degrees(math.atan2(-aim_vec.y, aim_vec.x)) - 90
        
        # Apply rotation to the visual image
        self.image = pygame.transform.rotate(self.original_image, target_angle)
        self.rect = self.image.get_rect(center=(int(self.pos.x), int(self.pos.y)))

        # 3. Handle Shooting
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
            
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and self.cooldown_timer <= 0: # Left Click
            self.shoot(aim_vec, particles)
            
    def shoot(self, aim_direction, particles):
        # Normalize the aim vector so it only provides direction, not magnitude
        if aim_direction.length() > 0:
            bullet_dir = aim_direction.normalize()
            # Instantiate projectile
            bullet = Projectile(self.pos.x, self.pos.y, bullet_dir)
            all_sprites.add(bullet)
            projectiles.add(bullet)
            
            # Tiny firing effect (kickback particles)
            for _ in range(3):
                particles.append(Particle(self.pos.x, self.pos.y, CLR_BULLET))
                
            self.cooldown_timer = self.shoot_cooldown

class Enemy(pygame.sprite.Sprite):
    """Enemy class featuring rudimentary homing AI."""
    def __init__(self, target_player):
        super().__init__()
        self.image = pygame.Surface((22, 22), pygame.SRCALPHA)
        pygame.draw.rect(self.image, CLR_ENEMY, (0,0,22,22), 2) # Hollow red square
        self.rect = self.image.get_rect()
        
        spawn_radius = max(WIDTH, HEIGHT)
        angle = random.uniform(0, 2 * math.pi)
        self.pos = pygame.math.Vector2(WIDTH/2 + math.cos(angle)*spawn_radius, 
                                       HEIGHT/2 + math.sin(angle)*spawn_radius)
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        self.speed = random.uniform(100, 200)
        self.player = target_player

    def update(self, dt):
        direction = self.player.pos - self.pos
        if direction.length() > 0:
            direction = direction.normalize()
            
        self.pos += direction * self.speed * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

# --- Main Game Loop ---
def main():
    pygame.init()
    # Enable anti-aliasing for smoother visuals if supported
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Neon Swarm: Aim & Shoot")
    clock = pygame.time.Clock()
    
    # Pre-render a background surface for performance
    bg_surf = pygame.Surface((WIDTH, HEIGHT))
    bg_surf.fill(CLR_BG)
    # Add minor scanlines effect
    for y in range(0, HEIGHT, 4):
        pygame.draw.line(bg_surf, (5, 5, 10), (0, y), (WIDTH, y))

    player = Player()
    all_sprites.add(player)
    
    particles = []
    enemy_spawn_timer = 0
    enemy_spawn_rate = 0.5 # Seconds between spawns

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0 

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Spawning logic (gets progressively harder)
        enemy_spawn_timer += dt
        if enemy_spawn_timer > enemy_spawn_rate:
            enemy = Enemy(player)
            all_sprites.add(enemy)
            enemies.add(enemy)
            enemy_spawn_timer = 0
            # Slowly increase difficulty
            enemy_spawn_rate = max(0.1, enemy_spawn_rate - 0.001)

        # UPDATES
        player.update(dt, particles) # Player update needs particles list now
        enemies.update(dt)
        projectiles.update(dt)
        
        # Update custom particle list
        for p in particles[:]:
            p.update(dt)
            if p.age >= p.lifetime:
                particles.remove(p)

        # COLLISIONS
        
        # 1. Projectiles vs Enemies
        # spritecollide(sprite, group, dokill) -> list of hits
        # We use groupcollide for efficiency with many bullets vs many enemies
        bullet_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
        for enemy_hit in bullet_hits:
            # Create large explosion for enemy death
            for _ in range(20):
                particles.append(Particle(enemy_hit.rect.centerx, enemy_hit.rect.centery, CLR_ENEMY))

        # 2. Enemies vs Player
        player_hits = pygame.sprite.spritecollide(player, enemies, True)
        for enemy_hit in player_hits:
            # Player damaged effect
            for _ in range(40):
                particles.append(Particle(player.pos.x, player.pos.y, CLR_PLAYER))
            # Game over logic would go here

        # RENDERING
        screen.blit(bg_surf, (0,0)) # Draw pre-rendered background
        
        all_sprites.draw(screen) # Draws all groups added to it
        
        # Particles are managed separately as they aren't Sprites
        for p in particles:
            p.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()