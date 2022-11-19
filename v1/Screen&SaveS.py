import tkinter as tk
import pyautogui as pag
import os

try:
    os.mkdir('%Screenshots%')
except Exception as e:
    pass

master = tk.Tk()
master.resizable(False,False)
master.title('Screen & Save')
master.geometry("200x140")
master.configure(bg='black')
master.iconbitmap('image/radioactive.ico')

font_specs = ("Algerian", 15)
fontBut = ("Arial",10)

def ads():
    leb = tk.Label(text="Screenshot saved in\n%Screenshots% directory", font=fontBut, fg='white',bg='black')
    leb.pack(pady=5)
    leb.after(3000, lambda: leb.destroy())

def Screenshot():
    mys = pag.screenshot()
    dir_list = os.listdir(r'%Screenshots%')
    i = len(dir_list)
    mys.save(r'%Screenshots%\Screenshot_'+str(i)+'.png')
    ads()

lab = tk.Label(text="Screen & Save", font=font_specs, fg='white',bg='black').pack(pady=5)
scr = tk.Button(text="Take a Screenshot", font=fontBut, fg='grey',bg='black', command=Screenshot).pack(pady=5)

if __name__ == "__main__":
    master.mainloop()
