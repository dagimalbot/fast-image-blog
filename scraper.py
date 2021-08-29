"""
FAST IMAGE SCRAPER
Author  : Dagimal
E-mail  : daffagifariakmal@gmail.com
Date    : 29-August-2021
Version : 1.0
"""

import PySimpleGUI as sg

sg.theme('Reddit')
#sg.ChangeLookAndFeel('black')
layout = [[sg.Text('FAST IMAGE SCRAPER',justification='center',size=(40, 1))],
	[sg.Multiline(size=(40,20), key='textbox')],
	[sg.Radio('Google','RADIO1',default=True,key='google'),sg.Radio('Hotlink','RADIO2',default=True,key='hotlink')],
	[sg.Radio('Bing','RADIO1',default=False),sg.Radio('Download','RADIO2',default=False,key='download')],
	[sg.Button('SCRAPE',size=(40,2))]]


win = sg.Window('Fast Image Scraper',icon='icon.png').Layout(layout)
e,v=win.read()
win.close()
