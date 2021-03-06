#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='#BFF5ED')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="#FF9D1C", outline="#FF9D1C")
player = drawpad.create_rectangle(240,240,260,260, fill="#29C462", outline="#29C462")
direction = 1


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
       	        self.up.configure(text="Up", background= "#8AD6FF")
       	        self.up.grid(row=0,column=1)
       	        self.up.bind("<Button-1>", self.upClick)
       	    
       	        self.left = Button(self.myContainer1)
	        self.left.configure(text="Left", background= "#8AD6FF")
	        self.left.grid(row=1,column=0)
	        self.left.bind("<Button-1>", self.leftClick)
		
	        self.right = Button(self.myContainer1)
	        self.right.configure(text="Right", background= "#8AD6FF")
	        self.right.grid(row=1,column=2)											
	        self.right.bind("<Button-1>", self.rightClick)
            
                self.down = Button(self.myContainer1)
	        self.down.configure(text="Down", background= "#8AD6FF")
	        self.down.grid(row=2,column=1)											
	        self.down.bind("<Button-1>", self.downClick)
				
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
	        self.animate()
		
	def upClick(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
	   global drawpad
	   global player
           x1,y1,x2,y2 = drawpad.coords(player)
	   if y1 > 0:
	       drawpad.move(player,0,-20)
		
		
	def leftClick(self, event):   
	   global player
           x1,y1,x2,y2 = drawpad.coords(player)
           if x1 > 5:
	       drawpad.move(player,-20,0)
                	   
	def rightClick(self, event):  
	   global player		
           x1,y1,x2,y2 = drawpad.coords(player)
           if x2 < 480:     
	       drawpad.move(player,20,0)
                		
	def downClick(self, event): 
	   global player
	   drawpad.move(player,0,20)
           x1,y1,x2,y2 = drawpad.coords(player)
	   if y2 > 320:
	       drawpad.move(player,0,-20)
	def animate(self):
            global direction 
            global target
            x1, y1, x2, y2 = drawpad.coords(target)
            px1,py1,px2,py2 = drawpad.coords(player)
            if x2 > drawpad.winfo_width():
                direction = - 7
            elif x1 < -5:
                direction = 7

            
            didWeHit = self.collisionDetect()
            if didWeHit == False:
                drawpad.move(target,direction,0)
            drawpad.after(10, self.animate)       
	
        def collisionDetect(self):
            global oval
	    global drawpad
            x1, y1, x2, y2 = drawpad.coords(target)
            px1,py1,px2,py2 = drawpad.coords(player)
            if (px1>=x1 and px2<=x2) and (py1>=y1 and py2<=y2):
                return True
            else:
                return False

		# Ensure that we are doing our collision detection
		# After we move our object!
		

	    
	    

                # Do your if statement - remember to return True if successful!
                
myapp = MyApp(root)

root.mainloop()