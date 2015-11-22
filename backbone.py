import random , os , math , binascii , base64 , getpass , hashlib
from tkinter import Tk
from Crypto.Cipher import AES

#https://code.activestate.com/recipes/410692/
class switch(object):
	def __init__(self , value):
		self.value = value
		self.fall = False
	def __iter__(self):
		"""Retrun the match method once, then stop"""
		yield self.match
		raise StopIteration
	def match(self, *args):
		"""Indicate whether or not to enter a case suite"""
		if self.fall or not args:
			return True
		else:
			return False
#usage:
# for case in switch(x):
# if case(value):
# if case() -< returns if no other value matches

class DataModule:
	def __init__(self, name, password, website):
		self.website = website
		self.password = password
		self.name = name
class Mngmnt:
	def __init__(self,password):
		self.secret = hashlib.md5(password.encode('utf-8')).hexdigest()
		self.cipher = AES.new(self.secret)
		#Encryption Setup
		self.BLOCK_SIZE = 32
		self.PADDING = '{'
		self.pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
		self.EncodeAES = lambda c , s: base64.b64encode(c.encrypt(pad(s)))
		self.DecodeAES = lambda c , e: c.decrypt(base64.b64decode(e)).decode('utf-8').rstrip(PADDING)
		self.PASSWORD_LENGHT = 50
		self.CHARS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','?','*','&','"','+','-']
		self.data = []
	def encrypt(self.data):
		encoded = EncodeAES(cipher,data)
		return encoded
	def decrypt(self.data):
		decrypt = DecodeAES(cipher,data)
		return decoded
	def loadPwFile():
		if os.stat("pws.encr").st_size == 0:
			return 0
		else:
			s = open("pws.encr","rt")
			dt = s.readline()
			dt = decrypt(dt)
			dt = dt.split("$")
			del dt[len(dt)-1]
			for i in dt:
				x = i.split("#")
				x[2] = x[2].replace("\n","")
				dm = DataModule(x[0],x[1],x[2])
				self.data.append(dm)
	def savePwFile():
		s = open("pws.encr","wt")
		b = ""
		for i in self.data:
			b += str(i.name+"#"+i.password+"#"+i.website)
			b += "$"
		b = encrypt(b).decode('utf-8')
		s.write(b)
	def genPassword():
		x = int(binascii.hexlify(os.urandom(8)).decode('utf-8'),16)
		y = int(binascii.hexlify(os.urandom(5)).decode('utf-8'),16)
		c = int(binascii.hexlify(os.urandom(2)).decode('utf-8'),16)
		ps = []
		pw = ""
		i = 0
		while x > len(CHARS):
			i += 1
			ps.append(x % len(CHARS))
			x -= y
			if i > 100000:
				break
		for i in range(PASSWORD_LENGHT):
			pw += str(CHARS[ps[c]])
		return pw
	def addNewEntryG(name,website):#Generate a new random Password for this website
		self.data.append(DataModule(name,genPassword(),website))
	def addNewEntryM(name,password,website):#Use the user's password
		self.data.append(DataModule(name,password,website))

	