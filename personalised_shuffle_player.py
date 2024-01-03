import os
import random
import pygame
import time
from getkey import getkey, key

#Step 1
print("""
Hello!
This is a shuffle player specially designed for History of Jazz 103.
The aim of this player is to help you practice the listening at anytime and anywhere.
Before beginning, this program will take you through two simple steps with detailed descriptions.
Hope you like it!
""")
print(
"""Step 1: DOWNLOADING THE SONGS
1)Copy the given link below and paste it on to your browser: [ https://spotify-downloader.com/ ]
2)Enter the link of your spotify jazz playlist link given to you by your professor in the space box in the website.
3)Click on "Submit".
4)The playlist and songs download options will appear. Click the 'Download ZIP' button in the first option to download the entire playlist.
5)After the download is complete, click "Save ZIP" and complete human verification by clicking on "Start Verification".
6)Your songs are finally downloaded. Now store it on a folder on your Computer/PC.
""") 

#Step 2
path = '/Users/arushiagrawal/Desktop/Jazz😭/Songs'
if path == "":
    print("Step 2: ENTERING THE PATH TO YOUR FOLDER")
    path = input("Enter the path to your directory/folder containing your downloaded songs (example: /Users/username/Desktop/Jazz/Songs): ")
    print("You're all set for the test. All the best!", end = "\n\n")

list_of_files = [f for f in os.listdir(path) if f.endswith('.mp3')]
pygame.mixer.init()
final_shuffled_playlist = list_of_files.copy()
random.shuffle(final_shuffled_playlist) 

