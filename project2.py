
from tkinter import * 
from PIL import ImageTk
import tkinter.font as font
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import parse
def convert_docxtopdf():
     filepath=filedialog.askopenfilename()
     convert(filepath)
def convert_pdftodocx():
     filepath=filedialog.askopenfilename()
     parse(filepath)
window=Tk()
window.title('DOCX PDF CONVERFTER')
window.minsize(width=600,height=600)
window.geometry("1000x400") 
bg= ImageTk.PhotoImage(file="C:/Users/91630/Pictures/pdf-to-word-banner.png")
canvas= Canvas(window,width=0, height=0)
canvas.pack(expand=True, fill=BOTH)
canvas.create_image(150,200,image=bg, anchor="nw")
headingFrame1 = Frame(window,bg="DodgerBlue4",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="DOCX PDF CONVERTER", bg='firebrick', fg='black', font=('Courier',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
myFont=font.Font(size=20)
b1=Button(text='convert docx 2 pdf',bg='DodgerBlue4',activebackground='firebrick',fg='white',command=convert_docxtopdf)
b1['font']=myFont
b1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
b2=Button(text='convert pdf 2 docx',bg='firebrick',activebackground='DodgerBlue4',fg='white',command=convert_pdftodocx)
b2['font']=myFont
b2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)
b3=Button(text="EXIT",bg='black',fg='white',command=window.destroy)
b3['font']=myFont
b3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
window.mainloop()