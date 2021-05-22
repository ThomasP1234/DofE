# Author: Thomas Preston

from tkinter import *
import pygame
# pip install pygame
import glob

class Music():
    pygame.mixer.init()

    background_colour = "#303030"

    Library = glob.glob("Music/*")


    window_width = 300
    window_height = 500
    window_x = 200
    window_y = 100

    background_colour = "#303030"
    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Music Player")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)

    def playmusic(self):
        try:
            self.SONG_END = pygame.USEREVENT + 1
            pygame.mixer.music.load(self.Library[0])
            pygame.mixer.music.play()
            self.Library = self.Library[1:] + [self.Library[0]]
        except:
            print('No Music In Folder')

    def playnext(self):
        self.stopmusic()
        try:
            self.Library = self.Library[1:] + [self.Library[0]]
        except:
            pass
        self.playmusic()

    def stopmusic(self):
        pygame.mixer.music.pause()

    def draw(self):
        playButton = Button(self.window, text = "Start", command = self.playmusic)
        playButton.pack()

        pauseButton = Button(self.window, text = "Stop", command = self.stopmusic)
        pauseButton.pack()

        nextButton = Button(self.window, text = "Next", command = self.playnext)
        nextButton.pack()

    def run(self):
        self.main()

        pygame.init()

        self.draw()

        # self.playmusic()

        self.window.mainloop()

runPlayer = Music()
runPlayer.run()


