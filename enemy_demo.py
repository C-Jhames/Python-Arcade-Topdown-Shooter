"""CS 122 Arcade demo: spawn, move, and fire enemy planes."""

import random

import arcade

WIDTH = 640
HEIGHT = 720
SPAWN_INTERVAL = 1.4
ASSETS = ":resources:images/space_shooter/"


class EnemyPlane(arcade.Sprite):
    """The movement and firing behavior of one enemy plane."""

    def __init__(self, x, y):
        super().__init__(ASSETS + "playerShip1_orange.png", scale=0.55)
        self.position = x, y
        self.angle = 180
        self.speed = 115  # Pixels per second
        self.shot_cooldown = 0.75

    def update(self, delta_time):
        self.center_y -= self.speed * delta_time
        self.shot_cooldown -= delta_time

    def shoot(self):
        bullet = arcade.SpriteSolidColor(5, 16, color=(255, 204, 88))
        bullet.center_x = self.center_x
        bullet.top = self.bottom
        self.shot_cooldown = 1.15
        return bullet


class EnemyDemo(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "CS 122 | Enemy Plane Demo")
        self.background_color = (14, 24, 41)
        self.enemies = arcade.SpriteList()
        self.enemy_bullets = arcade.SpriteList()
        self.time_until_spawn = SPAWN_INTERVAL
        self.spawn_enemy()

    def spawn_enemy(self):
        x = random.randint(40, WIDTH - 40)
        self.enemies.append(EnemyPlane(x, HEIGHT + 35))

    def on_draw(self):
        self.clear()
        self.enemies.draw()
        self.enemy_bullets.draw()

    def on_update(self, delta_time):
        self.time_until_spawn -= delta_time
        if self.time_until_spawn <= 0:
            self.spawn_enemy()
            self.time_until_spawn += SPAWN_INTERVAL

        self.enemies.update(delta_time)

        for enemy in list(self.enemies):
            if enemy.top < 0:
                enemy.remove_from_sprite_lists()
            elif enemy.top <= HEIGHT and enemy.shot_cooldown <= 0:
                self.enemy_bullets.append(enemy.shoot())

        for bullet in list(self.enemy_bullets):
            bullet.center_y -= 275 * delta_time
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.close()


if __name__ == "__main__":
    window = EnemyDemo()
    arcade.run()
