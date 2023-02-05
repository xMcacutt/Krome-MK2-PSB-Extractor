
from struct import pack, unpack
import sys
import os

class Sound:
    def __init__(self, name, size):
        self.name = name
        self.size = size

if len(sys.argv) != 3:
    print("incorrect arguments")
else:
    with open(sys.argv[1], "r+b") as f:
        f.seek(4, 0)
        fileCount = unpack("I", f.read(4))[0]
        print("File Count: " + str(fileCount))
        f.seek(16, 0)
        sounds = []
        
        count = 0
        while(count < fileCount):
            fileName = unpack("32s", f.read(32))[0]
            f.seek(4, 1)
            fileSize = unpack("I", f.read(4))[0]
            fileName = fileName.split(b"\x00")[0].decode()
            print(fileName + " " + str(fileSize) + "bytes")
            count += 1
            f.seek(24, 1)
            sound = Sound(fileName, fileSize)
            sounds.append(sound)
        for sound in sounds:
            output = open(sys.argv[2] + "\\" + str(sound.name) + ".raw", "w+b")
            f.seek(38, 1)
            data = f.read(sound.size)
            output.write(data)
            print("File written: " + str(sound.name) + ".raw")
        print("Done")


            