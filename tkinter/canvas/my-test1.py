from tkinter import *
from tkinter import ttk

canvas_width = 500
canvas_height = 400


xa = -2; ya = -1.27
xb =  1; yb =  1.27

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        print(self.cget('width'))
        self.do_draw()


    def dot(self, x, y):
        self.create_line(x, y, x+10, y+10, fill='#ff0000')
        

    def do_draw(self):
        for px in range(canvas_width):
            for py in range canvas_height:
                xm = xa + (xb-xa)*px/canvas_width
                ym = ya + (yb-ya)*py/canvas_height
                
        self.dot(300, 50)
        
        
        
    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)




root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketch = Sketchpad(root, width=canvas_width, height=canvas_height)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()
