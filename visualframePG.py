import pygame

class Master:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.screen = pygame.set_mode((width,height))
		self.canvases = []
	def update(self):
		pygame.display.flip()
		pygame.time.Clock().tick(16)
	class Canvas:
		def __init__(self,width,height,x,y,color):
			self.width = width
			self.height = height
			self.x = x
			self.y = y
			self.color = color
			self.surface = pygame.Surface((width,height))
			self.interactors = []#holds erverything on the canvas
		def update(self):
			for i in self.interactors:
				self.surface.blit(i.surface,(i.x,i.y))
		class Button:
			def __init__(self,width,height,x,y,color,text,textcolor):
				self.x = x
				self.y = y
				self.width = width
				self.height = height
				self.color = color
				self.text = text
				self.textcolor = textcolor
				self.surface = pygame.Surface((width,height))
			def update(self):
				t = pygame.font.Font(None,22).render(self.text,True,self.textcolor)
				self.surface.blit(t,(x,y))
		class Label:	
			def __init__(self,width,height,x,y,text,textcolor):
				self.width = width
				self.height = height
				self.x = x
				self.y = y
				self.text = text
				self.textcolor = textcolor
def preRun():
	return password