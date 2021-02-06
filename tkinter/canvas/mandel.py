from tkinter import *
from tkinter import ttk

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


canvas_width  = 500
canvas_height = 400

xaVar = DoubleVar(value=-2)
yaVar = DoubleVar(value=-1.27)
xbVar = DoubleVar(value=1)
ybVar = DoubleVar(value=1.27)

def isInMandelSet(p):
    z = 0
    for i in range(20):
        z = z*z + p
    if abs(z) < 2:
        return True
    else:
        return False

def mandelIter(p):
    maxIter = 256
    z = 0
    for i in range(maxIter):
        z = z*z + p
        if abs(z) >= 2:
            return i
    return maxIter

def isInMandelSet2(x, y):
    an, bn = 0, 0
    for i in range(20):
        an, bn = an*an -bn*bn + x, 2*an*bn + y
        if an*an+bn*bn > 4:
            return False
    return True
    
colors = [ '#%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(256)]
colors.append('#000000')

'''
Canvas for the Mandelbrot set
'''
class MandelCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        print(self.cget('width'), self.cget('height'))
        self['borderwidth'] = 2
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        self.lastRect = 0


    '''
    draw a dot
    '''
    def dot(self, x, y, color='#000000'):
        self.create_line(x, y, x+1, y, fill=color)
        
    '''
    draw the mandelbrot set
    '''
    def do_draw(self, withColors=False):
        self.xa =  xaVar.get(); self.ya = yaVar.get()
        self.xb =  xbVar.get(); self.yb = ybVar.get()
        print('draw mandelbrot set for xa {}, ya {}, xb {}, yb {}'.format(self.xa, self.ya, self.xb, self.yb))
        for px in range(canvas_width):
            for py in range(canvas_height):
                xm, ym = self.to_wc(px, py)
                if withColors:
                    nIter = mandelIter(complex(xm, ym))
                    self.dot(px, py, colors[nIter])                    
                else:
                    if isInMandelSet2(xm, ym):
                        self.dot(px, py)
                        
    def to_wc(self, px, py):
        xm = self.xa + (self.xb - self.xa)*px/canvas_width
        ym = self.yb - (self.yb - self.ya)*py/canvas_height
        return xm, ym
        
    def save_posn(self, event):
        self.lastx1, self.lasty1 = event.x, event.y
        print(self.to_wc(self.lastx1, self.lasty1))

    def add_line(self, event):
        rect = self.create_rectangle(self.lastx1, self.lasty1, event.x, event.y, outline='white')
        if self.lastRect != 0:
            self.delete(self.lastRect)
        self.lastRect = rect    
        self.lastx2, self.lasty2 = event.x, event.y        

    def redraw(self):
        print("redraw...")
        self.delete("all")
        xa, ya = self.to_wc(self.lastx1, self.lasty1)
        xb, yb = self.to_wc(self.lastx2, self.lasty2)
        xaVar.set(xa); yaVar.set(ya)
        xbVar.set(xb); ybVar.set(yb)
        self.do_draw(True)



content = ttk.Frame(root)
content.grid(column=0, row=0)

# Canvas
canvas = MandelCanvas(content, width=canvas_width, height=canvas_height)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# controls


controlsFrame = ttk.Frame(content, padding=(3))
controlsFrame.grid(column=1, row=0, sticky=(N, W, E, S))

label = ttk.Label(controlsFrame, text="Mandelbrot Set")
label.grid(column=0, row=0, sticky=(N, W, E, S))

label = ttk.Label(controlsFrame, text="xa")
label.grid(column=0, row=1)
xaEntry = ttk.Entry(controlsFrame, textvariable=xaVar)
xaEntry.grid(column=1, row=1)
label = ttk.Label(controlsFrame, text="ya")
label.grid(column=0, row=2)
yaEntry = ttk.Entry(controlsFrame, textvariable=yaVar)
yaEntry.grid(column=1, row=2)

label = ttk.Label(controlsFrame, text="xb")
label.grid(column=0, row=3)
xbEntry = ttk.Entry(controlsFrame, textvariable=xbVar)
xbEntry.grid(column=1, row=3)
label = ttk.Label(controlsFrame, text="yb")
label.grid(column=0, row=4)
ybEntry = ttk.Entry(controlsFrame, textvariable=ybVar)
ybEntry.grid(column=1, row=4)


# buttons
def onBtnTestClick():
    print("btn test clicked");
    canvas.redraw()

buttonsFrame = ttk.Frame(content, padding=(3, 5))
buttonsFrame.grid(row=1, column=0, columnspan=2, sticky=(E))
btnTest = ttk.Button(buttonsFrame, text="Test", command=onBtnTestClick)
btnTest.grid()

# initial draw
canvas.do_draw(False)


root.mainloop()


