import tkinter as tk

# ==================================================
# Window (Modernized)
# ==================================================
root = tk.Tk()
root.title("Priority Encoder & Decoder | Pro Edition ✨")
root.geometry("1200x550")
root.resizable(False, False)

# رنگ پس‌زمینه دارک و خفن
BG_COLOR = "#2c3e50"
canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ==================================================
# Logic Variables
# ==================================================
D1 = tk.IntVar()
D2 = tk.IntVar()
D3 = tk.IntVar()
blink = True

# ==================================================
# Drawing Helpers (Polished)
# ==================================================
def draw_switch(x, y, name, state):
    color = "#2ecc71" if state else "#e74c3c"
    shadow = "#27ae60" if state else "#c0392b"
    
    canvas.create_rectangle(x+2, y+2, x+62, y+32, fill=shadow, outline="")
    canvas.create_rectangle(x, y, x+60, y+30, fill=color, outline="white", width=2)
    canvas.create_text(x+30, y+15, text=name, fill="white",
                       font=("Consolas", 12, "bold"))

def draw_led(x, y, state, label):
    color = "#00ff00" if state else "#4a2323"
    glow = "#aaffaa" if state else "#2c3e50"
    
    if state:
        canvas.create_oval(x-2, y-2, x+28, y+28, fill=glow, outline="")
        
    canvas.create_oval(x, y, x+26, y+26, fill=color, outline="white", width=2)
    canvas.create_text(x+13, y+45, text=label, fill="#ecf0f1",
                       font=("Consolas", 10, "bold"))

def wire(x1, y1, x2, y2, active):
    color = "#00e5ff" if active and blink else "#7f8c8d"
    canvas.create_line(x1, y1, x2, y2, width=4, fill=color, capstyle=tk.ROUND)

def draw_or_gate(x, y, label):
    canvas.create_arc(x, y, x+120, y+120,
                      start=270, extent=180, width=3, outline="#f1c40f", fill="#34495e")
    canvas.create_arc(x-60, y, x+60, y+120,
                      start=270, extent=180, width=3, outline="#f1c40f", style=tk.ARC)
    canvas.create_text(x+55, y+60, text=label, fill="#f1c40f",
                       font=("Consolas", 12, "bold"))

# ==================================================
# Truth Table (Polished & Expanded)
# ==================================================
def draw_truth_table(active):
    x, y = 820, 50
    headers = ["D3", "D2", "D1", "Y1", "Y0"]
    # جدول اصلاح‌شده و کامل
    rows = [
        (0,0,0,0,0),
        (0,0,1,0,1),
        (0,1,0,1,0),
        (0,1,1,1,0),
        (1,0,0,1,1),
        (1,0,1,1,1),
        (1,1,0,1,1),
        (1,1,1,1,1),
    ]

    # پنل بک‌گراند جدول (ارتفاعش رو زیاد کردم تا ۸ ردیف جا بشه)
    canvas.create_rectangle(x-10, y-40, x+260, y+290, fill="#34495e", outline="#95a5a6", width=2)

    # عنوان رسمی و جدید
    canvas.create_text(x+125, y-20,
                       text="Priority Encoder Truth Table", fill="#f39c12",
                       font=("Consolas", 12, "bold"))

    for i,h in enumerate(headers):
        canvas.create_rectangle(x+i*50, y,
                                x+(i+1)*50, y+30,
                                fill="#9b59b6", outline="white")
        canvas.create_text(x+i*50+25, y+15, text=h, fill="white", font=("Consolas", 10, "bold"))

    for r,row in enumerate(rows):
        # هایلایت کردن ردیف فعال
        is_active = (row[:3] == active)
        bg = "#e67e22" if is_active else "#ecf0f1"
        fg = "white" if is_active else "black"
        
        for c,val in enumerate(row):
            canvas.create_rectangle(x+c*50, y+30+r*30,
                                    x+(c+1)*50, y+60+r*30,
                                    fill=bg, outline="#7f8c8d")
            canvas.create_text(x+c*50+25,
                               y+45+r*30,
                               text=str(val), fill=fg, font=("Consolas", 10, "bold"))

