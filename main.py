import tkinter
from tkinter import *

from editor import Editor

COLOR = '#E7B10A'

# GUI Creation
root = tkinter.Tk()

status_label = Label(text='Please select an image:')
status_label.grid(column=0, row=5, pady=20)

editor = Editor(root, status_label)
root.title("Photo Editor")
root.geometry('500x450+50+50')
root.config(bg=editor.BACKGROUND_COLOR, padx=50, pady=50)
select_files_button = Button(text="select_file", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                             command=editor.select_file)
select_files_button.grid(column=0, row=0)
canvas = Canvas(width=223, height=223, bg=COLOR, highlightthickness=0)
selected_img = PhotoImage(file=editor.FILE_PATH)
background = canvas.create_image(110, 110, image=selected_img)
canvas.grid(column=0, row=1, pady=20, rowspan=4)

crop_button = Button(text="Crop Photo", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                     command=editor.crop)
crop_button.grid(column=3, row=1, padx=50)

resize_button = Button(text="Resize Photo", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                       command=editor.resize)
resize_button.grid(column=3, row=2, padx=50)

rotate_button = Button(text="Rotate Photo", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                       command=editor.rotate)
rotate_button.grid(column=3, row=3, padx=50)

convert_button = Button(text="Convert Photo", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                        command=editor.convert)
convert_button.grid(column=3, row=4, padx=50)

dominant_button = Button(text="Find Dominant Color", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                        command=editor.dominant)
dominant_button.grid(column=3, row=5, padx=50)

add_text_button = Button(text="Add Text to Photo", fg=editor.FONT_COLOR, bg=editor.BUTTON_COLOR, highlightthickness=0,
                         command=editor.add_text)
add_text_button.grid(column=3, row=0, padx=50)

root.mainloop()
