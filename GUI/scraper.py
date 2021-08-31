"""
FAST IMAGE SCRAPER
Author  : Dagimal
E-mail  : daffagifariakmal@gmail.com
Date    : 29-August-2021
Version : 1.0
"""

from core.simple_image_download import simple_image_download as simp
import PySimpleGUI as sg

sg.theme('Reddit')
#sg.ChangeLookAndFeel('black')
layout = [[sg.Text('FAST IMAGE SCRAPER',justification='center',size=(40, 1))],
	[sg.Multiline(size=(40,20), key='textbox')],
	[sg.Text('Keyword:'),sg.InputText('kucing',size=(20,2),key='keyword')],
	[sg.Text('Nama File:'),sg.InputText('kucing',size=(20,2),key='fileName')],
	[sg.Text('Jumlah:'),sg.InputText('10',size=(20,2),key='jumlah')],
	[sg.Radio('Google','RADIO1',default=True,key='google'),sg.Radio('Hotlink','RADIO2',default=True,key='hotlink')],
	[sg.Radio('Bing','RADIO1',default=False),sg.Radio('Download','RADIO2',default=False,key='download')],
	[sg.Button('SCRAPE',size=(40,2))]]

#Simple Image Download
response = simp.simple_image_download
#fileName, jumlah

win = sg.Window('Fast Image Scraper',icon='icon.png').Layout(layout)
e,v=win.read()

def googleHotlink():
	f = open('output/hotlink/'+v['fileName']+'.txt','w')
	sg.popup('Tunggu Sebentar ...',button_type=5, icon='icon.png')
	print(response().urls(v['keyword'], 100), file=f)
#def googleDownload():

#def bingHotlink():

#def bingDownload():


#win = sg.Window('Fast Image Scraper',icon='icon.png').Layout(layout)

while True:
	#e,v=win.read()
	if e == 'SCRAPE':
		if v['google'] == True and v['hotlink'] == True:
			#print(v['textbox'])
			#sg.popup_auto_close('Tunggu Sebentar ...', button_type=5, icon='icon.png')
			googleHotlink()
	elif e == sg.WIN_CLOSED:
		break
#	win.close()
