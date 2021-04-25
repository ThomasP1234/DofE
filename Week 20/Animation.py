# Author: Thomas Preston

from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import json

'''
Todo
- Add scroll bar to slide deck
- Add check box for loop of animation
- Add shadow of previous frame
- Add save and load
'''

class Animation():
    def main(self):
        # Variables for all
        self.background_colour = "#303030"
        self.images = []
        self.pen_colour = "black"
        self.eraser_colour = "white"
        # Root
        self.root_width = 800
        self.root_height = 275
        self.root_height2 = self.root_height+75

        self.root = Tk()
        self.root.geometry("{0}x{1}+20+150".format(self.root_width, self.root_height2))
        self.root.title("Animation Window")
        self.root.resizable(False, False)
        self.root.configure(bg=self.background_colour)

        self.root.iconbitmap('Play.ico')

        self.create_design_tool()
        # self.c1 = Canvas(self.root, bg = "white", bd = 5, relief = GROOVE, height = 200, width = 300)
        # self.c1.place(x = 10, y = 10)


        self.b1 = Button(self.root, text = "Next Frame", command = self.next_frame, bd = 4, bg = self.background_colour, activebackground = self.background_colour, height = 1, relief = RIDGE)
        self.b1.configure(foreground = "white")
        self.b1.place(x = 10, y = 230)

        self.b2 = Button(self.root, text = "Play All Frames", command = self.init_slideshow, bd = 4, bg = self.background_colour, activebackground = self.background_colour, height = 1, relief = RIDGE)
        self.b2.configure(foreground = "white")
        self.b2.place(x = 90, y = 230)

        self.b3 = Button(self.root, text = "Export", command = self.export, bd = 4, bg = self.background_colour, activebackground = self.background_colour, height = 1, relief = RIDGE)
        self.b3.configure(foreground = "white")
        self.b3.place(x = 190, y = 230)

        self.lbl2 = Label(self.root, text = "Project Export Name:", bd = 4, bg = self.background_colour, foreground = "white")
        self.lbl2.place(x = 240, y = 230)

        self.projectname = Entry(self.root, bd = 4, bg = self.background_colour, relief = RIDGE)
        self.projectname.configure(foreground = "white")
        self.projectname.place(x = 360 , y = 230)

        self.b4 = Button(self.root, text = "Quit", command = exit, bd = 4, bg = self.background_colour, activebackground = self.background_colour, height = 1, relief = RIDGE)
        self.b4.configure(foreground = "white")
        self.b4.place(x = 750, y = 310)

        self.playback_scale_frame = LabelFrame(self.root, text = "Playback: Time Between Frames (Milliseconds)", bd = 5, bg = self.background_colour, font = ('arial', 10), relief = RIDGE)
        self.playback_scale_frame.configure(foreground = "white")
        self.playback_scale_frame.place(x = 10, y = 260, height = 80, width = 300)

        self.playback = Scale(self.playback_scale_frame, from_ = 20, to = 1000, length = 283, bg = self.background_colour, orient = HORIZONTAL, fg = "white", bd = 0, highlightbackground = self.background_colour)
        self.playback.set(500)
        self.playback.grid(row = 0, column = 0)

        # self.b3 = Button(self.root, text = "Play All Frames", command = self.play)

        # Secondary Window(s)
        self.test_width = 1100
        self.test_height = 75

        self.test = Toplevel(self.root)
        self.test.geometry("{0}x{1}+20+10".format(self.test_width, self.test_height))
        self.test.title("Frames")
        # self.test.resizable(False, False)
        self.test.configure(bg=self.background_colour)

        self.test.iconbitmap('Play.ico')

        self.b1 = Button(self.test, text = "Show Frames", command = self.display_all_frames)
        # self.b1.grid(row = 0, column = 0)

        self.tools_width = 660
        self.tools_height = 105

        self.tools = Tk()
        self.tools.geometry("{0}x{1}+20+565".format(self.tools_width, self.tools_height))
        self.tools.title("Pen Config")
        self.tools.resizable(False, False)
        self.tools.configure(bg=self.background_colour)

        self.tools.iconbitmap('Paintbrush.ico')

        self.colour_frame = LabelFrame(self.tools, text = "Colour Pallet", font = ('arial', 15), bd = 5, relief = RIDGE, bg = self.background_colour)
        self.colour_frame.configure(foreground = "white")
        self.colour_frame.place(x = 0, y = 0, width = 260, height = 90)

        with open('Colours.json', 'r') as myfile:
            array = myfile.read()

        data  = json.loads(array)
        colours = data['Colours']

        i=j=0
        for colour in colours:
            Button(self.colour_frame, bg = colour, activebackground = colour, bd = 2, relief = RIDGE, width = 3, command = lambda col = colour: self.select_colour(col)).grid(row = i, column = j)
            i += 1

            if i == 2:
                i = 0
                j += 1

        self.eraser_button = Button(self.tools, text = "Eraser", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.eraser, width = 12, relief = RIDGE)
        self.eraser_button.configure(foreground = "white")
        self.eraser_button.place(x = 261, y = 10)

        self.pen_size_scale_frame = LabelFrame(self.tools, text = "Brush Size", bd = 5, bg = self.background_colour, font = ('arial', 15), relief = RIDGE)
        self.pen_size_scale_frame.configure(foreground = "white")
        self.pen_size_scale_frame.place(x = 359, y = 0, height = 90, width = 300)

        self.pen_size = Scale(self.pen_size_scale_frame, from_ = 0, to = 100, length = 283, bg = self.background_colour, orient = HORIZONTAL, fg = "white", bd = 0, highlightbackground = self.background_colour)
        self.pen_size.set(10)
        self.pen_size.grid(row = 0, column = 0)

        # Run
        self.root.mainloop()

    # Methods
    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)
        
        width = self.pen_size.get()

        # self.c1.create_oval(x1, y1, x2, y2, fill = "gray", outline = "gray", width = 10)
        self.c2.create_oval(x1, y1, x2, y2, fill = self.pen_colour, outline = self.pen_colour, width = width)

        # self.draw1.ellipse((x1, y1, x1+width, y1+width), fill = "gray")
        self.draw2.ellipse((x1, y1, x1+width, y1+width), fill = self.pen_colour)
        
    def next_frame(self):
        self.images.append(self.image2)
        self.create_design_tool()
        self.display_all_frames()

    def create_design_tool(self):
        # self.c1 = Canvas(self.root, bg = "white", bd = 5, relief = GROOVE, height = 200, width = 300)
        # self.c1.place(x = 10, y = 10)

        self.c2 = Canvas(self.root, bg = self.eraser_colour, bd = 5, relief = GROOVE, height = 200, width = 300)
        if len(self.images) > 0:
            self.c2.create_image(300, 200, image=self.preview_image())# self.images[len(self.images)-1]
        # self.c2.place(x = 10, y = 230)
        self.c2.place(x = 10, y = 10)
        # self.c2.configure(alpha = 0.5)

        # self.image1 = Image.new("RGB", (300, 200), "white")
        # self.draw1 = ImageDraw.Draw(self.image1)

        self.image2 = Image.new("RGB", (300, 200), self.eraser_colour)
        self.draw2 = ImageDraw.Draw(self.image2)


        self.c2.bind("<B1-Motion>", self.paint)

    def display_all_frames(self):
        column = 1
        for img in self.images:
            # filename = "Frames\\frame"+str(row)+".jpeg"
            # img.save(filename)
            # load = Image.open(filename)
            # load = load.resize((150, 100), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            img = img.resize((75, 50), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(img)
            lbl = Label(self.test)#, image=render)
            lbl.configure(image = render)
            lbl.image = render
            lbl.grid(row = 0, column = column)
            column += 1

    def preview_image(self):
            # filename = "Frames\\preview.jpeg"
            # self.image1.save(filename)
            # load = Image.open(filename)
            # load = load.resize((150, 100), Image.ANTIALIAS)
            # render = ImageTk.PhotoImage(load)
            # return render
            pass
    
    def init_slideshow(self):
        if len(self.images) < 1:
            return     
        self.lbl = Label(self.root)
        # for img in self.images:
            # render = ImageTk.PhotoImage(img)
            # lbl.configure(image = render)
            # lbl.image = render
            # lbl.place(x = 400, y = 200)
            # self.root.after(1000, )
            # # break
        self.currentframe = 0
        self.slideshow()

    def slideshow(self):
        img = self.images[self.currentframe]
        img = img.resize((300, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        self.lbl.configure(image = render)
        self.lbl.image = render
        self.lbl.place(x = 350, y = 10)
        self.currentframe += 1
        if self.currentframe < len(self.images):
            self.root.after(self.playback.get(), self.slideshow)

    def export(self):
        row = 1
        for img in self.images:
            filename = "Frames\\"+self.projectname.get()+"_Frame"+str(row)+".png"
            img.save(filename)
            row += 1

    def select_colour(self, col):
        self.pen_colour = col

    def eraser(self):
        self.pen_colour = self.eraser_colour

    def play(self):
        pass

ui = Animation()
ui.main()