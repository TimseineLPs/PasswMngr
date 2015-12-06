"""
This is a password generation and encryption tool.
This Software is provided as is without any warranty. In no case should the Author be liable for the Software.
Tim Hartmann , November 2015
"""
import random , os , binascii , base64 , getpass
from tkinter import Tk
from Crypto.Cipher import AES
from backbone import switch , DataModule , Mngmnt

#resolution
width = 800
height = 600
#Tkinter Setup
r = Tk()
r.withdraw()

_password = ""
_Action_Backbone = ""#used by the frontend to tell the backend to do something
_Msg = ""#message containing additional information about the action
_DataTrans = 0#Variable for transport of larger datasets

Backbone = Mngmnt()

M = Master(width,height)

f = open("getpw.desc","rt")#Layout to get user password
M.build(f.read())
while _password== "":#user has not entered password
	M.main()
f.close()
#Graphics framework updates _password and notifies backend(calling Mngmnt.start(_password))

f = open("main.desc","rt")#Layout for gerneral use
M.build(f.read())
f.close()
while True:
	M.main()
	Backbone.actions()

