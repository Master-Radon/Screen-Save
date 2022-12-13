#import libraries
import tkinter as tk
import pyautogui as pag
import os

#build default directory (where screenshots are saved)
try:
    os.mkdir('%Screenshots%')
except Exception as e:
    pass

#build GUI
master = tk.Tk() #create window
master.resizable(False,False) #not resizable
master.title('Screen & Save') #set title
master.geometry("200x140") #set dimension
master.configure(bg='black') #set background
master.iconbitmap('image/radioactive.ico') #set icon

font_specs = ("Algerian", 15) #set label font
fontBut = ("Arial",10) #set button font

#show message that everything went good
def ads():
    leb = tk.Label(text="Screenshot saved in\n%Screenshots% directory", font=fontBut, fg='white',bg='black') #build label
    leb.pack(pady=5)
    leb.after(3000, lambda: leb.destroy()) #delete label after 3 secs

#save screenshot
def Screenshot():
    mys = pag.screenshot() #take screenshot
    dir_list = os.listdir(r'%Screenshots%') #get all files in default directory
    i = len(dir_list) #get progressive number
    mys.save(r'%Screenshots%\Screenshot_'+str(i)+'.png') #save screenshot with progressive number
    ads() #call label everything went good

lab = tk.Label(text="Screen & Save", font=font_specs, fg='white',bg='black').pack(pady=5) #label window title
scr = tk.Button(text="Take a Screenshot", font=fontBut, fg='grey',bg='black', command=Screenshot).pack(pady=5) #button to take screenshot

if __name__ == "__main__":
    master.mainloop() #start application
