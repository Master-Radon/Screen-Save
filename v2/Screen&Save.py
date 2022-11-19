import tkinter as tk
import pyautogui as pag
import cv2
import numpy as np
import os

try:
    os.mkdir('%Records%')
except Exception as e:
    pass
try:
    os.mkdir('%Screenshots%')
except Exception as e:
    pass

master = tk.Tk()
master.resizable(False,False)
master.title('Screen & Save')
master.geometry("200x180")
master.configure(bg='black')
master.iconbitmap('image/radioactive.ico')

font_specs = ("Algerian", 15)
fontBut = ("Arial",10)
dat = tk.Entry(width=10)

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

def advice():
    re = tk.Label(text='Video Completed!',font=fontBut,bg='black',fg='white')
    re.pack(pady=5)
    re.after(3000, lambda: re.destroy())

def Screenvideo():
    dir_list = os.listdir(r'%Records%')
    i = len(dir_list)
    path = r'%Records%\ScreenRecord_'+str(i)+'.avi'
    sec = dat.get()
    er = tk.Label(text="ON AIR!",font=fontBut,bg='black',fg='white')
    er.pack(pady=5)
    sa = 1
    try:
        record_seconds = int(sec)
        er.after(record_seconds, lambda: er.destroy())
        sa = 0
    except Exception as e:
        er['text']='Error: enter in the TextField a \nduration of the video (in seconds)'
        er.pack(pady=5)
        er.after(3000, lambda: er.destroy())
        sa = 90
    if sa == 0:
        SCREEN_SIZE = tuple(pag.size())
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = 12.0
        out = cv2.VideoWriter(path, fourcc, fps, (SCREEN_SIZE))
        for i in range(int(record_seconds * fps)):
            img = pag.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.imshow("screenshot", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        cv2.destroyAllWindows()
        out.release()
        img = pag.screenshot(region=(0, 0, 300, 400))
    if sa!=90:
        advice()

lab = tk.Label(text="Screen & Save", font=font_specs, fg='white',bg='black').pack(pady=5)
scr = tk.Button(text="Take a Screenshot", font=fontBut, fg='grey',bg='black', command=Screenshot).pack(pady=5)
rec = tk.Button(text="Start Recording", font=fontBut, fg='grey',bg='black', command=Screenvideo).pack(pady=5)
dat.pack(pady=5) 

if __name__ == "__main__":
    master.mainloop()
