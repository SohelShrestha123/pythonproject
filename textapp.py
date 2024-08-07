import tkinter as tk
from tkinter import ttk

class Box():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.title('Text App')
        self.mainframe=tk.Frame(self.root,background='lightblue')
        self.mainframe.pack(fill="both", expand=True)

        self.text=ttk.Label(self.mainframe, text="Python",background='lightblue',font=("Brass Mono",14))
        self.text.grid(row=0, column=0)

        self.set_text_field=ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0,pady=10,sticky='NWES')
        set_text_button=ttk.Button(self.mainframe,text='Set Text',command=self.set_text)
        set_text_button.grid(row=1,column=1,pady=10)
        
        color_opt=['Red','Green','Blue','Yellow','Black']
        self.set_color_field=ttk.Combobox(self.mainframe, values=color_opt)
        self.set_color_field.grid(row=2, column=0,pady=10,sticky='NWES')
        set_clr_button=ttk.Button(self.mainframe,text='Set Color',command=self.set_color)
        set_clr_button.grid(row=2,column=1,pady=10)

        self.reverse_txt=ttk.Button(self.mainframe, text="Reverse text", command=self.reverse)
        self.reverse_txt.grid(row=3,column=0,sticky='NWES',pady=10)



        self.root.mainloop()
        return
    
    def set_text(self):
        txt=self.set_text_field.get()
        self.text.config(text=txt)

    def set_color(self):
        clr=self.set_color_field.get()
        self.text.config(foreground=clr)

    def reverse(self):
        rev=self.text.cget('text')
        reversed=rev[::-1]
        self.text.config(text=reversed)
    
if __name__=='__main__':
    Box()