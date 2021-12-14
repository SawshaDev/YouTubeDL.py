from pytube import YouTube
import os
import pyfiglet


import sys
import time


import colorama
from colorama import Fore

colorama.init(autoreset=True)

#1 by 1
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


#if contributing, do not mess with theses lines 
printy("Warning!")
time.sleep(1)
printy("This project is a WIP and it may not work properly!")
time.sleep(1)
printy("If there are any problems, please report it to the github:  https://github.com/SawshaDev/YoutubeDl.py")
time.sleep(1)
input("Press any key to continue... and enjoy!")
os.system('clear')

ascii_banner = pyfiglet.figlet_format("YoutubeDl . py")

print(ascii_banner)
printy("Official Discord: https://discord.gg/8HbaQBBVWN")
time.sleep(1)
print("-----------------------------------------------------------")

print("What would you like to download? \n")

URl_ask= input(f"{Fore.RED}Please Insert video link here: ")

yt = YouTube(URl_ask)

name_video = yt.title


print(f"{Fore.WHITE}-----------------------------------------")
print(f"{Fore.GREEN}title = {name_video} ")                           #print video name
print(f"{Fore.WHITE}-----------------------------------------")
stream_mp4 = yt.streams.filter(file_extension='mp4').get_by_itag(22)
stream_mp3 = yt.streams.filter(only_audio=True).get_by_itag(139)

ask_videofile = input("Mp3 or Mp4?: ")



if os.path.exists(f"video/{name_video}.{ask_videofile}"):
    print(f"The File {name_video}.{ask_videofile} Exists Sadly. \n",
    "If the file does not exist anywhere in /video folder, Please report it to https://discord.gg/8HbaQBBVWN, or the github ")
        
else:
    if ask_videofile == "mp3":
        stream_mp3.download(filename = f"{name_video}.mp3", 
        output_path = "video") 
            
            
    if ask_videofile == "mp4":
        stream_mp4.download(filename=f"{name_video}.mp4",
        output_path = "video")

    print(f"succesfully downloaded {name_video}.{ask_videofile}! go check it out in '/video' Folder!")    

