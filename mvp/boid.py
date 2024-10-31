import pygame as pg
import random
import math
import globals as gb

class Boid:
    def __init__(self):
        self.position   = [random.randint(0, gb.WIDTH), random.randint(0, gb.HEIGHT)]
        self.speed      = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
        self.color      = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.size       = 10
        self.triangle   = self.create_triangle()
        self.max_speed  = 2

    def create_triangle(self):
        triangle_surf = pg.Surface((self.size, self.size), pg.SRCALPHA)
        pg.draw.polygon(triangle_surf, self.color, [(0, self.size / 2), (self.size, 0), (self.size, self.size)])
        return triangle_surf

    def get_angle(self):
        sx, sy = self.speed
        return math.degrees(math.atan2(sy, -sx))
    
    def draw(self, screen):
        angle = self.get_angle()
        rotated_triangle = pg.transform.rotate(self.triangle, angle)
        rect = rotated_triangle.get_rect(center=(int(self.position[0]), int(self.position[1])))
        screen.blit(rotated_triangle, rect.topleft)

    def update_position(self, boids):
        # Aplicar as três regras dos boids
        separation  = self.separation(boids)
        alignment   = self.alignment(boids)
        cohesion    = self.cohesion(boids)
        

        speed_magnitude = math.sqrt(self.speed[0]**2 + self.speed[1]**2)
        if speed_magnitude > self.max_speed:
            self.speed[0] = (self.speed[0] / speed_magnitude) * self.max_speed
            self.speed[1] = (self.speed[1] / speed_magnitude) * self.max_speed
            
        self.speed[0] += separation[0] + alignment[0] + cohesion[0]
        self.speed[1] += separation[1] + alignment[1] + cohesion[1]


        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        
        if self.position[0] < 0:
            self.position[0] = gb.WIDTH
        elif self.position[0] > gb.WIDTH:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = gb.HEIGHT
        elif self.position[1] > gb.HEIGHT:
            self.position[1] = 0
        #self.position[0] += self.speed[0]
        #self.position[1] += self.speed[1]

        #self.border_collision()

    def border_collision(self):
        if self.position[0] <= 0 or self.position[0] >= gb.WIDTH:
            self.speed[0] *= -1
        if self.position[1] <= 0 or self.position[1] >= gb.HEIGHT:
            self.speed[1] *= -1

    def euclidean_distance(self, boid):
        return math.sqrt((self.position[0] - boid.position[0]) ** 2 + (self.position[1] - boid.position[1]) ** 2)

    def alignment(self, boids):
        xvel_average = 0
        yvel_average = 0
        boids_in_range = []

        for boid in boids:
            if boid != self:
                distance = self.euclidean_distance(boid)
                if distance < gb.DISTANCE_THRESHOLD:
                    boids_in_range.append(boid)

        
        for boid in boids_in_range:
            xvel_average += boid.speed[0]
            yvel_average += boid.speed[1]

        if len(boids_in_range) > 0:
            xvel_average /= len(boids_in_range)
            yvel_average /= len(boids_in_range)

            return [(xvel_average - self.speed[0]) * 0.01, (yvel_average - self.speed[1]) * 0.01]
        
        return [0, 0]

    def cohesion(self, boids):
        xpos_average = 0
        ypos_average = 0

        boids_in_range = []

        for boid in boids:
            if boid != self:
                distance = self.euclidean_distance(boid)
                if distance < gb.DISTANCE_THRESHOLD:
                    boids_in_range.append(boid)

        for boid in boids_in_range:
            xpos_average += boid.speed[0]
            ypos_average += boid.speed[1]

        if len(boids_in_range) > 0:
            xpos_average /= len(boids_in_range)
            ypos_average /= len(boids_in_range)

            return [(xpos_average - self.position[0]) * 0.01, (ypos_average - self.position[1]) * 0.01]
        
        return [0, 0]

    def separation(self, boids):
        direction = [0, 0]
        boids_in_range = []

        for boid in boids:
            if boid != self:
                distance = self.euclidean_distance(boid)
                if distance < gb.DISTANCE_THRESHOLD:
                    boids_in_range.append(boid)

        for boid in boids_in_range:
            ratio_x = max(0, min((self.position[0] - boid.position[0]) / gb.DISTANCE_THRESHOLD, 1))
            ratio_y = max(0, min((self.position[1] - boid.position[1]) / gb.DISTANCE_THRESHOLD, 1))
            direction[0] += (self.position[0] - boid.position[0]) * ratio_x
            direction[1] += (self.position[1] - boid.position[1]) * ratio_y
            magnitude = math.sqrt(direction[0]**2 + direction[1]**2)
            if magnitude > 0:
                direction[0] = (direction[0] / magnitude) * min(magnitude, self.max_speed)
                direction[1] = (direction[1] / magnitude) * min(magnitude, self.max_speed)

        return direction
            
    