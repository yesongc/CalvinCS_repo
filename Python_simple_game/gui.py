'''
@author: Yesong Choi
CS108 Final project
Creating the Gui for the game itself

'''

from tkinter import *
from obstacle import *
from player import *
from random import randint
from math import sqrt

def distance_form(x1, x2, y1, y2):
    dist = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return dist


class   Gui:
    def __init__(self, window):
        #Canvas for us to work with
        self.window = window
        self.width = 600
        self.canvas = Canvas(self.window, bg='white',
                        width=self.width, height=self.width)
        self.canvas.grid()
        #change terminated into True if you want to turn it off
        self.terminated = False
        #List of obstacle objects (20 of them)
        self.obstacle_list =[]
        #Timer
        self.timer = 0
        
        #Label for timer
        self.timer_text = IntVar()
        self.timer_text.set(0)
        self.timer_label = Label(window, textvariable=self.timer_text)
        self.timer_label.grid(row = 11, column = 2)
        
        #Text for timer
        self.score_readable = Label(window, text="Score: ")
        self.score_readable.grid(row = 11, column = 1)
        
        
        #button for starting the game
        start_button = Button(window, text="Start", command = self.start)
        start_button.grid(row = 10, column = 1)
        
        #Button for stop
        pause_button = Button(window, text="Pause", command = self.pause)
        pause_button.grid(row = 10, column = 2)
        
        #Button for resuming the game
        resume_button = Button(window, text="Resume", command = self.resume)
        resume_button.grid(row = 10, column = 3)
        
        #Creating a button for restart
        restart_button = Button(window, text="Restart", command = self.restart)
        restart_button.grid(row = 10, column = 4)
        
        
        #Label for Game over
        self.gameover_text = StringVar()
        self.gameover = Label(window, textvariable= self.gameover_text)
        self.gameover_text.set("")
        self.gameover.grid(row = 12, column =3 )
        
        #Creating a highscore text file to keep highscores
        highscore_file = open("highscores.txt", 'r')
        self.highscore = int(highscore_file.readline())
        highscore_file.close()
        
        
        #Label for highscores
        self.highscore_text = IntVar()
        self.highscore_text.set(self.highscore)
        self.highscore_label = Label(window, textvariable = self.highscore_text)
        self.highscore_label.grid(row = 11, column = 4)
        
        #Text for highscore
        self.highscore_readable = Label(window, text="Current Highscore: ")
        self.highscore_readable.grid(row = 11, column = 3)
        
        self.player = Player(self.canvas)
        self.create_obstacles()
        
       #Creating 25 obstacles that are at the top of the screen
       #Has random radius, has random speed, moves in a random direction
    def create_obstacles(self):
        #Initializing the game
        #render a player's head on the canvas
        
        num_obstacle = 0
        start = 0
        while start < 600 and num_obstacle < 25:
            obstacles = Obstacles(randint(5,15), randint(100,500),15, randint(1,10), randint(1,10) )
            space = randint(0,20)
            new_x = start + obstacles.get_radius() + space
            start = new_x + obstacles.get_radius()
            obstacles.set_x(new_x)
            self.obstacle_list.append(obstacles)
            num_obstacle += 1
        
        
        

    
    def start(self):
        #Animation loop
        while not self.terminated:
            self.canvas.delete(ALL)
            for obst in self.obstacle_list:
                obst.move(self.canvas)
                obst.render(self.canvas)
                #Obstacles bounce off of one another
                '''
                from the animation loop in lab 12
                particle simulation
                '''
                for obst2 in self.obstacle_list:
                    obst.bounce(obst2)
                    if obst.hits(self.player):
                        highscore_file = open("highscores.txt", 'w')
                        highscore_file.write(str(self.highscore + 1))
                        highscore_file.close()
                        self.game_over()
                        
            self.timer += 1
            self.timer_text.set(self.timer)
            if  self.timer > self.highscore:
                self.highscore = self.timer
                self.highscore_text.set(self.highscore)
                
                        
            self.player.render(self.canvas)
            
            self.canvas.after(50)
            self.canvas.update()
        
    def pause(self):
        self.terminated = True
    
    def resume(self):
        self.terminated = False
        self.start()
        self.gameover_text.set("")
    
    def restart(self):
        self.terminated = False
        self.obstacle_list = []
        self.player = Player(self.canvas)
        self.create_obstacles()
        self.timer = 0
        self.timer_text.set(self.timer)
        self.start()
    
    
    
    def game_over(self):
        self.gameover_text.set("Game Over")
        self.pause()
        
    


if __name__ == '__main__':
    root = Tk()
    root.title('Dodge the balls')    
    app = Gui(root)
    root.mainloop()
