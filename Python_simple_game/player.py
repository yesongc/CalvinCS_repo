'''
Created on 2016. 5. 3.

@author: Yesong Choi
Setting methods and attributes for players
Binding arrow keys to movement methods
Rendering
'''

#Player class, only need one instance of it at the moment.
class Player:
    def __init__(self, canvas):
        self.player_x = 200
        self.player_y = 500
        self.player_radius = 12
        self.player_speed = 15
        
        #Binding the left and right arrows so that we can move the player when pressing the keys
        canvas.bind("<Left>", self.move_left)
        canvas.bind("<Right>", self.move_right)
        canvas.bind("<Up>", self.move_up)
        canvas.bind("<Down>", self.move_down)
        canvas.focus_set()

        
    #Actualizing the player drawing so that it shows up on a canvas.
    #Need to draw the rest of its body (arms, legs) later once I make it move
    def render(self, canvas):
        canvas.create_oval(self.player_x - self.player_radius, 
                           self.player_y - self.player_radius, 
                           self.player_x + self.player_radius, 
                           self.player_y + self.player_radius,
                           fill = "red")
    
    #Commands for the keys that are bound
    def move_left(self, event):
        if  self.player_x - self.player_radius > 0:
            self.player_x -= self.player_speed
        else:
            self.player_x = self.player_radius
    
    def move_right(self, event):
        if  self.player_x + self.player_radius < 600:
            self.player_x += self.player_speed
        else:
            self.player_x = self.player_x
    
    def move_up(self,event):
        if  self.player_y - self.player_radius > 0:
            self.player_y -= self.player_speed
        else:
            self.player_y = self.player_radius
    
    def move_down(self,event):
        if  self.player_y + self.player_radius < 600:
            self.player_y += self.player_speed
        else:
            self.player_y = self.player_y

    
    #Accessor
    
    
    def get_y(self):
        return self.player_y  
    def get_x(self):
        return self.player_x
    def get_radius(self):
        return self.player_radius
    def get_speed(self):
        return self.player_speed