# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:20:25 2021

@author: Amlan Ghosh
"""

# importing tkinter and pandastable
import pandas as pd
import tkinter as tk
from tkinter import *
from pandastable import Table

# making main UI
top = tk.Tk()
top.title('Solver')     # setting title
top.geometry('600x600') #setting geometry


# making Frame
f = Frame(top, height = 350, width = 350)
f.pack()

# Defining string variable
cheap_var = tk.StringVar()
lead_var = tk.StringVar()

cost = tk.StringVar()
days = tk.StringVar()

d = tk.StringVar()
l = tk.StringVar()

o = tk.StringVar()

# Function to upload csv file
def demand():
    d.set(filedialog.askopenfilename(initialdir = '/Desktop', title = 'Select Demand Data',
                                                            filetypes = (('csv file','*.csv'),
                                                                          ('csv file','*.csv'))))

def liner():
    l.set(filedialog.askopenfilename(initialdir = '/Desktop', title = 'Select Liner Data',
                                                            filetypes = (('csv file','*.csv'),
                                                                         ('csv file','*.csv'))))

# Function to run a function
def run():
    cheap = cheap_var.get()
    lead = lead_var.get()
    
    demand_data = d.get()
    liner_data = l.get()
    
    if cheap != '' and lead != '':
        
        
        a,b, c = function(float(cheap), float(lead), str(demand_data), str(liner_data))
        
        cost.set(str(a))
        days.set(str(b))
        o.set(str(c))
        
 #Function to display a csv file in another window            
def show():
    
    window2 = tk.Toplevel()
    window2.title('Output')
    window2.geometry('1200x1000')
    
    output = o.get()
    
    df = pd.read_csv(str(output))
    
    f1 = Frame(window2, height = 300, width = 300) 
    f1.pack(fill=BOTH,expand=1)
    table = Table(f1, dataframe=c,read_only=True)
    table.show()

def show_demand():
    
    window = tk.Toplevel()
    window.title('Demand Data')
    
    window.geometry('1200x1000')
    output = d.get()
    
    df = pd.read_csv(str(output))
    
    f2 = Frame(window, height = 300, width = 300) 
    f2.pack(fill=BOTH,expand=1)
    table = Table(f2, dataframe=df,read_only=False, showtoolbar = True, showstatusbar = True)
    table.show()

def show_liner():
    
    window1 = tk.Toplevel()
    window1.title('Liner Data')
    
    window1.geometry('1200x1000')
    
    output = l.get()
    
    df = pd.read_csv(str(output))
    
    f3 = Frame(window1, height = 300, width = 300) 
    f3.pack(fill=BOTH,expand=1)
    table = Table(f3, dataframe=df,read_only=True)
    table.show()
    
# Defining button
Button(f, text = 'Upload Demand Data', command = demand).place(x = 30, y = 10)
Button(f, text = 'Upload Liner Data', command = liner).place(x = 180, y = 10)

Button(f, text = 'Show Demand Data', command = show_demand).place(x = 30, y = 50)
Button(f, text = 'Show Liner Data', command = show_liner).place(x = 180, y = 50)

#Definig Label and Entry       
Label(top, text = 'Cheap priority').place(x = 30,y = 90)
Entry(top, textvariable = cheap_var).place(x = 130, y = 90) 
Label(top, text = 'Leadtime priority').place(x = 30,y = 130)  
Entry(top, textvariable = lead_var).place(x = 130, y = 130)

Button(f, text = 'Run', command = run).place(x = 30, y = 170)

Label(top, text = 'Cost').place(x = 30,y = 210)
Entry(top, textvariable = cost).place(x = 130, y = 210)  
Label(top, text = 'Container Days').place(x = 30,y = 250)  
Entry(top, textvariable = days).place(x = 130, y = 250)

Button(f, text = 'Show Output', command = show).place(x = 30, y = 290)

# generating the UI
top.mainloop()