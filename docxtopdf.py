# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:19:19 2023

@author: 91630
"""

from tkinter import *
 
import tkinter.font as font
from tkinter import filedialog
from docx2pdf import convert
 
def convert_docxtopdf():
    filepath=filedialog.askopenfilename()
    convert(filepath)
 
window=Tk()
window.title('DOCX PDF CONVERFTER')
window.minsize(width=600,height=600)
window.geometry("1000x400") 
 
headingFrame1 = Frame(window,bg="DodgerBlue4",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="DOCX PDF CONVERTER", bg='firebrick', fg='black', font=('Courier',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
myFont=font.Font(size=20)
b1=Button(text='convert docx 2 pdf',bg='DodgerBlue4',activebackground='firebrick',fg='white',command=convert_docxtopdf)
b1['font']=myFont
b1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
 
b3=Button(text="EXIT",bg='black',fg='white',command=window.destroy)
b3['font']=myFont
b3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
window.mainloop()
