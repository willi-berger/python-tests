from tkinter import *
from tkinter import ttk

class Sketchpad(Canvas):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        self.lastRect = 0
        
    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        if self.lastRect != 0:
            self.delete(self.lastRect)
        self.lastRect = self.create_rectangle(self.lastx, self.lasty,event.x, event.y)
        
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketch = Sketchpad(root)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))


id = sketch.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
sketch.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = sketch.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
sketch.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = sketch.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
sketch.tag_bind(id, "<Button-1>", lambda x: setColor("black"))


sketch.create_rectangle(40, 10, 500, 80, fill="yellow")


root.mainloop()
