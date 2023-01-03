from tkinter import *
from tkinter import filedialog
from docx2pdf import convert
from pdf2docx import parse
def convert_docxtopdf():
    filepath=filedialog.askopenfilename()
    convert(filepath)
def convert_pdftodocx():
    filepath=filedialog.askopenfilename()
    parse(filepath)
window=project()
window.geometry("200x100")
b1=Button(text='convert docx 2 pdf',command=convert_docxtopdf)
b1.pack()
b2=Button(text='convert pdf 2 docx',command=convert_pdftodocx)
b2.pack()
b3=Button(text="EXIT",command=window.destroy)
b3.pack()
window.mainloop()

