# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 03:00:36 2019

@author: Rishabh Chandra
"""

import tkinter as tk
import steganography as algo
import generate_key as keys
import webbrowser
from tkinter import filedialog

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class encodePage(Page):
    
    def encoder(self):
        try:
            pk=(int(self.entry_key1.get()),int(self.entry_key2.get()))
            algo.encodePic(self.entry_msg.get("1.0","end-1c"),pk,self.filepath)
            self.label_floc.config(text="secret.PNG created in current directory with encoded message.")
            
        except:
            self.label_floc.config(text="Invalid Inputs. Enter both key fields and select image first.")
                
    
    def browseFile(self):
        try:
            filename = filedialog.askopenfile()
            self.label_floc.config(text="Image Selected!")
            self.filepath = filename.name
            print(self.filepath)
        except:
            self.label_floc.config(text="Select image!")
            pass
    
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       keyframe = tk.Frame(self)
       
       label_msg = tk.Label(self, text="Enter message : ")
       self.entry_msg = tk.Text(self,width=30,height=5)
       label_key = tk.Label(self, text="Public Keys\n for encryption E & N: ")
       self.entry_key1 = tk.Entry(keyframe,width=40)
       self.entry_key2 = tk.Entry(keyframe,width=40)
       self.label_floc = tk.Label(self,text="Select image for encoding.")
       button_floc = tk.Button(self, text="Select Image", command=self.browseFile)
       button_encode = tk.Button(self, text="ENCODE", command=self.encoder)
       
       self.columnconfigure(0,weight=2)
       self.columnconfigure(1,weight=2)
       
       label_msg.grid(row=0,column=0,pady=3)
       self.entry_msg.grid(row=0,column=1,pady=2,padx=2)
       
       label_key.grid(row=1,column=0,pady=3)
       keyframe.columnconfigure(0,weight=1)
       self.entry_key1.grid(row=0,pady=3)
       self.entry_key2.grid(row=1,pady=3)
       keyframe.grid(row=1,column=1,pady=2)
       
       self.label_floc.grid(row=3,column=0,pady=3, columnspan=2)
       button_floc.grid(pady=3,padx=6,columnspan=2,sticky=tk.E+tk.W)
       button_encode.grid(pady=3,padx=6,columnspan=2,sticky=tk.E+tk.W)
       
       
       
class decodePage(Page):
    def decoder(self):
        try:
            pk=(int(self.entry_key1.get()),int(self.entry_key2.get()))
            msg = algo.decodePic(pk,self.filepath)
            self.showmsg.config(state=tk.NORMAL)
            self.showmsg.delete('1.0', tk.END)
            self.showmsg.insert(tk.END,msg)
            self.showmsg.config(state=tk.DISABLED)
        except ValueError:
            self.showmsg.config(state=tk.NORMAL)
            self.showmsg.delete('1.0', tk.END)
            self.showmsg.insert(tk.END,"Invalid inputs. Enter both key fields and select image first.")
            self.showmsg.config(state=tk.DISABLED)
        except:
            self.showmsg.config(state=tk.NORMAL)
            self.showmsg.delete('1.0', tk.END)
            self.showmsg.insert(tk.END,"Incorrect private key.")
            self.showmsg.config(state=tk.DISABLED)
           
        
    def browseFile(self):
        try:
            filename = filedialog.askopenfile()
            self.label_floc.config(text="Image Selected!")
            self.filepath = filename.name
            print(self.filepath)
        except:
            self.label_floc.config(text="Select image!")
            pass

    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       self.columnconfigure(0,weight=2)
       self.columnconfigure(1,weight=2)
       
       
       label_key = tk.Label(self, text="Private keys\n for decryption D & N : ")
       keyframe = tk.Frame(self)
       self.entry_key1 = tk.Entry(keyframe,width=40)
       self.entry_key2 = tk.Entry(keyframe,width=40)
       label_key.grid(row=0,column=0,pady=3)
       self.entry_key1.grid(row=0,pady=3,padx=2)
       self.entry_key2.grid(row=1,pady=3,padx=2)
       keyframe.grid(row=0,column=1,pady=3)
       self.label_floc = tk.Label(self,text="Select image for decoding.", width=20)
       button_floc = tk.Button(self, text="Select Image", command=self.browseFile)
       self.label_floc.grid(row=3,column=0,pady=3,padx=2,columnspan=2)
       button_floc.grid(row=4,pady=3,padx=2,columnspan=2,sticky=tk.E+tk.W)
       
       button_encode = tk.Button(self, text="DECODE", command=self.decoder)
       button_encode.grid(pady=3,columnspan=2,sticky=tk.E+tk.W,padx=2)
       
       self.showmsg = tk.Text(self,state=tk.DISABLED,height=5)
       self.showmsg.grid(columnspan=2,pady=15,padx=5)

class keyPage(Page):
   def genkey(self):
       if(self.entry_p.get()!="" and self.entry_q.get()!="" and len(self.entry_p.get())==len(self.entry_q.get())):
           k=keys.generatePair(int(self.entry_p.get()),int(self.entry_q.get()))
       else:
           k = keys.generatePair()
    
       self.tb_d.config(state=tk.NORMAL)
       self.tb_e.config(state=tk.NORMAL)
       self.tb_n.config(state=tk.NORMAL)
       self.tb_e.delete('1.0', tk.END)
       self.tb_n.delete('1.0', tk.END)
       self.tb_d.delete('1.0', tk.END)
       self.tb_e.insert(tk.END,"E: " + str(k[0]))
       self.tb_d.insert(tk.END,"D: " + str(k[1]))
       self.tb_n.insert(tk.END,"N: " + str(k[2]))
       self.tb_d.config(state=tk.DISABLED)
       self.tb_e.config(state=tk.DISABLED)
       self.tb_n.config(state=tk.DISABLED)
       
   
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
       self.columnconfigure(0,weight=2)
       self.columnconfigure(1,weight=2)
       
       heading = tk.Label(self, text="You can enter your own N-digit prime numbers or leave it\n empty if you want to use default 50 digit primes.")
       heading.grid(row=0,columnspan=2,pady=3,padx=5)
       
       
       label_p = tk.Label(self, text="Prime P : ")
       label_q = tk.Label(self, text="Prime Q : ")
       self.entry_p = tk.Entry(self,width=40)
       self.entry_q = tk.Entry(self,width=40)
       button_gen  = tk.Button(self,text="Generate Keys",command=self.genkey)
       
       self.tb_e = tk.Text(self,width=40,height=3,pady=5)
       self.tb_d = tk.Text(self,width=40,height=3,pady=5)
       self.tb_n = tk.Text(self,width=40,height=3,pady=5)
       self.tb_d.config(state=tk.DISABLED)
       self.tb_e.config(state=tk.DISABLED)
       self.tb_n.config(state=tk.DISABLED)
       
       label_p.grid(row=1,column=0,pady=3,padx=2)
       self.entry_p.grid(row=1,column=1,pady=3,padx=2)
       label_q.grid(row=2,column=0,pady=3,padx=2)
       self.entry_q.grid(row=2,column=1,pady=3,padx=2)
       button_gen.grid(row=3,column=0,columnspan=2,pady=3,padx=2,sticky=tk.W+tk.E)
       self.tb_e.grid(column=0,columnspan=2,pady=3,padx=2)
       self.tb_d.grid(column=0,columnspan=2,pady=3,padx=2)
       self.tb_n.grid(column=0,columnspan=2,pady=3,padx=2)
       
class aboutPage(Page):
    about = "Created by Rishabh Chandra.\n Learn more about it.\n Visit link below."
   
    def callback(self,event):
        webbrowser.open_new(event.widget.cget("text"))
    
    def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       self.columnconfigure(0,weight=2)
       heading = tk.Label(self, text="SNEAK100", fg="Green", font=("HELVETICA",20))
       heading.grid(pady=3,padx=5)
       txt = tk.Label(self, text=self.about)
       txt.grid(pady=3,padx=5)
       lbl = tk.Label(self, text=r"https://github.com/chandrarishabh/SNEAK100", fg="blue", cursor="hand2")
       lbl.grid(padx=5)
       lbl.bind("<Button-1>", self.callback)
           


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = encodePage(self)
        p2 = decodePage(self)
        p3 = keyPage(self)
        p4 = aboutPage(self)
        
        buttonframe = tk.Frame(self)
        aboutframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        aboutframe.pack(side="bottom", fill="x", expand=False)

        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        

        b1 = tk.Button(buttonframe, text="ENCODE", height=3,width=10, command=p1.lift)
        b2 = tk.Button(buttonframe, text="DECODE", height=3,width=10, command=p2.lift)
        b3 = tk.Button(buttonframe, text="GENERATE KEY", height=3,width=10,command=p3.lift)
        b4 = tk.Button(aboutframe, text="ABOUT", height=3,width=10,command=p4.lift)
        
        
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        aboutframe.columnconfigure(0, weight=1)
        
        
        b1.grid(row=0,column=0,sticky=tk.W+tk.E,pady=3)
        b2.grid(row=0,column=1,sticky=tk.E+tk.W,pady=3)
        b3.grid(row=0,column=2,sticky=tk.E+tk.W,pady=3)
        b4.grid(row=0,sticky=tk.E+tk.W,pady=3)
      
        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SNEAK100")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x500")
    root.mainloop()
    