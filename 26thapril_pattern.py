from tkinter import filedialog
import pyautogui as p
import time
import os
import tkinter as tk
from datetime import datetime



num_rows = int(input("Enter the number of rows"))
k = 0
for i in range(1, num_rows + 1): 
    for j in range (1, (num_rows - i) + 1): 
        print(end = " ")          
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0   
    print()  


time.sleep(5)
screen=p.screenshot()
folder=filedialog.askdirectory()
c=datetime.now()
c=c.replace(microsecond=0)
format="%y_%b_%d_%H_%M_%S"
c=datetime.strftime(c,format)
file_name="ashika1"+c+".png"
file=os.path.join(folder,file_name)
screen.save(file)


k = 2
m = 15
for i in range(1, num_rows): 
    for j in range (1, k):
        print(end = " ") 
    k = k + 1	  
    while m <= (2 * (num_rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1	
    print()




rows = input("Enter maximum stars you want display on a single line")
rows = int (rows)
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")
time.sleep(5)
screen=p.screenshot()
folder=filedialog.askdirectory()
c=datetime.now()
c=c.replace(microsecond=0)
format="%y_%b_%d_%H_%M_%S"
c=datetime.strftime(c,format)
file_name="ashika2"+c+".png"
file=os.path.join(folder,file_name)
screen.save(file)