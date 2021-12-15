from tkinter import *
from pathlib import Path
import time
import fileorganizer


window = Tk()
window.geometry("480x200")
window.resizable(width=False, height=False)
window.title("EFBOT")

icon = PhotoImage(file=r'icon.png')
window.iconphoto(True,icon)

source_input = StringVar()
destination_input = StringVar()
keyword_input = StringVar()

def run():

    if source_input.get():
        source = source_input.get()
    else:
        source = Path.home() / 'Hackathon' / 'Downloads'
    
    if destination_input.get():
        destination = destination_input.get()
    else:
        destination = Path.home() / 'Hackathon'

    fileorganizer.remove_duplicates(source)

    if keyword_input.get():
        keywords = keyword_input.get().split(',')
        for i, keyword in enumerate(keywords):
            keywords[i] = keyword.strip()
        fileorganizer.organize_by_keyword(source, destination, keywords)
    else:
        fileorganizer.organize_by_type(source, destination)

source_label = Label(window, text="Source directory path:")
source_label.place(x=10,y=10)

source_entry = Entry(window, width=50, textvariable=source_input)
source_entry.place(x=160,y=10)

destination_label = Label(window, text="Destination directory path:")
destination_label.place(x=10,y=40)

destination_entry = Entry(window, width=50, textvariable=destination_input)
destination_entry.place(x=160,y=40)

keyword_label = Label(window, text="Enter keyword:")
keyword_label.place(x=10,y=70)

keyword_entry = Entry(window, width=50, textvariable=keyword_input)
keyword_entry.place(x=160,y=70)

keyword_label = Label(window, text="NOTE: Leave this entry empty to organize files by file type OR type keywords", fg="RED")
keyword_label.place(x=10,y=95)

keyword_label2 = Label(window, text="to organize files by keywords eg. FIT1045, MAT1830, Lecture, Hackathon", fg="RED")
keyword_label2.place(x=10,y=115)

run_button = Button(window, text="Run", width=10, command=run)
run_button.place(x=385,y=160)

window.mainloop()
