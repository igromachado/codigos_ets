import tkinter as tk

root = tk.Tk()
root.title("Kernel")
root.bind("<Escape>", lambda e: root.destroy())

SCREEN_W = (root.winfo_screenwidth()//2)
def get_height():
    return SCREEN_H
SCREEN_H = (root.winfo_screenheight()//2)
def get_width():
    return SCREEN_W

BACKGROUND_COLOR = "#f5f5f5"

canvas = tk.Canvas(root, width=SCREEN_W, height=SCREEN_H, bg=BACKGROUND_COLOR)
canvas.pack()



objs = []


def loop(fps=60):
    dt = 1 / fps

    for i in range(len(objs)):
        if(objs[i]['behavior'] != None):
            objs[i]['behavior'](objs[i], [o for o in objs if o['id'] != objs[i]['id']], dt)

        o = objs[i]
        canvas.coords(
            o['id'],
            o['x'] - o['ray'],
            o['y'] - o['ray'],
            o['x'] + o['ray'],
            o['y'] + o['ray'],
        )
        
    root.after(1000//fps, lambda: loop(fps=fps))


def init(entities = [], fps = 60):
    for e in entities:
        obj_id = canvas.create_oval(
            e['pos_xy'][0] - e['ray'], 
            e['pos_xy'][1] - e['ray'], 
            e['pos_xy'][0] + e['ray'], 
            e['pos_xy'][1] + e['ray'], 
            fill=e['color']
        )
        a = e['aceleration']
        vx, vy = e['velocities_xy']

        objs.append(
            {
                'label'       : e['label'],
                'id'          : obj_id,
                'ray'         : e['ray'],
                'velocity_y'  : vy,
                'velocity_x'  : vx,
                'aceleration' : a,
                'x'           : e['pos_xy'][0],
                'y'           : e['pos_xy'][1],
                'behavior'    : e['behavior']
            })

    loop(fps=fps)
    root.mainloop()