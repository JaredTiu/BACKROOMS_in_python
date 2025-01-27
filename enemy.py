import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2  # Speed of the enemy

    def update(self, player_x, player_y):
        # Move towards the player
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed

    def draw(self, screen, enemy_texture, ground_level):  # Accept ground_level as a parameter
        screen.blit(enemy_texture, (self.x, ground_level))  # Draw the enemy at ground level