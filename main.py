"""
This is a password generation and encryption tool.
This Software is provided as is without any warranty. In no case should the Author be liable for the Software.
Tim Hartmann , November 2015
"""
import random , os , math , binascii , base64 , getpass
from tkinter import Tk
from Crypto.Cipher import AES
from backbone import switch , DataModule , Mngmnt

#resolution
width = 800
height = 600
#Tkinter Setup
r = Tk()
r.withdraw()

M = Master(width,height)

Hold = Mngmnt()
Hold.loadPwFile()

Hold.savePwFile()
