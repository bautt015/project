import tkinter as tk
import math

app = tk.Tk()
app.title("Log kalkoelator")
app.geometry("600x400")
app.resizable(False, False)
app.configure(padx=10, pady=1)

tk.Label(app, text="kalkoelator log", font=("Arial", 14, "bold"))\
    .grid(row=0, column=0, columnspan=4, pady=10)


tk.Label(app, text="Masukan nilai X").grid(row=1, column=0)
entry_x = tk.Entry(app)
entry_x.grid(row=1, column=1)

tk.Label(app, text="masukan basis (b)").grid(row=2, column=0)
entry_b = tk.Entry(app)
entry_b.grid(row=2, column=1)

def hitung_log():
    try:
        x = float(entry_x.get())
        if not validasi(x):
            hasil.config(text="Error co: x harus di atas 0")
            return
            
        hasil.config(text=f"log(x) = {math.log10(x):.4f}")
  
    except:
        hasil.config(text="harus masukin angka coo")

def hitung_in():
    try:
        x = float(entry_x.get())
        if not validasi(x):
            hasil.config(text="Error wee: x kudu di atas 0")
            return
        
        hasil.config(text=f"in(x) = {math.log(x):.4f}")
    
    except:
        hasil.config(text="harus masukin angka coo")

def hitung_log_b():
    try:
        x = float(entry_x.get())
        b = float(entry_b.get())

        if not validasi(x, b):
            hasil.config(text="Error bang: x harus di atas 0, b juga sama")
            return
        
        hasil.config(text=f"log{b}(x) = {math.log(x, b):.4f}")
    
    except:
        hasil.config(text="harus masukin angka coo")

def clear():
    entry_x.delete(0, tk.END)
    hasil.config(text="Hasil:")

def validasi(x, b=None):
    if x <= 0:
        return False
    if b is not None and (b <= 0 or b == 1):
        return False
    return True

tk.Button(app, text="Hitung log(x)", command=hitung_log).grid(row=3,column=0,)
tk.Button(app, text="Hitung ln(x)", command=hitung_in).grid(row=3, column=1,)
tk.Button(app, text="Hitung log b(x)", command=hitung_log_b).grid(row=3, column=2,)
tk.Button(app, text="bersihkan", command=clear).grid(row=3, column=5,)
hasil =tk.Label(app, text="Hasil:")


hasil.grid(pady=10, row=5, column=1)

app.mainloop()