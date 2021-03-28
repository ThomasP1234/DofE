# Author: Thomas Preston

from tkinter import *
from PIL import Image, ImageDraw, ImageTk


class Animation():
    def main(self):
        # Variables for all
        self.background_colour = "#303030"
        self.images = []
        # Root
        self.root_width = 800
        self.root_height = 500
        self.root_height2 = self.root_height+75

        self.root = Tk()
        self.root.geometry("{0}x{1}+280+175".format(self.root_width, self.root_height2))
        self.root.title("Animation Window")
        self.root.resizable(False, False)
        self.root.configure(bg=self.background_colour)

        self.root.iconbitmap('Play.ico')

        self.create_design_tool()

        self.b1 = Button(self.root, text = "Next Frame", command = self.next_frame)
        self.b1.place(x = 600, y = 10)

        # Secondary Window(s)
        self.test_width = 300
        self.test_height = 575

        self.test = Toplevel(self.root)
        self.test.geometry("{0}x{1}+1100+175".format(self.test_width, self.test_height))
        self.test.title("2nd Window")
        # self.test.resizable(False, False)
        self.test.configure(bg=self.background_colour)

        self.test.iconbitmap('Play.ico')

        self.b1 = Button(self.test, text = "Show Frames", command = self.display_all_frames)
        self.b1.grid(row = 0, column = 0)

        # Run
        self.root.mainloop()

    # Methods
    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)

        self.c1.create_oval(x1, y1, x2, y2, fill = "gray", outline = "gray", width = 10)
        self.c2.create_oval(x1, y1, x2, y2, fill = "black", outline = "black", width = 10)

        width = 10

        self.draw1.ellipse((x1, y1, x1+width, y1+width), fill = "gray")
        self.draw2.ellipse((x1, y1, x1+width, y1+width), fill = "black")
        
    def next_frame(self):
        self.images.append(self.image2)
        self.create_design_tool()

    def create_design_tool(self):
        self.c1 = Canvas(self.root, bg = "white", bd = 5, relief = GROOVE, height = 200, width = 300)
        self.c1.place(x = 10, y = 10)

        self.c2 = Canvas(self.root, bg = "white", bd = 5, relief = GROOVE, height = 200, width = 300)
        if len(self.images) > 0:
            self.c2.create_image(300, 200, image=self.preview_image())# self.images[len(self.images)-1]
        self.c2.place(x = 10, y = 230)

        self.image1 = Image.new("RGB", (300, 200), "white")
        self.draw1 = ImageDraw.Draw(self.image1)

        self.image2 = Image.new("RGB", (300, 200), "white")
        self.draw2 = ImageDraw.Draw(self.image2)


        self.c2.bind("<B1-Motion>", self.paint)

    def display_all_frames(self):
        row = 1
        for img in self.images:
            filename = "frame"+str(row)+".jpeg"
            img.save(filename)
            load = Image.open(filename)
            load = load.resize((150, 100), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self.test, image=render)
            img.image = render
            img.grid(row = row, column = 0)
            row += 1

    def preview_image(self):
            filename = "preview.jpeg"
            self.image1.save(filename)
            load = Image.open(filename)
            load = load.resize((150, 100), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            return render

ui = Animation()
ui.main()