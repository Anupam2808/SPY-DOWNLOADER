from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import pytube
import youtube_dl
from tkinter import *
from tkinter.ttk import *

ydl_opts = {}
#ydl_opts = {}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])



root= tk.Tk()
root.title('Youtube Downloader (Created By Spidy)')

root.geometry('500x300')
root.resizable(0, 0)

def use():      

    explain = "(1)First Copy The Link Of the Youtube Video \n (2)Then Paste the Link IN the Textbox \n (3)Then Press The Download Button \n (4)The file will get downloaded"

    label3 = tk.Label(root, text=explain)
    label3.place(x = 0,
    y = 0,
    width=290,
    height=120)


# Creating Menu ...
menubar = Menu(root) 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = file) 
file.add_command(label ='How To Use App', command = use) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()


entry1 = tk.Entry (root) 
entry1.place(x = 180,
y = 130,
width=140,
height=20)



def Video():  
    link = entry1.get()
    try:
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            
        ans= "Successfully Dowloaded Video "
        root.after(2000,reset)
    except Exception:
        ans= "Not Able To Download Youtube Video"
        root.after(2000,reset)
        label1 = tk.Label(root, text=ans)
        canvas1.create_window(200, 280, window=label1)

def Audio():

    URL = entry1.get()
    from youtube_dl import YoutubeDL
    audio_downloader = YoutubeDL({'format':'bestaudio'})
    try:
        
        audio_downloader.extract_info(URL)

        ans=  "Audio Downloaded "
        root.after(2000,reset)
    except youtube_dl.utils.DownloadError as e:
        ans= "Couldn't download the audio"
        root.after(2000,reset)

        label2 = tk.Label(root, text=ans)
        canvas1.create_window(200, 290, window=label2)

def reset():
    label2 = tk.Label(root, text='                                                  ')
    canvas1.create_window(200, 290, window=label2)
    label1 = tk.Label(root, text='                                                                                   ')
    canvas1.create_window(200, 280, window=label1)



button1 = tk.Button(text='Download Video', command=Video, bg="gold" )
button2 = tk.Button(text='Download Audio', command=Audio, bg="sky blue")
label1 = tk.Label(root, text="")
label2 = tk.Label(root, text="")

canvas1.create_window(200, 180, window=button1)
canvas1.create_window(200, 220, window=button2)

root.config(menu = menubar)
root.mainloop()
