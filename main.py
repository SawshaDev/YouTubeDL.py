from pytube import YouTube
import os
import pyfiglet


import colorama
from colorama import Fore

colorama.init(autoreset=True)

ascii_banner = pyfiglet.figlet_format("YoutubeDl . py")

print(ascii_banner)
print("-----------------------------------------------------------")

print("What would you like to download? \n")
URl_ask= input(f"{Fore.RED}Please Insert video link here: ")

yt = YouTube(URl_ask)

name_video = yt.title


print(f"{Fore.WHITE}-----------------------------------------")
print(f"{Fore.GREEN}{name_video} ")                           #print video name
print(f"{Fore.WHITE}-----------------------------------------")
stream_mp4 = yt.streams.filter(file_extension='mp4').get_by_itag(22)
stream_mp3 = yt.streams.filter(only_audio=True).get_by_itag(139)

ask_videofile = input("Mp3 or Mp4?: ")



if os.path.exists(f"video/{name_video}.{ask_videofile}"):
    print(f"The File {name_video}.{ask_videofile} Exists Sadly.")
        
else:
    if ask_videofile == "mp3":
        stream_mp3.download(filename = f"{name_video}.mp3", 
        output_path = "video") 
            
            
    if ask_videofile == "mp4":
        stream_mp4.download(filename=f"{name_video}.mp4",
        output_path = "video")

    print(f"succesfully downloaded {name_video}.{ask_videofile}! go check it out in 'video/' Folder!")    