# ==================================================
# Update Circuit (FIXED LOGIC & WIRING)
# ==================================================
def update():
    global blink
    canvas.delete("all")

    d1, d2, d3 = D1.get(), D2.get(), D3.get()

    # ====== Logic Fix: Priority Encoder ======
    Y1 = d3 or d2
    Y0 = d3 or (d1 and not d2) 
    error = (d1 and d2) or (d1 and d3) or (d2 and d3)

    # ====== Decoder ======
    D0o = int(not Y1 and not Y0)
    D1o = int(not Y1 and Y0)
    D2o = int(Y1 and not Y0)
    D3o = int(Y1 and Y0)

    # ================= INPUTS =================
    canvas.create_text(60, 60, text="► INPUTS", fill="#3498db",
                       font=("Consolas", 14, "bold"))
    draw_switch(40, 100, "D1", d1)
    draw_switch(40, 160, "D2", d2)
    draw_switch(40, 220, "D3", d3)

    # ================= WIRES TO GATES (Fixed Routing) =================
    wire(100, 175, 220, 140, d2)
    wire(100, 235, 220, 180, d3)
    
    wire(100, 115, 220, 280, d1)
    wire(100, 235, 220, 320, d3)

    # ================= OR GATES =================
    draw_or_gate(220, 100, "OR (Y1)")
    draw_or_gate(220, 260, "OR (Y0)")

    # ================= OUTPUT WIRES =================
    wire(340, 160, 420, 160, Y1)
    wire(340, 320, 420, 320, Y0)

    # ================= ENCODER OUTPUT =================
    canvas.create_text(420, 110, text="► ENCODER OUT", fill="#e74c3c",
                       font=("Consolas", 12, "bold"))
    draw_led(430, 145, Y1, "Y1")
    draw_led(430, 305, Y0, "Y0")

    # ================= ERROR LED =================
    draw_led(430, 385, error, "WARN")
    if error:
        canvas.create_text(440, 435, text="Priority Active!", fill="#f1c40f",
                           font=("Consolas", 10, "bold"))

    # ================= DECODER =================
    canvas.create_text(600, 90, text="► DECODER 2→4", fill="#9b59b6",
                       font=("Consolas", 12, "bold"))
    
    canvas.create_rectangle(570, 110, 630, 300, outline="#9b59b6", width=2, dash=(4,4))
    
    draw_led(585, 120, D0o, "D0")
    draw_led(585, 160, D1o, "D1")
    draw_led(585, 200, D2o, "D2")
    draw_led(585, 240, D3o, "D3")

    # ارسال مقادیر به جدول برای هایلایت شدن ردیف درست
    draw_truth_table((d3, d2, d1))

    blink = not blink
    root.after(400, update)

# ==================================================
# Control Panel (Floating Window style)
# ==================================================
control = tk.Frame(root, bg="#34495e", padx=10, pady=10, bd=2, relief="ridge")
control.place(x=30, y=300)

tk.Label(control, text="⚙️ SWITCHBOARD", bg="#34495e", fg="#f1c40f",
         font=("Consolas", 12, "bold")).pack(anchor="w", pady=(0,5))
tk.Checkbutton(control, text="Toggle D1", variable=D1, bg="#34495e", fg="white", 
               selectcolor="#2c3e50", activebackground="#34495e", activeforeground="white", font=("Consolas", 10)).pack(anchor="w")
tk.Checkbutton(control, text="Toggle D2", variable=D2, bg="#34495e", fg="white",
               selectcolor="#2c3e50", activebackground="#34495e", activeforeground="white", font=("Consolas", 10)).pack(anchor="w")
tk.Checkbutton(control, text="Toggle D3", variable=D3, bg="#34495e", fg="white",
               selectcolor="#2c3e50", activebackground="#34495e", activeforeground="white", font=("Consolas", 10)).pack(anchor="w")

update()
root.mainloop()
