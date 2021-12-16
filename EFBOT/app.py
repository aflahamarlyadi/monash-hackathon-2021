from tkinter import *
from tkinter import messagebox
from pathlib import Path
import fileorganizer

BLACK = "#000000"
WHITE = "#FFFFFF"
OFF_WHITE = "#f0f0f0"
LIGHT_GRAY = "#333333"
DARK_GRAY = "#1e1e1e"
BLUE = "#087ccc"
LIGHT_BLUE = "#2189d1"

DEFAULT_BG = "SystemButtonFace"
DEFAULT_FG = "SystemWindowText"
DEFAULT_SC = "SystemWindow"
GRAY = "light grey"

DEFAULT_FONT_STYLE = ("Calibri", 13)
LARGE_FONT_STYLE = ("Calibri", 14, "bold")
SMALL_FONT_STYLE = ("Calibri", 10)

# Functions
def hide_all_frames():
    home_frame.pack_forget()
    history_frame.pack_forget()
    settings_frame.pack_forget()
    about_frame.pack_forget()

def display_home():
    hide_all_frames()
    home_frame.pack(expand=True, fill=BOTH, side=RIGHT)

def display_history():
    hide_all_frames()
    history_frame.pack(expand=True, fill=BOTH, side=RIGHT)

def display_settings():
    hide_all_frames()
    settings_frame.pack(expand=True, fill=BOTH, side=RIGHT)

def display_about():
    hide_all_frames()
    about_frame.pack(expand=True, fill=BOTH, side=RIGHT)

def on_enter(e):
    if var.get() == 1:
        e.widget['background'] = DARK_GRAY
    else:
        e.widget['background'] = DEFAULT_BG

def on_leave(e):
    if var.get() == 1:
        e.widget['background'] = LIGHT_GRAY
    else:
        e.widget['background'] = GRAY

def reset_check_button():
    keyword_label.place_forget()
    keyword_entry.place_forget()
    keyword_note.place_forget()
    keyword_entry.delete(0, END)
    check_button.deselect()

def click_check_button():
    if check_button_input.get():
        keyword_label.place(x=20,y=100)
        keyword_entry.place(x=160,y=100)
        keyword_note.place(x=160, y=130)
    else:
        reset_check_button()

def clear_input():
    source_entry.delete(0, END)
    destination_entry.delete(0, END)
    keyword_entry.delete(0, END)
    reset_check_button()

