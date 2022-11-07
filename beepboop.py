from pygame import mixer
import time

def playSound(path):
    mixer.init()
    explosion_sound = mixer.Sound(path)
    explosion_sound.play()
    time.sleep(0.1)

def toBinary(string):
    binaryString = ""
    for character in string:
        binaryString += bin(ord(character))[2:]
    return binaryString


# string = input("Enter a string: ")
string = "this is a test file for beep boop program. let see or we should say here how it sounds."

for bit in toBinary(string):
    if bit == "1":
        playSound("music/beep.ogg")
    elif bit == "0":
        playSound("music/boop.ogg")