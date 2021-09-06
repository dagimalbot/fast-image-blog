"""
FAST IMAGE SCRAPER <CLI>
Author  : Dagimal
E-mail  : daffagifariakmal@gmail.com
Date    : 31-August-2021
Version : 1.0
"""
import blogger
import os
from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

#def banner(): #Function
print(
"""
 __________________
 ___  __/__(_)__  /_
 __  /_ __  /__  __ \\
 _  __/ _  / _  /_/ /
 /_/    /_/  /_.___/
  Fast Image Blog v1.0
   >>> Scraper & AGC Blogspot
  Created By Dagimal
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

#def blogger_upload():
	

#Call Banner
#banner()
mainMenu()

#Input1
input1 = input(' >> ')

secondMenu()

#Case
#if input1 == '1':
#	if input2 == '1':

