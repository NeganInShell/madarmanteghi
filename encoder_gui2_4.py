import tkinter as tk

# ==================================================
# Window (Modernized Decoder)
# ==================================================
root = tk.Tk()
root.title("2-to-4 Decoder | Pro Edition 🚀")
root.geometry("1000x500")
root.resizable(False, False)

# رنگ پس‌زمینه دارک و خفن
BG_COLOR = "#1a252f"
canvas = tk.Canvas(root, bg=BG_COLOR, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ==================================================
# Logic Variables
# ==================================================
A = tk.IntVar() # MSB
B = tk.IntVar() # LSB
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
    glow = "#aaffaa" if state else "#1a252f"
    
    if state:
        # افکت درخشش نئونی
        canvas.create_oval(x-4, y-4, x+30, y+30, fill=glow, outline="")
        
    canvas.create_oval(x, y, x+26, y+26, fill=color, outline="white", width=2)
    canvas.create_text(x+45, y+13, text=label, fill="#ecf0f1",
                       font=("Consolas", 12, "bold"))

def wire(x1, y1, x2, y2, active):
    color = "#00e5ff" if active and blink else "#7f8c8d"
    canvas.create_line(x1, y1, x2, y2, width=4, fill=color, capstyle=tk.ROUND)

def draw_decoder_chip(x, y):
    # رسم تراشه دیکودر (مغز متفکر مدار!)
    canvas.create_rectangle(x, y, x+120, y+200, fill="#2c3e50", outline="#3498db", width=3)
    canvas.create_text(x+60, y+100, text="2-to-4\nDECODER", fill="#3498db",
                       font=("Consolas", 14, "bold"), justify="center")

# ==================================================
# Truth Table (Live & Interactive)
# ==================================================
def draw_truth_table(active_a, active_b):
    x, y = 650, 100
    headers = ["A", "B", "D0", "D1", "D2", "D3"]
    # جدول درستی دیکودر 2 به 4
    rows = [
        (0, 0, 1, 0, 0, 0),
        (0, 1, 0, 1, 0, 0),
        (1, 0, 0, 0, 1, 0),
        (1, 1, 0, 0, 0, 1),
    ]

    # پنل بک‌گراند جدول
    canvas.create_rectangle(x-10, y-40, x+310, y+170, fill="#2c3e50", outline="#95a5a6", width=2)

    # عنوان
    canvas.create_text(x+150, y-20,
                       text="Live Truth Table", fill="#f39c12",
                       font=("Consolas", 14, "bold"))

    # هدرها
    for i, h in enumerate(headers):
        canvas.create_rectangle(x+i*50, y,
                                x+(i+1)*50, y+30,
                                fill="#9b59b6", outline="white")
        canvas.create_text(x+i*50+25, y+15, text=h, fill="white", font=("Consolas", 10, "bold"))

    # ردیف‌ها
    for r, row in enumerate(rows):
        is_active = (row[0] == active_a and row[1] == active_b)
        bg = "#e67e22" if is_active else "#ecf0f1"
        fg = "white" if is_active else "black"
        
        for c, val in enumerate(row):
            canvas.create_rectangle(x+c*50, y+30+r*30,
                                    x+(c+1)*50, y+60+r*30,
                                    fill=bg, outline="#7f8c8d")
            canvas.create_text(x+c*50+25,
                               y+45+r*30,
                               text=str(val), fill=fg, font=("Consolas", 12, "bold"))

# ==================================================
# Core Engine
# ==================================================
def update():
    global blink
    canvas.delete("all")

    a_val = A.get()
    b_val = B.get()

    # ====== Decoder Logic ======
    D0_out = int(not a_val and not b_val)
    D1_out = int(not a_val and b_val)
    D2_out = int(a_val and not b_val)
    D3_out = int(a_val and b_val)

    # ================= INPUTS =================
    canvas.create_text(70, 110, text="► INPUTS", fill="#f1c40f",
                       font=("Consolas", 14, "bold"))
    draw_switch(40, 150, "A", a_val)
    draw_switch(40, 230, "B", b_val)

    # ================= WIRES TO CHIP =================
    wire(100, 165, 250, 165, a_val)
    wire(100, 245, 250, 245, b_val)

    # ================= THE CHIP =================
    draw_decoder_chip(250, 100)

    # ================= OUTPUT WIRES =================
    wire(370, 125, 450, 125, D0_out)
    wire(370, 175, 450, 175, D1_out)
    wire(370, 225, 450, 225, D2_out)
    wire(370, 275, 450, 275, D3_out)

    # ================= LEDS (OUTPUTS) =================
    canvas.create_text(480, 80, text="► OUTPUTS", fill="#2ecc71",
                       font=("Consolas", 14, "bold"))
    draw_led(450, 112, D0_out, "D0")
    draw_led(450, 162, D1_out, "D1")
    draw_led(450, 212, D2_out, "D2")
    draw_led(450, 262, D3_out, "D3")

    # ================= TRUTH TABLE =================
    draw_truth_table(a_val, b_val)

    blink = not blink
    root.after(400, update)

# ==================================================
# Control Panel
# ==================================================
control = tk.Frame(root, bg="#2c3e50", padx=15, pady=15, bd=2, relief="ridge")
control.place(x=40, y=320)

tk.Label(control, text="⚙️ SWITCHBOARD", bg="#2c3e50", fg="#3498db",
         font=("Consolas", 12, "bold")).pack(anchor="w", pady=(0,10))

tk.Checkbutton(control, text="Toggle A (MSB)", variable=A, bg="#2c3e50", fg="white", 
               selectcolor="#1a252f", activebackground="#2c3e50", activeforeground="white", 
               font=("Consolas", 11)).pack(anchor="w", pady=2)

tk.Checkbutton(control, text="Toggle B (LSB)", variable=B, bg="#2c3e50", fg="white",
               selectcolor="#1a252f", activebackground="#2c3e50", activeforeground="white", 
               font=("Consolas", 11)).pack(anchor="w", pady=2)

update()
root.mainloop()
