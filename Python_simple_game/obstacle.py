'''
@author: Yesong Choi
Setting methods and attributes for obstacles
Rendering and moving obstacles
Methods for hitting and bouncing
'''
import math
from random import randint


DAMPENING_FACTOR = 0.88  

#Distance formula
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class   Obstacles:
    #Obstacles need to be told their radius, x value, y value, x velocity, and y velocity
    #Did it this way so that I could randomize each of the obstacles' speed and size and location
    def __init__(self, obstacle_radius, obstacle_x, obstacle_y, speed_x, speed_y):
        self.radius = obstacle_radius
        self.obstacle_x = obstacle_x
        self.obstacle_y = obstacle_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    #Actualizing the obstacles on the canvas
    def render(self,canvas):
        canvas.create_oval(self.obstacle_x - self.radius,
                            self.obstacle_y - self.radius, 
                            self.obstacle_x + self.radius, 
                            self.obstacle_y + self.radius)
    
    #Allowing for the obstacles to move around on the canvas and bounce off any edges
    def move(self, canvas):
        self.obstacle_x += self.speed_x
        self.obstacle_y += self.speed_y
        if  self.obstacle_x + self.radius > canvas.winfo_reqwidth() or self.obstacle_x - self.radius <0:
            self.speed_x = -self.speed_x
        if  self.obstacle_y + self.radius > canvas.winfo_reqwidth() or self.obstacle_y - self.radius <0:
            self.speed_y = -self.speed_y
    
    
    '''
    Got these codes from Lab 12 (particles extra credit part)
    Hits, bounce
    '''
    
    def hits(self, other):
        if (self == other):
        # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self.radius + other.get_radius()) >= distance(self.obstacle_x, self.obstacle_y, other.get_x(), other.get_y())


    def bounce(self, target):
        ''' This method modifies this Particle object's velocities based on its
            collision with the given target particle. It modifies both the magnitude
            and the direction of the velocities based on the interacting magnitude
            and direction of particles. It only changes the velocities of this
            object; an additional call to bounce() on the other particle is required
            to implement a complete bounce interaction.
      
            The collision algorithm is based on a similar algorithm published by K.
            Terzidis, Algorithms for Visual Design.
      
            target  the other particle
         '''
        if self.hits(target):
            angle = math.atan2(target.get_y() - self.obstacle_y, target.get_x() - self.obstacle_x)
            targetX = self.obstacle_x + math.cos(angle) * (self.radius + target.get_radius())
            targetY = self.obstacle_y + math.sin(angle) * (self.radius + target.get_radius())
            ax = targetX - target.get_x()
            ay = targetY - target.get_y()
            self.speed_x = (self.speed_x - ax) * DAMPENING_FACTOR
            self.speed_y = (self.speed_y - ay) * DAMPENING_FACTOR
    
    
    
    
    #Accessors
    def get_x(self):
        return self.obstacle_x
    
    def get_y(self):
        return self.obstacle_y
    def get_radius(self):
        return self.radius
    
    #Mutator
    def set_x(self,num):
        self.obstacle_x = num




