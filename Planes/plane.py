#Plane parent class, player and enemy planes inherit from this class
#Allows consistency for both

import math
import arcade

class Plane(arcade.Sprite):
    def __init__(self, image, x, y, health=1, speed=200, bullet_direction=1):
        super().__init__(image, scale=0.5, center_x=x, center_y=y)
        self.health = health
        self.speed = speed
        self.is_hit = False
        self.bullet_direction = bullet_direction
        self.fire_delay = 0.25
        self.shot_timer = 0.0
        self. hit_timer = 0.0
        self.move_x = 0.0
        self.move_y = 0.0

    def update (self, delta_time):
        self.center_x += self.move_x * self.speed * delta_time
        self.center_y += self.move_y * self.speed * delta_time

    def set_direction(self, dx, dy):
        # normalize diagonal input so diagonal travel isn't faster
        length = max(1.0, math.hypot(dx,dy))
        self.move_x = dx / length
        self.move_y = dy / length

    def move_up(self):
        self.set_direction(0, 1)
    def move_down(self):
        self.set_direction(0, -1)
    def move_left(self):
        self.set_direction(-1, 0)
    def move_right(self):
        self.set_direction(1, 0)

    def take_damage(self, amount=1):
        #Subtract the amount of damage from the health of the plane
        self.health = max(0, self.health - amount)
        if self.is_destroyed():
            self.remove_from_sprite_lists()
    def is_destroyed (self):
        return self.health == 0
