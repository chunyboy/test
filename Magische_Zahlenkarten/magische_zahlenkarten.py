"""Magische Zahlenkarten

**********************************
*Autor:        Marco Schmid      *
*Date:         26.05.14          *
*Version:      1.01              *
**********************************

Beschreibung
************

Der Proband wird aufgefordert, sich eine Zahl zwischen 1 und 63 
zu merken. Alle Karten, auf welchen diese gemerkte Zahl vorkommt,
soll angeklickt werden (das Feld wird rot angefärbt).

Auf Los! klicken und die gemerkte Zahl erscheint von Zauberhand.
"""

import tkinter as tk
from tkinter import messagebox

class Karte:
    def __init__(self, active_path, passiv_path, nummer, status=False):
        self.active_path = active_path
        self.passiv_path = passiv_path
        self.nummer = nummer
        self.status = status
    
    def change_status(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False
            
 
class Application:
 
    def __init__(self, master):
        
        master.title("Die magischen Zahlenkarten")
 
        # Oberer Teil des GUIs. Mit Titel und Beschreibungen
        frame1 = tk.Frame(master)
        frame1.pack()
        
        frame2 = tk.Frame(master)
        frame2.pack()
        
        my_title = "Magische Zahlenkarten"
        my_info = "Beschreibung: \n\
Merke dir eine Zahl zwischen 1 und 63. \
Klicke auf jede Karte, auf welcher \
deine gemerkte Zahl vorkommt. Sind \
alle Karten markiert (rot angefärbt) auf welchen deine Zahl vorkommt, \
so klicke weiter unten auf Los!"

        the_title = tk.Message(frame1, text = my_title)
        the_title.config(width = 340, font=("Times", "24", "bold italic") )  
        the_title.grid(row=0)
        
        beschreibung = tk.Message(frame2, text = my_info)
        beschreibung.config(width = 300)  
        beschreibung.grid(row=0, column=0, rowspan = 2, padx = 60)
        
        my_info2 = 'Wenn du alle Felder markiert hast, \
auf welchen sich deine gewünschte Zahl befindet, \
dann klicke auf "Los!"'
        beschreibung2 = tk.Message(frame2, text = my_info2, width = 200)
        beschreibung2.grid(row=0, column=1, columnspan = 2, padx = 20)
        
        tk.Button(frame2, text = "Los!", command = self.action_magic_guess).grid(row = 1, column = 1, sticky = tk.E)
        tk.Button(frame2, text = "Exit", command = master.quit).grid(row = 1, column = 2, sticky = tk.W )
        
        
        self.txt_magic_guess = tk.Message(frame2, width = 500, font=("Times", "16", "bold italic"))
        self.txt_magic_guess.grid(row = 2, column = 0, columnspan = 3)
     
        
        # Erstellen der Bilder-Button
        self.frame_karten = tk.Frame(master)
        self.frame_karten.pack()
        
        self.karten_list = []
        self.button_list = []
        self.image_list = []
        
        
        pic_dir = "./pics/"
        
        for i in range(2):
            for j in range(3):
                glob_nr = 3*i + j
                passiv_path = pic_dir + "b" + str(2**glob_nr) + ".gif"
                active_path = pic_dir + "b" + str(2**glob_nr) + str(2**glob_nr) + ".gif"
                self.karten_list.append(Karte(active_path, passiv_path, glob_nr))               
                self.image_list.append(tk.PhotoImage(file=passiv_path))
                
                self.button_list.append(tk.Button(self.frame_karten, image = self.image_list[glob_nr], 
                                                  command=lambda glob_nr=glob_nr: self.action_change_button(glob_nr)))    
                self.button_list[glob_nr].grid(row=i, column=j)
         
        # Menu erstellen 
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Los!", command=self.action_magic_guess)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Info!", command=self.action_get_info_dialog)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        master.config(menu=menubar)          
        
# Funktionen, welche bei einem Klick auf das entsprechende Icon ausgeführt werden        
    def action_change_button(self, nummer):
        if (self.karten_list[nummer].status ==False):
            self.image_list[nummer] = tk.PhotoImage(file=self.karten_list[nummer].active_path)
            
            self.button_list[nummer] = tk.Button(self.frame_karten, image = self.image_list[nummer], 
                                                 command=lambda:self.action_change_button(nummer))
            self.karten_list[nummer].change_status()
            
            self.button_list[nummer].grid(row=nummer // 3, column=nummer % 3)
        else:    
            self.image_list[nummer] = tk.PhotoImage(file=self.karten_list[nummer].passiv_path)
            
            self.button_list[nummer] = tk.Button(self.frame_karten, image = self.image_list[nummer], 
                                                 command=lambda:self.action_change_button(nummer))
            self.karten_list[nummer].change_status()
            
            self.button_list[nummer].grid(row=nummer // 3, column=nummer % 3)  
            
            
    def action_magic_guess(self):
        magic_result = 0
        for karte in self.karten_list:
            if karte.status == True:
                magic_result += 2**karte.nummer
        my_guess = "Die gedachte Zahl lautet: " + str(magic_result)
        self.txt_magic_guess.config(text = my_guess)

    
    def action_get_info_dialog(self):
        m_text = "Magische Zahlenkarten\n\n\
************************\n\
Autor: Marco Schmid\n\
Date: 26.05.14\n\
Version: 1.01\n\
************************"
        messagebox.showinfo(message=m_text, title = "Infos")

# MAIN ---------------------------------------------------------------
root = tk.Tk()
app = Application(root) 

root.mainloop()