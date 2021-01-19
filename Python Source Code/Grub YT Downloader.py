# This program was created 

from pytube import YouTube
import os 
import sys
from pathlib import Path

from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
default_path = f"{os.path.dirname(str(os.path.splitext(Path(__file__).absolute())[0]))}\downloads"
normal_path = f"{os.path.dirname(str(os.path.splitext(Path(__file__).absolute())[0]))}"
# Defining for Tkinter
# --------------------
master = Tk() 
master.geometry("500x300") 
#master.iconbitmap(f"{normal_path}\icon.ico")
master.title("Grub YouTube Downloader")

# This is simply a function to help keep it sorted away.
def creating_ui():
    default_path = f"{os.path.dirname(str(os.path.splitext(Path(__file__).absolute())[0]))}\downloads"
    # Label for progam and the video link text box
    label = Label(master,  
                text ="Youtube Video Downloader | V1.5 \n\n") 
    label.pack()
    label = Label(master,  
                text ="Video Link: (REQUIRED)") 
    label.pack()
    # Link text box
    videoentry = Entry(master, width = 50)
    videoentry.pack()
    # Path Lable for text box
    label = Label(master,  
                text ="Download Path: (empty for default)") 
    label.pack()
    # Path text box
    pathentry = Entry(master, width = 50)
    pathentry.config(text=default_path)
    pathentry.pack()
    # Label for Filename text box
    label = Label(master,  
                text ="Video Name: (empty for default)") 
    label.pack()
    # Filename text box
    nameentry = Entry(master, width = 50)
    nameentry.pack()
    # Video Button 
    button = Button(master, text="Download Video (mp4)", width = 50, command= lambda: download_video(videoentry.get(), pathentry.get(), nameentry.get(), 'video'))
    button.pack()
    # Audio Button
    button2 = Button(master, text="Download Audio Only", width = 50, command= lambda: download_video(videoentry.get(), pathentry.get(), nameentry.get(), 'audio'))
    button2.pack()
    global statusLabel
    statusLabel = Label(master, text="Status: ")
    statusLabel.pack()

# This is the function when the button to download is clicked
def download_video(youtube_video_url, path, name, mode):
    global statusLabel
    # Grab the URL from the text box.
    if path:
        pass
    else:
        path = default_path

    if youtube_video_url:
        pass
    else:
        statusLabel.config(text=f"Status: Please Enter A Valid Link!")
        return

    try:
        yt_obj = YouTube(youtube_video_url)

        if name: # This is here so we can grab the yt vid title
            pass
        else:
            name = f"{yt_obj.title}"

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        if mode == 'video':
            filters.get_highest_resolution().download(output_path=path, filename=name)
        elif mode == 'audio':
            yt_obj.streams.get_audio_only().download(output_path=path, filename=name)

        print('Downloaded Successfully')
        statusLabel.config(text=f"Status: Download of {yt_obj.title} {mode} was Successful!")
    except Exception as e:
        print(e)
        statusLabel.config(text=f"Status: {e}" + "\n Please Check Your Link!")

# Running the tkinter window 
creating_ui()
mainloop() 