def dark_theme():
    side_menu.config(bg=LIGHT_GRAY)
    home_frame.config(bg=DARK_GRAY)
    history_frame.config(bg=DARK_GRAY)
    settings_frame.config(bg=DARK_GRAY)
    about_frame.config(bg=DARK_GRAY)

    home_button.config(highlightcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground=OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE)
    history_button.config(activebackground=DARK_GRAY, activeforeground=OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE)
    settings_button.config(activebackground=DARK_GRAY, activeforeground=OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE)
    about_button.config(activebackground=DARK_GRAY, activeforeground=OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE)

    source_label.config(bg=DARK_GRAY, fg=WHITE)
    destination_label.config(bg=DARK_GRAY, fg=WHITE)
    check_button.config(selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground=WHITE, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
    keyword_label.config(bg=DARK_GRAY, fg=WHITE)
    keyword_note.config(bg=DARK_GRAY, fg=WHITE)
    reset_button.config(activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE)
    run_button.config(activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE)

    textarea.config(bg=DARK_GRAY, fg=WHITE)

    theme_label.config(bg=DARK_GRAY, fg=WHITE)
    theme_label.place(x=20,y=20)

    dark_mode.config(selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground=WHITE, bg=DARK_GRAY, fg=WHITE)
    light_mode.config(selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground=WHITE, bg=DARK_GRAY, fg=WHITE)
    clear_history_label.config(bg=DARK_GRAY, fg=WHITE)
    clear_history_button.config(activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE)

    about_message.config(activebackground=DARK_GRAY, activeforeground=WHITE, bg=DARK_GRAY, fg=WHITE)

def light_theme():
    side_menu.config(bg=GRAY)
    home_frame.config(bg=DEFAULT_BG)
    history_frame.config(bg=DEFAULT_BG)
    settings_frame.config(bg=DEFAULT_BG)
    about_frame.config(bg=DEFAULT_BG)

    home_button.config(highlightcolor=GRAY, activebackground=DEFAULT_BG, activeforeground=BLACK, bg=GRAY, fg=DEFAULT_FG)
    history_button.config(activebackground=DEFAULT_BG, activeforeground=BLACK, bg=GRAY, fg=DEFAULT_FG)
    settings_button.config(activebackground=DEFAULT_BG, activeforeground=BLACK, bg=GRAY, fg=DEFAULT_FG)
    about_button.config(activebackground=DEFAULT_BG, activeforeground=BLACK, bg=GRAY, fg=DEFAULT_FG)

    source_label.config(bg=DEFAULT_BG, fg=DEFAULT_FG)
    destination_label.config(bg=DEFAULT_BG, fg=DEFAULT_FG)
    check_button.config(selectcolor=DEFAULT_SC, activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG)
    keyword_label.config(bg=DEFAULT_BG, fg=DEFAULT_FG)
    keyword_note.config(bg=DEFAULT_BG, fg=DEFAULT_FG)
    reset_button.config(activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG, borderwidth=2)
    run_button.config(activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG, borderwidth=2)

    textarea.config(bg=DEFAULT_BG, fg=DEFAULT_FG)

    theme_label.config(bg=DEFAULT_BG, fg=DEFAULT_FG)

    dark_mode.config(selectcolor=DEFAULT_SC, activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG)
    light_mode.config(selectcolor=DEFAULT_SC, activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG)
    clear_history_label.config(bg=DEFAULT_BG, fg=DEFAULT_FG)
    clear_history_button.config(activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG, borderwidth=2)

    about_message.config(activebackground=DEFAULT_BG, activeforeground=DEFAULT_FG, bg=DEFAULT_BG, fg=DEFAULT_FG)

def set_theme():
    if var.get() == 1:
        dark_theme()

    else:
        light_theme()


def clear_history():
    open("history.txt", "w").close()
    textarea.delete("1.0","end")
    pass

def update_history(update):
    file = open('history.txt', 'a')
    file.write(update)
    file.close()
    pass

def read_history():
    file = open('history.txt', 'r')
    for line in file:
        textarea.insert(END, line)
    file.close()
    pass

def run():
    total_deleted_files = 0
    total_moved_files = 0

    if source_input.get():
        source = source_input.get()
    else:
        source = Path.home() / 'Hackathon' / 'Downloads'
    
    if destination_input.get():
        destination = destination_input.get()
    else:
        destination = Path.home() / 'Hackathon'

    (history, deleted_files) = fileorganizer.remove_duplicates(source)
    total_deleted_files += deleted_files
    update_history(history)

    if keyword_input.get():   
        keywords = keyword_input.get().split(',')
        for i, keyword in enumerate(keywords):
            keywords[i] = keyword.strip()
        (history, moved_files, deleted_files) = fileorganizer.organize_by_keyword(source, destination, keywords)
    else:
        (history, moved_files, deleted_files) = fileorganizer.organize_by_type(source, destination)
    total_deleted_files += deleted_files
    total_moved_files += moved_files
    update_history(history)

    message = f'Total number of files moved: {total_moved_files}\nTotal number of files deleted: {total_deleted_files}'
    messagebox.showinfo("Analytics" , message)
    read_history()

window = Tk()
window.geometry("800x450")
window.resizable(width=False, height=False)
window.title("EFBot")

icon = PhotoImage(file=r"logo.png")
window.iconphoto(True,icon)

side_menu = Frame(window, bg=LIGHT_GRAY, borderwidth=0)
side_menu.pack(expand=False, fill=BOTH, side=LEFT, anchor=NW)

home_frame = Frame(window, width=500, bg=DARK_GRAY)
home_frame.pack(expand=True, fill=BOTH, side=RIGHT)

history_frame = Frame(window, width=500, bg=DARK_GRAY)

settings_frame = Frame(window, width=500, bg=DARK_GRAY)

about_frame = Frame(window, width=500, bg=DARK_GRAY)

# Tabs
home_button = Button(side_menu, text="Home    ", highlightcolor=LIGHT_GRAY, activebackground = DARK_GRAY, activeforeground = OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE, font=LARGE_FONT_STYLE, padx=20, pady=5, borderwidth=0, command=display_home)
home_button.pack(fill=BOTH, anchor=W)
home_button.bind('<Enter>', on_enter)
home_button.bind('<Leave>', on_leave)

history_button = Button(side_menu, text="History  ", activebackground = DARK_GRAY, activeforeground = OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE, font=LARGE_FONT_STYLE, padx=20, pady=5, borderwidth=0, command=display_history)
history_button.pack(fill=BOTH, anchor=W)
history_button.bind('<Enter>', on_enter)
history_button.bind('<Leave>', on_leave)

settings_button = Button(side_menu, text="Settings", activebackground = DARK_GRAY, activeforeground = OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE, font=LARGE_FONT_STYLE, padx=20, pady=5, borderwidth=0, command=display_settings)
settings_button.pack(fill=BOTH, anchor=W)
settings_button.bind('<Enter>', on_enter)
settings_button.bind('<Leave>', on_leave)

about_button = Button(side_menu, text="About    ", activebackground = DARK_GRAY, activeforeground = OFF_WHITE, bg=LIGHT_GRAY, fg=WHITE, font=LARGE_FONT_STYLE, padx=20, pady=5, borderwidth=0, command=display_about)
about_button.pack(fill=BOTH, anchor=W)
about_button.bind('<Enter>', on_enter)
about_button.bind('<Leave>', on_leave)

# Home
source_input = StringVar()
source_label = Label(home_frame, text="Source folder:", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
source_label.place(x=20,y=20)
source_entry = Entry(home_frame, font=DEFAULT_FONT_STYLE, width=50, textvariable=source_input)
source_entry.place(x=160,y=20)

destination_input = StringVar()
destination_label = Label(home_frame, text="Destination folder:", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
destination_label.place(x=20,y=60)
destination_entry = Entry(home_frame, font=DEFAULT_FONT_STYLE, width=50, textvariable=destination_input)
destination_entry.place(x=160,y=60)

check_button_input = BooleanVar()
check_button = Checkbutton(home_frame, text="Organize by keywords", selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground = WHITE, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE, variable=check_button_input, command=click_check_button)
check_button.place(x=20, y=400)

keyword_input = StringVar()
keyword_label = Label(home_frame, text="Enter keyword:", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
keyword_entry = Entry(home_frame, font=DEFAULT_FONT_STYLE, width=50, textvariable=keyword_input)
keyword_note = Label(home_frame, text="eg. FIT1045, Lecture, Hackathon, Animals, Artists", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)

reset_button = Button(home_frame, text="Reset", activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE, font=DEFAULT_FONT_STYLE, width=10, borderwidth=0, command=clear_input)
reset_button.place(x=460, y=400)

run_button = Button(home_frame, text="Run", activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE, font=DEFAULT_FONT_STYLE, width=10, borderwidth=0, command=run)
run_button.place(x=570,y=400)

# History
ver_sb = Scrollbar(history_frame, orient=VERTICAL )
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(history_frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

textarea = Text(history_frame, bd=0, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE, width=40, height=20)
textarea.pack(fill=BOTH)

textarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=textarea.yview)

textarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=textarea.xview)

read_history()

# Settings
theme_label = Label(settings_frame, text="Theme", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
theme_label.place(x=20,y=20)

var = IntVar()
dark_mode = Radiobutton(settings_frame, text="Dark mode", selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground = WHITE, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE, variable=var, value=1, command=set_theme)
dark_mode.place(x=30,y=50)
dark_mode.select()

light_mode = Radiobutton(settings_frame, text="Light mode", selectcolor=LIGHT_GRAY, activebackground=DARK_GRAY, activeforeground = WHITE, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE, variable=var, value=2, command=set_theme)
light_mode.place(x=30,y=80)

clear_history_label = Label(settings_frame, text="History", bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE)
clear_history_label.place(x=20,y=120)

clear_history_button = Button(settings_frame, text="Clear history", activebackground=LIGHT_BLUE, activeforeground=OFF_WHITE, bg=BLUE, fg=WHITE, font=DEFAULT_FONT_STYLE, width=10, borderwidth=0, command=clear_history)
clear_history_button.place(x=40,y=160)


# About
about_message = Label(about_frame, 
    text=
    """
    EFBot is a file organizing system developed by a group of passionate students from 
    Monash University Malaysia.
    For bugs, errors and feedbacks, please contact us:
    Tan Ye Qian <ytan0240@student.monash.edu>
    Aflah Hanif Amarlyadi <aama0015@student.monash.edu>
    Yap Yong Hong <yyap0025@student.monash.edu>
    """, 
    activebackground=DARK_GRAY, activeforeground = WHITE, bg=DARK_GRAY, fg=WHITE, font=DEFAULT_FONT_STYLE, justify=LEFT)
about_message.pack(anchor=NW)

window.mainloop()
