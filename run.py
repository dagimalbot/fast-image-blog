"""
FAST IMAGE BLOG <CLI>
Author  : Dagimal
E-mail  : daffagifariakmal@gmail.com
Date    : 31-August-2021
Version : 1.0
"""
import blogger
import os
from simple_image_download import simple_image_download as simp
from subprocess import call
from tqdm import tqdm
from bing_image_urls import bing_image_urls

response = simp.simple_image_download

def banner(): #Function
	print(
	"""
	__________________
	___  __/__(_)__  /_
	__  /_ __  /__  __ \\
	_  __/ _  / _  /_/ /
	/_/    /_/  /_.___/
	Fast Image Blog v1.0
	>>> Scraper & AGC Blogspot
	Created By Dagimal <daffagifariakmal@gmail.com>
	------------------------
	""")

def main():
	menu()

def clear(): # Clear Screen Function
	# Check and make call for specific operating system
	_ = call('clear' if os.name == 'posix' else 'cls')

def menu():
	banner()
	print('@@@@@@@@@@@@ WELCOME @@@@@@@@@@@@')
	choice = input('''
		[1] Scrape Image
		[2] Build Article

		Please enter your choice : ''')
	if choice == '1':
		scrapeImage()
	elif choice == '2':
		buildArticle()
	else:
		clear()
		banner()
		menu()

#def buildArticle():


def scrapeImage():
	clear()
	banner()
	print('		@@@@@@@@@@@@ SEARCH ENGINE @@@@@@@@@@@@')
	searchEngine = input('''
		[1] Google
		[2] Bing

		Please enter your choice : ''')

	# Search Engine Function
	def googleSearch():
		clear()
		banner()
		print('		@@@@@@@@@@@@ GOOGLE @@@@@@@@@@@@')
		file = open('keyword.txt','r').readlines()
		for i in tqdm(file):
			saveFile = open('output/google/'+i.replace('\n','')+'.txt','w')
			print('\n'.join(response().urls(i, 5000)), file=saveFile)

	def bingSearch():
		clear()
		banner()
		print('@@@@@@@@@@@@ BING @@@@@@@@@@@@')
		file = open('keyword.txt','r').readlines()
		for i in tqdm(file):
			saveFile = open('output/bing/'+i.replace('\n','')+'.txt','w')
			print('\n'.join(bing_image_urls(i, limit=5000)), file=saveFile)

	if searchEngine == '1':
		googleSearch()
	elif searchEngine == '2':
		bingSearch()
	else:
		clear()
		scrapeImage()
	#f = open('output/hotlink/'+fileName)

main()
