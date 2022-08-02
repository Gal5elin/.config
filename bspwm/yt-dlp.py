# yt-dlp program

import subprocess
import os
import time
from subprocess import Popen, PIPE
from subprocess import DEVNULL, STDOUT, check_call

#echo 'Please input your url:'
url = input('Please input your url: ')

#print("Please choose what you want to do: 1 -> mp3 || 2 -> mp4")
choice = input("Please choose what you want to do: 1 -> mp3 || 2 -> mp4 ")


def mp3():
	print()
	#title = os.system(f'yt-dlp --extract-audio -f "bestaudio" --no-playlist --audio-format mp3 -s -O "title" {url}')
	title = subprocess.check_output(f'yt-dlp --extract-audio -f "bestaudio" --no-playlist --audio-format mp3 -s -O "title" {url}', shell=True)
	title2 = title.decode()
	print(f'Found {title2}')
	dl = input('Do you want to download it? (y/n) ')
	if dl == 'y':
		print(f"Downloading {title2}")
		os.system('yt-dlp --extract-audio -f "bestaudio" --no-playlist --audio-format mp3' + ' ' + url)

def mp4():
	print("fuck off")

if choice == '1':
	mp3()
elif choice == '2':
	mp4()
else:
	print('bruh')
	exit
