# Author: Thomas Preston

from tkinter import *
import json
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab
from PIL import Image, ImageDraw
import io
# pip install pillow

class Paint():
    def main(self):
        self.background_colour = "#303030"
        self.pen_colour = "black"


        # Canvas Window
        self.root_width = 835
        self.root_height = 535

        self.canvas_colour = "white"
        self.eraser_colour = "white"

        self.root = Tk()
        self.root.geometry("{0}x{1}+300+200".format(self.root_width, self.root_height))
        # self.root.geometry("{0}x{1}".format(self.root_width, self.root_height))
        self.root.title("Canvas")
        self.root.resizable(False, False)
        self.root.configure(bg=self.background_colour)

        self.root.iconbitmap('Paintbrush.ico')
        
        # self.canvas = Canvas(self.root, bg = self.canvas_colour, bd = 5, relief = GROOVE, height = self.root_height-35, width = self.root_width-35)
        # self.canvas.place(x = 10, y = 10)

        # self.canvas.bind("<B1-Motion>", self.paint)

        # Tools Window
        self.tools_width = 765
        self.tools_height = 105

        self.tools = Tk()
        self.tools.geometry("{0}x{1}+300+35".format(self.tools_width, self.tools_height))
        self.tools.title("Tools")
        self.tools.resizable(False, False)
        self.tools.configure(bg=self.background_colour)

        self.tools.iconbitmap('Paintbrush.ico')


        self.colour_frame = LabelFrame(self.tools, text = "Colours", font = ('arial', 15), bd = 5, relief = RIDGE, bg = self.background_colour)
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

        self.clear_button = Button(self.tools, text = "Clear", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.clear, width = 12, relief = RIDGE)
        self.clear_button.configure(foreground = "white")
        self.clear_button.place(x = 261, y = 40)

        self.save_button = Button(self.tools, text = "Export", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.save, width = 12, relief = RIDGE)
        self.save_button.configure(foreground = "white")
        self.save_button.place(x = 359, y = 10)

        self.canvas_tool_button = Button(self.tools, text = "Canvas Colour", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.canvas_colour_changer, width = 12, relief = RIDGE)
        self.canvas_tool_button.configure(foreground = "white")
        self.canvas_tool_button.place(x = 359, y = 40)

        self.custom_Colour_Button = Button(self.tools, text = "Custom Brush Colour", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.custom_colour, width = 26, height = 1, relief = RIDGE)
        self.custom_Colour_Button.configure(foreground = "white")
        self.custom_Colour_Button.place(x = 261, y = 70)


        self.pen_size_scale_frame = LabelFrame(self.tools, text = "Size", bd = 5, bg = self.background_colour, font = ('arial', 15), relief = RIDGE)
        self.pen_size_scale_frame.configure(foreground = "white")
        self.pen_size_scale_frame.place(x = 458, y = 0, height = 90, width = 300)

        self.pen_size = Scale(self.pen_size_scale_frame, from_ = 0, to = 100, length = 283, bg = self.background_colour, orient = HORIZONTAL, fg = "white", bd = 0, highlightbackground = self.background_colour)
        self.pen_size.set(50)
        self.pen_size.grid(row = 0, column = 0)


        # Canvas Window
        self.can_width = 200
        self.can_height = 500

        self.can = Tk()
        self.can.geometry("{0}x{1}+1150+200".format(self.can_width, self.can_height))
        self.can.title("Canvas Propeties")
        self.can.resizable(False, False)
        self.can.configure(bg=self.background_colour)

        self.can.iconbitmap('Paintbrush.ico')


        self.canvas_prop_frame = LabelFrame(self.can, text = "Canvas Menu", bd = 5, bg = self.background_colour, font = ('arial', 15), relief = RIDGE)
        self.canvas_prop_frame.configure(foreground = "white")
        self.canvas_prop_frame.place(x = 5, y = 5, height = 490, width = 190)


        self.canvas_width_label = Label(self.canvas_prop_frame, text = "Canvas Width:", bg = self.background_colour)
        self.canvas_width_label.configure(foreground = "white")
        self.canvas_width_label.place(x = 5, y = 5)

        self.canvas_width_entry = Entry(self.canvas_prop_frame, width = 10)
        self.canvas_width_entry.place(x = 100, y = 5)


        self.canvas_height_label = Label(self.canvas_prop_frame, text = "Canvas Height:", bg = self.background_colour)
        self.canvas_height_label.configure(foreground = "white")
        self.canvas_height_label.place(x = 5, y = 35)

        self.canvas_height_entry = Entry(self.canvas_prop_frame, width = 10)
        self.canvas_height_entry.place(x = 100, y = 35)


        self.colour = self.background_colour
        self.canvas_button = Button(self.canvas_prop_frame, text = "Canvas Colour", bd = 4, bg = self.colour, activebackground = self.colour, command = self.canvas_colour_set, width = 22, relief = RIDGE)
        self.canvas_button.configure(foreground = "white")
        self.canvas_button.place(x = 5, y = 65)

        self.submit_button = Button(self.canvas_prop_frame, text = "Create Canvas", bd = 4, bg = self.background_colour, activebackground = self.background_colour, command = self.new_canvas, width = 22, relief = RIDGE)
        self.submit_button.configure(foreground = "white")
        self.submit_button.place(x = 5, y = 95)


        self.canvas_height_label = Label(self.canvas_prop_frame, text = "Recommended: 800x500", bg = self.background_colour)
        self.canvas_height_label.configure(foreground = "white")
        self.canvas_height_label.place(x = 5, y = 125)


        self.exit_button = Button(self.canvas_prop_frame, text = "Quit", command = self.leaving, width = 5, bd = 4, bg = self.background_colour, activebackground = self.background_colour, relief = RIDGE)
        self.exit_button.configure(foreground = "white")
        self.exit_button.place(x = 125, y = 425)

        self.about_button = Button(self.canvas_prop_frame, text = "About", command = self.about, width = 5, bd = 4, bg = self.background_colour, activebackground = self.background_colour, relief = RIDGE)
        self.about_button.configure(foreground = "white")
        self.about_button.place(x = 5, y = 425)
    


        self.root.mainloop()

    def leaving(self):
        answer = messagebox.askquestion("Quitting", "Are you sure?")
        if answer == "yes":
            exit()
    
    def about(self):
        messagebox.showinfo('About','Made by Thomas Preston')
    
    def new_canvas(self):
        self.temproot_height = self.canvas_height_entry.get()
        self.temproot_width = self.canvas_width_entry.get()
        self.root_height = int(self.temproot_height) + 35
        self.root_width = int(self.temproot_width) + 35
        # print(self.root_height, self.root_width)
        self.canvas = Canvas(self.root, bg = self.canvas_colour, bd = 5, relief = GROOVE, height = self.root_height-35, width = self.root_width-35)
        self.canvas.place(x = 10, y = 10)
        self.canvas.configure(bg = self.colour[1])
        self.eraser_colour = self.colour[1]
        self.root.geometry("{0}x{1}+300+200".format(self.root_width, self.root_height))
        self.canvas.bind("<B1-Motion>", self.paint)
        self.submit_button.config(state=DISABLED)


        self.image1 = Image.new("RGB", (self.root_width-35, self.root_height-35), str(self.colour[1]))
        self.draw = ImageDraw.Draw(self.image1)
        

    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)

        self.canvas.create_oval(x1, y1, x2, y2, fill = self.pen_colour, outline = self.pen_colour, width = self.pen_size.get())
        
        width = self.pen_size.get()

        self.draw.ellipse((x1, y1, x1+width, y1+width), fill = self.pen_colour) # width = self.pen_size
        

    def select_colour(self, col):
        self.pen_colour = col

    def eraser(self):
        self.pen_colour = self.eraser_colour

    def canvas_colour_changer(self):
        self.colour = colorchooser.askcolor()
        self.canvas.delete("all")
        self.canvas.configure(bg = self.colour[1])
        self.image1 = Image.new("RGB", (self.root_width-35, self.root_height-35), str(self.colour[1]))
        self.draw = ImageDraw.Draw(self.image1)
        self.eraser_colour = self.colour[1]

        self.canvas_button.configure(bg = self.colour[1], activebackground = self.colour[1])
        self.canvas_tool_button.configure(bg = self.colour[1], activebackground = self.colour[1])
    
    def canvas_colour_set(self):
        self.colour = colorchooser.askcolor()

        self.canvas_button.configure(bg = self.colour[1], activebackground = self.colour[1])
        self.canvas_tool_button.configure(bg = self.colour[1], activebackground = self.colour[1])

    def custom_colour(self):
        colour = colorchooser.askcolor()
        self.pen_colour = colour[1]

    def save(self):
        try:
            # self.root.focus()
            # g = str(self.root.wm_geometry())
            # list_geometry = g.split("+")
            # root_location = list_geometry[1], list_geometry[2]
            # str_wxh = list_geometry[0]
            # list_wxh = str_wxh.split("x")
            # print(root_location)
            # print(list_wxh)
            # # print(int(list_geometry[1])+int(list_wxh[0]), int(list_geometry[2])+int(list_wxh[1]), int(list_geometry[1]), int(list_geometry[2]))
            # # ImageGrab.grab().crop((int(list_geometry[1])+int(list_wxh[0]), int(list_geometry[2])+int(list_wxh[1]), int(list_geometry[1]), int(list_geometry[2]))).save("filename.png")
            # # print(int(list_geometry[1]), int(list_geometry[2]), int(list_geometry[1])+int(list_wxh[0]), int(list_geometry[2])+int(list_wxh[1]))
            # # ImageGrab.grab().crop((int(list_geometry[1]), int(list_geometry[2]), int(list_geometry[1])+int(list_wxh[0]), int(list_geometry[2])+int(list_wxh[1]))).save("filename.png")
            # ImageGrab.grab().crop((int(list_geometry[1]), int(list_geometry[2]), int(list_geometry[1])+500, int(list_geometry[2])+500)).save("filename.png")
            filename = filedialog.asksaveasfilename(defaultextension = ".png")
            self.image1.save(filename)
            messagebox.showinfo('', 'Image saved in ' + str(filename))        
        except Exception as ex:
            messagebox.showerror('', 'Image unable to save - ' + str(ex))

    def test(self):
        # g = str(self.root.wm_geometry()) # 835x535+300+200
        # print(g)
        # list_geometry = g.split("+") # ['835x535', '300', '200']
        # print(list_geometry)
        # root_location = list_geometry[1], list_geometry[2] # ('300', '200')
        # print(root_location)
        # str_wxh = list_geometry[0] # 835x535
        # print(str_wxh)
        # list_wxh = str_wxh.split("x") # ['835', '535']
        # print(list_wxh)
        # ImageGrab.grab().crop((int(list_geometry[1])*0.5, 0, int(list_geometry[1])+300, 300)).save("filename.png")
        # self.retval = self.canvas.postscript(file="test.ps")
        # ps = self.canvas.postscript(colormode='color')
        # img = Image.open(io.BytesIO(ps.encode('utf-8')))
        # img.save('test.jpg')
        # self.canvas.clipboard_append(self.canvas)
        self.image1.save("test.png")

    def clear(self):
        self.canvas.delete("all")
        self.image1 = Image.new("RGB", (self.root_width-35, self.root_height-35), str(self.colour[1]))
        self.draw = ImageDraw.Draw(self.image1)


ui = Paint()
ui.main()