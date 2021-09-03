"""
FAST IMAGE SCRAPER <CLI>
Author  : Dagimal
E-mail  : daffagifariakmal@gmail.com
Date    : 31-August-2021
Version : 1.0
"""

import os
from core.simple_image_download import simple_image_download as simp

response = simp.simple_image_download

def banner(): #Function
	print(
"""
  _____ _____ _____ _____ 
 |   __|     |   __|     |
 |   __|-   -|__   |   --|
 |__|  |_____|_____|_____|
 Fast Image Scraper v1.0
 ------------------------
"""
)
def mainMenu():
	print(' [1] Google')
	print(' [2] Bing')

def secondMenu():
	print(' [1] Hotlink')
	print(' [2] Download')

def googleHotlink(fileName):
	f = open('output/hotlink/'+fileName)

def blogger_upload():
	

#Call Banner
banner()
mainMenu()

#Input1
input1 = input(' >> ')

secondMenu()

#Case
#if input1 == '1':
#	if input2 == '1':

