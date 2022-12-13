#import libraries
import tkinter as tk
import pyautogui as pag
import cv2
import numpy as np
import os

#create default directory where saved screenshots and videos
try:
    os.mkdir('%Records%')
except Exception as e:
    pass
try:
    os.mkdir('%Screenshots%')
except Exception as e:
    pass

#build window
master = tk.Tk() #create window
master.resizable(False,False) #not resizable
master.title('Screen & Save') #set title
master.geometry("200x180") #set dimension
master.configure(bg='black') #set background
master.iconbitmap('image/radioactive.ico') #set icon

font_specs = ("Algerian", 15) #set label font
fontBut = ("Arial",10) #set button font
dat = tk.Entry(width=10) #set textField

#all went good message
def ads():
    leb = tk.Label(text="Screenshot saved in\n%Screenshots% directory", font=fontBut, fg='white',bg='black') #create label
    leb.pack(pady=5)
    leb.after(3000, lambda: leb.destroy()) #delete message after 3 sec

#take screenshot
def Screenshot():
    mys = pag.screenshot() #take screenshot
    dir_list = os.listdir(r'%Screenshots%') #get all file in screenshot
    i = len(dir_list) #get progressive number
    mys.save(r'%Screenshots%\Screenshot_'+str(i)+'.png') #save screenshot with progressive number
    ads() #call message all went good

#all went good message
def advice():
    re = tk.Label(text='Video Completed!',font=fontBut,bg='black',fg='white') #create label
    re.pack(pady=5)
    re.after(3000, lambda: re.destroy()) #delete message after 3 sec

#take video
def Screenvideo():
    dir_list = os.listdir(r'%Records%') #get files in records directory
    i = len(dir_list) #get progressive number
    path = r'%Records%\ScreenRecord_'+str(i)+'.avi' #save it with progressive number
    sec = dat.get() #get seconds length video
    #start video
    er = tk.Label(text="ON AIR!",font=fontBut,bg='black',fg='white') 
    er.pack(pady=5)
    sa = 1
    try:
        record_seconds = int(sec)
        er.after(record_seconds, lambda: er.destroy())
        sa = 0
    except Exception as e: #if error, report it
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

lab = tk.Label(text="Screen & Save", font=font_specs, fg='white',bg='black').pack(pady=5) #name
scr = tk.Button(text="Take a Screenshot", font=fontBut, fg='grey',bg='black', command=Screenshot).pack(pady=5) #screenshot button
rec = tk.Button(text="Start Recording", font=fontBut, fg='grey',bg='black', command=Screenvideo).pack(pady=5) #start recording
dat.pack(pady=5) 

if __name__ == "__main__":
    master.mainloop() #start application
