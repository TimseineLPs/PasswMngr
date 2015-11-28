"""
This is a password generation and encryption tool.
This Software is provided as is without any warranty. In no case should the Author be liable for the Software.
Tim Hartmann , November 2015
"""
import random , os , binascii , base64 , getpass
from tkinter import Tk
from Crypto.Cipher import AES

#https://code.activestate.com/recipes/410692/
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
#usage:
# for case in switch(x):
# if case(value):
# if case() <- returns if no other value matches

class DataModule:
	def __init__(self,name,password,website):
		self.website = website
		self.password = password
		self.name = name

def encrypt(data):
	#return str(data)#for development only NO ENCRYPTION !!!
	encoded = EncodeAES(cipher,data)
	return encoded
def decrypt(data):
	#return str(data)#for development only NO ENCRYPTION !!!
	decoded = DecodeAES(cipher,data)
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
			data.append(dm)
def savePwFile():
	s = open("pws.encr","wt")
	b = ""
	for i in data:
		b += str(i.name+"#"+i.password+"#"+i.website)
		b += "$"
	b = encrypt(b).decode('utf-8')
	s.write(b)

#def loadSettings():

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
		pw += str(CHARS[ps[c+i]])
	return pw
def addNewEntryG(name,website):#Generate a new random Password for this website
	data.append(DataModule(name,genPassword(),website))
def addNewEntryM(name,password,website):#Use the users Password
	data.append(DataModule(name,password,website))

GlobPasswd = getpass.getpass("Enter your Master-Password(16 character minimum recomended):")
while len(GlobPasswd) < 32:
	GlobPasswd += GlobPasswd
#Encryption Setup
BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c , s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c , e: c.decrypt(base64.b64decode(e)).decode('utf-8').rstrip(PADDING)

secret = GlobPasswd.encode('utf-8')[0:32]
cipher = AES.new(secret)

#Password-Generation Setup
PASSWORD_LENGHT = 50#Safer Config random.randint(50,53) -> more password-lenghts to bruteforce | not needed
CHARS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','.',',','?','*','&','"','+','-']

#Tkinter Setup
r = Tk()
r.withdraw()
data = []

loadPwFile()

run = True
while run:
	choice = input(">")
	for case in switch(choice):
		if case("ls") or case("list"):
			for i in range(len(data)):
				print(str(i)+". >"+data[i].name+" : "+data[i].password+" : "+data[i].website)
		elif case("cp website"):
			choice = int(input("Index >>"))
			if choice >= 0 and choice < len(data):
				r.withdraw()
				r.clipboard_clear()
				r.clipboard_append(data[choice].website)
			else:
				print("Index out of bounds!")
		elif case("cp password"):
			choice = int(input("Index >>"))
			if choice >= 0 and choice < len(data):
				r.withdraw()
				r.clipboard_clear()
				r.clipboard_append(data[choice].password)
			else:
				print("Index out of bounds!")
		elif case("cp name"):
			choice = int(input("Index >>"))
			if choice >= 0 and choice< len(data):
				r.withdraw()
				r.clipboard_clear()
				r.clipboard_append(data[choice].name)
			else:
				print("Index out of bounds!")
		elif case("add new"):
			name =     input("Username >>")
			website =  input("Website  >>")
			addNewEntryG(name,website)
		elif case("add manual"):
			name =     input("Username >>")
			password = input("Password >>")
			website =  input("Website  >>")
			addNewEntryM(name,password,website)
		elif case("rm"):
			index =    input("Index    >>")
			confirm = input("Are you sure you want to delete the Entry at Index "+str(index)+" ?(y/n)")
			if confirm == "y":
				del data[int(index)]
		elif case("exit") or case("close"):
			run = False
		elif case("edit"):
			index =    input("Index    >>")
			c = input("Name, Password, Website(n/p/w)>>") 
			new = input("New Value  >>")
			if c == "n":
				data[int(index)].name = new
			elif c == "p":
				data[int(index)].password = new
			elif c == "w":
				data[int(index)].website = new
			else:
				pass
		elif case("regen"):
			index = input("Index    >>")
			data[int(index)].password = genPassword()
		else:
			print("Invalid option!")

savePwFile()
