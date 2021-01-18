# This program was made on Monday January 18th 2021 at 5:30pm
# It's purpose was to make a youtube video downloader as 
# a website I used to do the same thing attempted to give me a virus.
# I made this open source so others could see it's not nefarious in any way. 
#
# Thanks for reading this if you do. 

from pytube import YouTube
import os 
import sys
from pathlib import Path

from tkinter import * 
from tkinter.ttk import *

default_path = f"{str(os.path.splitext(Path(__file__).absolute())[0])[:-4]}\downloads"

# Defining for Tkinter
# --------------------
master = Tk() 
master.geometry("500x500") 

# This is simply a function to help keep it sorted away.
def creating_ui():
    default_path = f"{str(os.path.splitext(Path(__file__).absolute())[0])[:-4]}\downloads"

    label = Label(master,  
                text ="Youtube Video Downloader | V1 \n\n") 
    label.pack()
    label = Label(master,  
                text ="Video Link: (REQUIRED)") 
    label.pack()

    videoentry = Entry(master, width = 50)
    videoentry.pack()

    label = Label(master,  
                text ="Download Path: (empty for default)") 
    label.pack()

    pathentry = Entry(master, width = 50)
    pathentry.pack()
    pathentry.config(text=default_path)

    label = Label(master,  
                text ="Video Name: (empty for default)") 
    label.pack()

    nameentry = Entry(master, width = 50)
    nameentry.pack()

    button = Button(master, text="Download Video", width = 50, command= lambda: download_video(videoentry.get(), pathentry.get(), nameentry.get()))
    button.pack()
    global statusLabel
    statusLabel = Label(master, text="Status: ")
    statusLabel.pack()

# This is the function when the button to download is clicked
def download_video(youtube_video_url, path, name):
    global statusLabel
    # Grab the URL from the text box.
    if path:
        pass
    else:
        path = default_path

    if name:
        pass
    else:
        name = f"{youtube_video_url[-6:]}"

    if youtube_video_url:
        pass
    else:
        statusLabel.config(text=f"Status: Please Enter A Valid Link!")
        return

    try:
        yt_obj = YouTube(youtube_video_url)
    
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    
        filters.get_highest_resolution().download(output_path=path, filename=name)
        print('Video Downloaded Successfully')
        statusLabel.config(text=f"Status: Download Successful")
    except Exception as e:
        print(e)
        statusLabel.config(text=f"Status: {e}" + "\n Please Check Your Link!")

# Running the tkinter window 
creating_ui()
mainloop() 
