import pygame

class Master:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.screen = pygame.set_mode((width,height))
		self.canvases = []
		self.data_lenght = len(Backbone.data)
	def update(self):
		pygame.display.flip()
		pygame.time.Clock().tick(16)
	def main(self):
		while True:
			for a in self.canvases:
				for b in a.interactors:
					b.update()#Interactor Update
				a.update()#Canvas Update
			self.update()#Update self
	def build(self,desc):
		"""
		descriptive language:
		
		C,100,50,20,40,(255:255:255). #describe Canvas
		I,10,10,5,20,test.png,rm. #Image Button
		B,25,22,5,30,(255:0:0),Caption,(0:255:0),add new. #Normal Button
		L,25,22,5,36,YEEEY,(0:255:0); #semicolon marks end of canvas
		C,10,50,120,40,(0:255:255). #new canvas
		it L,25,22,5,10*i,$,(0:255:122) data-user #Interatively create labels
		it L,25,22,30,10*i,$,(0:255:122) data-password 
		it L,25,22,55,10*i,$,(0:255:122) data-website
		
		saved in file like this
		C,100,50,20,40,(255:255:255).I,10,10,5,20,test.png,rm.B,25,22,5,30,(255:0:0),Caption,(0:255:0),add new.L,25,22,5,36,YEEEY,(0:255:0);C,10,50,120,40,(0:255:255).		
		"""
		self.canvases = []
		desc = desc.split(";")#Canvas Split
		for x in desc:
			x = x.split(".")
			for y in x:
				y = y.split(",")
				
		for i in range(len(desc)):#For every Canvas
			if desc[i][0][0] == "C":#check if file is broken
				CanvasColor = desc[i][0][5].split(":").replace("(","").replace(")","")
				self.canvases.append(Canvas( int(desc[i][0][1]) , int(desc[i][0][2]) , int(desc[i][0][3]) , int(desc[i][0][4]) , ( int(CanvasColor[0]) , int(CanvasColor[1]) ,  int(CanvasColor[2]) ))
			else:
				print("Descriptive File Broken!!!")
			for u in range(len(desc[i])-1):#for everything on the canvas			
		
	class Canvas:
		def __init__(self,width,height,x,y,color,scrollable):
			self.width = width
			self.height = height
			self.x = x
			self.y = y
			self.color = color
			self.surface = pygame.Surface((width,height))
			self.interactors = []#holds erverything on the canvas
			self.scrollable = scrollable
			if self.scrollable:
				self.scrollvalue = 0
		def update(self):
			for i in self.interactors:
				self.surface.blit(i.surface,(i.x,i.y))
		class Button:
			def __init__(self,width,height,x,y,color,text,textcolor,action):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.color = color
				self.text = text
				self.textcolor = textcolor
				self.surface = pygame.Surface((width,height))
				self.action = action
			def update(self):
				self.surface.fill(self.color)
				t = pygame.font.Font(None,22).render(self.text,True,self.textcolor)
				self.surface.blit(t,(0,0))
			def trigger(self):
				global _Action_Backbone
				_Action_Backbone = self.action
		class ImageButton:
			def __init__(self,width,height,x,y,image,action):
				self.image = image
				self.image = pygame.transform.scale(self.image,(self.width,self.height))
				self.x = x
				self.y = y
				self.surface = pygame.Surface((width,height))
				self.action = action
			def update(self):
				self.surface.blit(self.image,(0,0))
			def trigger(self):
				global _Action_Backbone
				_Action_Backbone = self.action
		class Label:	
			def __init__(self,width,height,x,y,text,textcolor):
				self.width = width
				self.height = height
				self.x = x
				self.y = y
				self.text = text
				self.textcolor = textcolor
			def update(self):
				self.surface.fill((255,0,255))
				t = pygame.font.Font(None,22).render(self.text,True,self.textcolor)
				self.surface.blit(t,(0,0))
				self.surface.set_colorkey((255,0,255))
			def trigger(self):
				pass
				
def preRun():
	global _password
	#ask the user for the password
	_password = ...