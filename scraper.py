import PySimpleGUI as sg

sg.theme('Reddit')
#sg.ChangeLookAndFeel('black')
layout = [[sg.Text('FAST IMAGE SCRAPER',justification='center',size=(40, 1))],
	[sg.Multiline(size=(40,20), key='textbox')],
	[sg.Radio('Google','RADIO1',default=True,key='google')],
	[sg.Radio('Bing','RADIO1',default=False)],
	[sg.Button('SCRAPE',size=(40,2))]]


win = sg.Window('Fast Image Scraper',layout, ttk_theme='clam')
e,v=win.read()
win.close()
