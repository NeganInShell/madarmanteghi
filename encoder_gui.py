import tkinter as tk

# ==================================================
# Window
# ==================================================
root = tk.Tk()
root.title("Priority Encoder & Decoder | Logic Simulator")
root.geometry("1200x550")
root.resizable(False, False)

canvas = tk.Canvas(root, bg="#ecf0f1")
canvas.pack(fill="both", expand=True)

# ==================================================
# Logic Variables
# ==================================================
D1 = tk.IntVar()
D2 = tk.IntVar()
D3 = tk.IntVar()
blink = True

# ==================================================
# Drawing Helpers
# ==================================================
def draw_switch(x, y, name, state):
    color = "#2ecc71" if state else "#e74c3c"
    canvas.create_rectangle(x, y, x+60, y+30, fill=color)
    canvas.create_text(x+30, y+15, text=name, fill="white",
                       font=("Arial", 10, "bold"))

def draw_led(x, y, state, label):
    color = "lime" if state else "#7f0000"
    canvas.create_oval(x, y, x+26, y+26, fill=color)
    canvas.create_text(x+13, y+40, text=label,
                       font=("Arial", 9, "bold"))

def wire(x1, y1, x2, y2, active):
    color = "green" if active and blink else "black"
    canvas.create_line(x1, y1, x2, y2, width=3, fill=color)

def draw_or_gate(x, y, label):
    canvas.create_arc(x, y, x+120, y+120,
                      start=270, extent=180, width=2)
    canvas.create_arc(x-60, y, x+60, y+120,
                      start=270, extent=180, width=2)
    canvas.create_text(x+60, y+60, text=label,
                       font=("Arial", 11, "bold"))

# ==================================================
# Truth Table
# ==================================================
def draw_truth_table(active):
    x, y = 780, 40
    headers = ["D3", "D2", "D1", "Y1", "Y0"]
    rows = [
        (0,0,0,0,0),
        (0,0,1,0,1),
        (0,1,0,1,0),
        (1,0,0,1,1)
    ]

    canvas.create_text(x+125, y-20,
                       text="Valid Truth Table",
                       font=("Arial", 11, "bold"))

    for i,h in enumerate(headers):
        canvas.create_rectangle(x+i*50, y,
                                x+(i+1)*50, y+30,
                                fill="#bdc3c7")
        canvas.create_text(x+i*50+25, y+15, text=h)

    for r,row in enumerate(rows):
        bg = "#f1c40f" if row[:3] == active else "white"
        for c,val in enumerate(row):
            canvas.create_rectangle(x+c*50, y+30+r*30,
                                    x+(c+1)*50, y+60+r*30,
                                    fill=bg)
            canvas.create_text(x+c*50+25,
                               y+45+r*30,
                               text=str(val))

# ==================================================
# Update Circuit
# ==================================================
def update():
    global blink
    canvas.delete("all")

    d1, d2, d3 = D1.get(), D2.get(), D3.get()
    active_inputs = d1 + d2 + d3

    # Priority Encoder Logic
    Y1 = d3 or d2
    Y0 = d3 or d1
    error = active_inputs > 1

    # Decoder
    D0o = int(not Y1 and not Y0)
    D1o = int(not Y1 and Y0)
    D2o = int(Y1 and not Y0)
    D3o = int(Y1 and Y0)

    # ================= INPUTS =================
    canvas.create_text(60,60,text="INPUTS",
                       font=("Arial",11,"bold"))
    draw_switch(40, 100, "D1", d1)
    draw_switch(40, 160, "D2", d2)
    draw_switch(40, 220, "D3", d3)

    # ================= WIRES TO GATES =================
    wire(100,115,220,140,d1)
    wire(100,175,220,160,d2)
    wire(100,235,220,180,d3)
    wire(100,235,220,320,d3)

    # ================= OR GATES =================
    draw_or_gate(220,100,"OR")
    draw_or_gate(220,260,"OR")

    # ================= OUTPUT WIRES =================
    wire(340,160,420,160,Y1)
    wire(340,320,420,320,Y0)

    # ================= ENCODER OUTPUT =================
    canvas.create_text(420,120,
                       text="Encoder Output",
                       font=("Arial",10,"bold"))
    draw_led(430,145,Y1,"Y1")
    draw_led(430,305,Y0,"Y0")

    # ================= ERROR LED =================
    draw_led(430,365,error,"ERROR")
    canvas.create_text(430,400,
                       text="Multiple Inputs!",
                       font=("Arial",9,"bold"))

    # ================= DECODER =================
    canvas.create_text(560,90,
                       text="Decoder 2→4",
                       font=("Arial",10,"bold"))
    draw_led(560,120,D0o,"D0")
    draw_led(560,160,D1o,"D1")
    draw_led(560,200,D2o,"D2")
    draw_led(560,240,D3o,"D3")

    draw_truth_table((d3,d2,d1))

    blink = not blink
    root.after(400, update)

# ==================================================
# Controls
# ==================================================
control = tk.Frame(root)
control.place(x=40, y=10)

tk.Label(control,
         text="INPUT SWITCHES",
         font=("Arial", 12, "bold")).pack(anchor="w")
tk.Checkbutton(control, text="D1", variable=D1).pack(anchor="w")
tk.Checkbutton(control, text="D2", variable=D2).pack(anchor="w")
tk.Checkbutton(control, text="D3", variable=D3).pack(anchor="w")

update()
root.mainloop()
