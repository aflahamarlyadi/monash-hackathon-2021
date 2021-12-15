from tkinter import *
from pathlib import Path
import fileorganizer
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.geometry("600x550")
window.resizable(width=False, height=False)
window.title("EFBOT")

icon = PhotoImage(file=r"logo.png")
window.iconphoto(True,icon)

# function
def display(title="MessageBox", message="None"):
    messagebox.showinfo(title , message)

def home(event=None):
    message = "Welcome to EFBot !"
    display("Home", message)

def about(event=None):
    message = """
    EFBot is a file organizing system developed by 
    a group of passionate students from 
    Monash University Malaysia.
    """
    display("About", message)

def contact(event=None):
    message = """
    Tan Ye Qian
    <ytan0240@student.monash.edu>

    Aflah Hanif Amarlyadi
    <aama0015@student.monash.edu>

    Yap Yong Hong
    <yyap0025@student.monash.edu>
    """
    display("Contact", message)

def reset_check_button():
    keyword_label.place_forget()
    keyword_entry.place_forget()
    keyword_note.place_forget()
    keyword_entry.delete(0, END)
    check_button.deselect()

def click_check_button():
    if check_button_input.get():
        keyword_label.place(x=10,y=400)
        keyword_entry.place(x=160,y=400)
        keyword_note.place(x=160, y=420)
    else:
        reset_check_button()
    
def report():
    display("Report", "None")

def clear_input():
    source_entry.delete(0, END)
    destination_entry.delete(0, END)
    keyword_entry.delete(0, END)
    reset_check_button()

def run():
    if source_input.get():
        source = source_input.get()
    else:
        source = Path.home() / 'Hackathon' / 'Downloads'
    
    if destination_input.get():
        destination = destination_input.get()
    else:
        destination = Path.home() / 'Hackathon'

    if keyword_input.get():
        keywords = keyword_input.get().split(',')
        for i, keyword in enumerate(keywords):
            keywords[i] = keyword.strip()
        return_msg = fileorganizer.organize_by_keyword(source, destination, keywords)
        display("Output", return_msg)
    else:
        if not check_button_input.get():
            return_msg = fileorganizer.organize_by_type(source, destination)
            display("Output", return_msg)
        else:
            messagebox.showwarning("Warning", "Please enter a keyword")

# intro
home_label = Label(window, text="Home")
home_label.bind("<Button-1>", home)
home_label.place(x=10, y=10)

about_label = Label(window, text="About")
about_label.bind("<Button-1>", about)
about_label.place(x=60, y=10)

contact_label = Label(window, text="Contact")
contact_label.bind("<Button-1>", contact)
contact_label.place(x=110, y=10)

# image
image = Image.open(r"logo.png")
resized_image = image.resize((200,200))
new_image = ImageTk.PhotoImage(resized_image)
image_label = Label(window, image=new_image)
image_label.place(x=200, y=40)

# entry
source_input = StringVar()
source_label = Label(window, text="Source directory path:")
source_label.place(x=10,y=280)
source_entry = Entry(window, width=65, textvariable=source_input)
source_entry.place(x=160,y=280)

destination_input = StringVar()
destination_label = Label(window, text="Destination directory path:")
destination_label.place(x=10,y=315)
destination_entry = Entry(window, width=65, textvariable=destination_input)
destination_entry.place(x=160,y=315)

keyword_input = StringVar()
keyword_label = Label(window, text="Enter keyword:")
keyword_entry = Entry(window, width=65, textvariable=keyword_input)
keyword_note = Label(window, text="eg. FIT1045,MAT1830,Lecture,Hackathon", fg="red",)

# button
check_button_input = BooleanVar()
check_button = Checkbutton(window, text="Select manual mode", variable=check_button_input, command=click_check_button)
check_button.place(x=10, y=345)
check_button_note = Label(window, text="NOTE: Select this mode if you want to group the files by your own preference keyword.", fg="red")
check_button_note.place(x=10, y=370)

view_button = Button(window, text="View Report", width=10, command=report)
view_button.place(x=10, y=500)

reset_button = Button(window, text="Reset", width=10, command=clear_input)
reset_button.place(x=100, y=500)

run_button = Button(window, text="Run", width=10, command=run)
run_button.place(x=195,y=500)

exit_button = Button(window, text="Exit", width=10, command=window.quit)
exit_button.place(x=500, y=500)


window.mainloop()