def test_player(final_shuffled_playlist, song_duration):
    print(       
"""THIS PROGRAM HAS 3 MODES TO PRACTICE FOR THE LISTENING TEST:
1 - BASIC PRACTICE MODE:
• In this mode, the songs will be shuffled and will be played in a random order from anywhere in the song for a minute(60 seconds).
• The user needs to guess the song name and enter the name of the song. 
• If the user's first guess is right, the program will tell you him/her that they are right and move to the next song.
• If the user's first guess is wrong, it will you give him/her another chance to guess the song name. 
• If the user's second is wrong, it will print the song name and continue playing for the entire duration.
• The player will repeat the above steps for all the songs in the playlist and finally, ask the user if they want to practice another time.
• The user can practice the listening as many times as he/she wants by pressing "yes".
• If the user presses "no", it will exit the program.

2 - ADVANCE PRACTICE MODE:
• The user will be asked if they want to play the 1-minute excerpt from the first half or the second half of the song.
• If the user selects the first half, then the songs will be shuffled and will be played in a random order from anywhere in the first half of the song for a minute(60 seconds)
• If the user selects the second half, then the songs will be shuffled and will be played in a random order from anywhere in the second half of the song for a minute(60 seconds)
• The user needs to guess the song name and enter the name of the song. 
• If the user's first guess is right, the program will tell you him/her that they are right and move to the next song.
• If the user's first guess is wrong, it will you give him/her another chance to guess the song name. 
• If the user's second is wrong, it will print the song name and continue playing for the entire duration.
• The player will repeat the above steps for all the songs in the playlist and finally, ask the user if they want to practice another time.
• The user can practice the listening as many times as he/she wants by pressing "yes".
• If the user presses "no", it will exit the program.

3 - MOCK TEST MODE:
• This mode is designed purely for test practice.
• In this mode, the player will play songs as if it is being played in the test. The user will NOT have the option to guess and type the song's name.
• The user will listen to each song and write down the name and artist of the song like they would in a test. Then, they will press enter and the next song will start playing.
• The player will repeat the process for all the songs in the playlist and at the end, it will print the song names according to the order played for the user to verify.
""")
    mode = int(input("Enter the number of your preferred mode: "))
    if mode == 1:
        for my_song in final_shuffled_playlist:
            mp3_path = os.path.join(path, my_song)
            print("Playing:")
            song_length = pygame.mixer.Sound(mp3_path).get_length()
            start_position = random.uniform(0, song_length - song_duration)
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play(start=start_position)
            song = input("Enter Song Name:")
            if song.lower() in my_song.lower():
                print("Yes! You're right")
                pygame.mixer.music.stop()
                if final_shuffled_playlist.index(my_song)!=12:
                    continue
                else:
                    second_practice = input("Would you like to practice another time? Answer in Y/N")
                    if second_practice in "yY":
                        second_shuffle = random.shuffle(final_shuffled_playlist)
                        test_player(final_shuffled_playlist, song_duration)
            else:
                print("Oops, that's wrong! Please try again.")
            song = input("Enter Song Name:")
            if song.lower() in my_song.lower():
                print("Yes! You're right")
                pygame.mixer.music.stop()
                if final_shuffled_playlist.index(my_song)!=12:
                    continue
                else:
                    second_practice = input("Would you like to practice another time? Answer in Y/N")
                    if second_practice in "yY":
                        second_shuffle = random.shuffle(final_shuffled_playlist)
                        test_player(second_shuffle, song_duration)
                    else:
                        break
            else:
                print("Oops, that's wrong")
                print("The name of the song is:", my_song)
            time.sleep(song_duration)
            print(song)
            pygame.mixer.music.stop()
    elif mode == 2:
        personalise_timings = int(input("""
Would you like to practice the first half of the song or the second half?
If it's the first half, enter 1. 
If it's the second half, enter 2: """))
        for my_song in final_shuffled_playlist:
            mp3_path = os.path.join(path, my_song)
            print("Playing:")
            song_length = pygame.mixer.Sound(mp3_path).get_length()
            if personalise_timings == 1:
                start_position = random.uniform(0, ((song_length)/2) - song_duration)
            else:
                start_position = random.uniform((song_length/2), song_length - song_duration)
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play(start=start_position)
            song = input("Enter Song Name:")
            if song.lower() in my_song.lower():
                print("Yes! You're right")
                pygame.mixer.music.stop()
                if final_shuffled_playlist.index(my_song)!=-1:
                    continue
                else:
                    second_practice = input("Would you like to practice another time? Answer in Y/N")
                    if second_practice in "yY":
                        second_shuffle = random.shuffle(final_shuffled_playlist)
                        test_player(final_shuffled_playlist, song_duration)
            else:
                print("Oops, that's wrong! Please try again.")
            song = input("Enter Song Name:")
            if song.lower() in my_song.lower():
                print("Yes! You're right")
                pygame.mixer.music.stop()
                if final_shuffled_playlist.index(my_song)!=-1:
                    continue
                else:
                    second_practice = input("Would you like to practice another time? Answer in Y/N")
                    if second_practice in "yY":
                        second_shuffle = random.shuffle(final_shuffled_playlist)
                        test_player(second_shuffle, song_duration)
                    else:
                        break
            else:
                print("Oops, that's wrong")
                print("The name of the song is:", my_song)
            time.sleep(song_duration)
            print(song)
            pygame.mixer.music.stop()
    elif mode == 3:
        list_of_songs = []
        for index, my_song in enumerate(final_shuffled_playlist):
            mp3_path = os.path.join(path, my_song)
            print(f"Playing song {index+1}: ")
            song_length = pygame.mixer.Sound(mp3_path).get_length()
            start_position = random.uniform(0, song_length - song_duration)
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play(start=start_position)
            var = getkey()
            if var == key.ENTER:
                pygame.mixer.music.stop()
                list_of_songs.append(my_song)
                continue
            time.sleep(song_duration)
            pygame.mixer.music.stop()
            list_of_songs.append(my_song)
        print("---------The list of songs are as follows------------")
        for i in range(1, 13):
            print(i,".", list_of_songs[i-1])
song_duration = 60  # seconds
test_player(final_shuffled_playlist, song_duration)
print("Thankyou for using our player. All the best!")