import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

from PIL import Image, ImageDraw, ImageFont

BACKGROUND_COLOR = '#898121'
FONT_COLOR = '#F7F1E5'
BUTTON_COLOR = '#4C4B16'
COLOR = '#E7B10A'
file_path = "./images/applogo.png"
save_path = './images'


def select_file():
    global file_path
    filetypes = (
        ('text files', '*.jpg'),
        ('text files', '*.png'),
        ('text files', '*.jpeg'),
        ('text files', '*.gif'),
        ('text files', '*.tiff'),
        ('All files', '*.*'))

    file = filedialog.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    filelist = file.split('/')
    file_name = filelist[len(filelist) - 1].split('.')[0]
    showinfo(
        title='Selected Files',
        message=file)
    file_path = os.path.join(save_path, file_name + ".jpg")
    img = Image.open(file)
    img.save(file_path)
    print('Selected:', file_name)
    status_label.config(text=f'{file_name} Selected')


def crop():
    def save_crop_parameters():
        left = int(left_ent.get())
        upper = int(upper_ent.get())
        right = int(right_ent.get())
        lower = int(lower_ent.get())
        img = Image.open(f"{file_path}")
        croped_img = img.crop((left, upper, right, lower))
        croped_img_path = os.path.join(save_path, "croped_img" + ".jpg")
        croped_img.save(croped_img_path)
        print('Croped:', croped_img_path)

    window = tkinter.Toplevel(root)
    window.title("Photo Croper")
    window.geometry('600x300')
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    left_lab = Label(window, text='Left crop value', bg=BACKGROUND_COLOR)
    left_lab.grid(row=0, column=0, pady=5)
    left_ent = Entry(window)
    left_ent.focus_set()
    left_ent.grid(row=0, column=1, padx=5, pady=5)
    upper_lab = Label(window, text='Upper crop value', bg=BACKGROUND_COLOR)
    upper_lab.grid(row=1, column=0, pady=5)
    upper_ent = Entry(window)
    upper_ent.grid(row=1, column=1, padx=5, pady=5)
    right_lab = Label(window, text='Right crop value', bg=BACKGROUND_COLOR)
    right_lab.grid(row=2, column=0, pady=5)
    right_ent = Entry(window)
    right_ent.grid(row=2, column=1, padx=5, pady=5)
    lower_lab = Label(window, text='Lower crop value', bg=BACKGROUND_COLOR)
    lower_lab.grid(row=3, column=0, pady=5)
    lower_ent = Entry(window)
    lower_ent.grid(row=3, column=1, padx=5, pady=5)
    notic_lab = Label(window, text='Keep in mind that the axis of these coordinates is at the top left (0,0).',
                      bg=BACKGROUND_COLOR)
    notic_lab.grid(row=4, column=0, columnspan=3, pady=5)
    submit_button = Button(window, text="Submit", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                           command=save_crop_parameters)
    submit_button.grid(row=5, column=0, pady=5)


def resize():
    def save_resize_parameters():
        width = int(width_ent.get())
        height = int(height_ent.get())
        img = Image.open(f"{file_path}")
        resized_img = img.resize((width, height))
        resized_img_path = os.path.join(save_path, "resized_img" + ".jpg")
        resized_img.save(resized_img_path)
        print('Resized:', resized_img_path)

    window = tkinter.Toplevel(root)
    window.title("Photo Resizer")
    window.geometry('600x300')
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    width_lab = Label(window, text='Width value', bg=BACKGROUND_COLOR)
    width_lab.grid(row=0, column=0, pady=5)
    width_ent = Entry(window)
    width_ent.focus_set()
    width_ent.grid(row=0, column=1, padx=5, pady=5)
    height_lab = Label(window, text='Height value', bg=BACKGROUND_COLOR)
    height_lab.grid(row=1, column=0, pady=5)
    height_ent = Entry(window)
    height_ent.grid(row=1, column=1, padx=5, pady=5)
    notic_lab = Label(window, text='Keep in mind that the axis of these coordinates is at the top left (0,0).',
                      bg=BACKGROUND_COLOR)
    notic_lab.grid(row=2, column=0, columnspan=3, pady=5)
    submit_button = Button(window, text="Submit", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                           command=save_resize_parameters)
    submit_button.grid(row=3, column=0, pady=5)


def rotate():
    def save_rotate_parameters():
        angle = int(angle_ent.get())
        img = Image.open(f"{file_path}")
        rotated_img = img.rotate(angle=angle)
        rotated_img_path = os.path.join(save_path, "rotated_img" + ".jpg")
        rotated_img.save(rotated_img_path)
        print('Rotated:', rotated_img_path)

    window = tkinter.Toplevel(root)
    window.title("Photo Rotater")
    window.geometry('600x300')
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    angle_lab = Label(window, text='angle value', bg=BACKGROUND_COLOR)
    angle_lab.grid(row=0, column=0, pady=5)
    angle_ent = Entry(window)
    angle_ent.focus_set()
    angle_ent.grid(row=0, column=1, padx=5, pady=5)
    notic_lab = Label(window, text='Keep in mind that Angle is in degrees counter clockwise', bg=BACKGROUND_COLOR)
    notic_lab.grid(row=1, column=0, columnspan=3, pady=5)
    submit_button = Button(window, text="Submit", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                           command=save_rotate_parameters)
    submit_button.grid(row=2, column=0, pady=5)


def convert():
    def save_convert_parameters():
        selected_mode = clicked.get()
        img = Image.open(f"{file_path}")
        converted_img = img.convert(selected_mode)
        converted_img_path = os.path.join(save_path, "converted_img" + ".jpg")
        converted_img.save(converted_img_path)
        print('Converted:', converted_img_path)

    window = tkinter.Toplevel(root)
    window.title("Photo Converter")
    window.geometry('600x300')
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    mode_lab = Label(window, text='Mode', bg=BACKGROUND_COLOR)
    mode_lab.grid(row=0, column=0, pady=5)
    options = [
        '1',
        'L',
        'RGB',
        'CMYK',
        'YCbCr',
        'RGBX']
    clicked = StringVar()
    mode = OptionMenu(window, clicked, *options)
    mode.config(bg=BUTTON_COLOR)
    mode["menu"].config(bg=BUTTON_COLOR)
    mode.grid(row=0, column=1, pady=5)
    notic_lab = Label(window, text='1: 1-bit pixels, black and white, stored with one pixel per byte;\n'
                                   'L: 8-bit pixels, grayscale;\n'
                                   'RGB: 3x8-bit pixels, true color;\n'
                                   'CMYK: 4x8-bit pixels, color separation;\n'
                                   'YCbCr: 3x8-bit pixels, color video format;\n'
                                   'RGBX: true color with padding', anchor="e", justify=LEFT, bg=BACKGROUND_COLOR)
    notic_lab.grid(row=2, column=0, columnspan=3, pady=5)
    submit_button = Button(window, text="Submit", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                           command=save_convert_parameters)
    submit_button.grid(row=3, column=0, pady=5)


def add_text():
    def save_text_parameters():
        img = Image.open(f"{file_path}")
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((0, 0), text_ent.get(), (255, 255, 255), font=font)
        img.show()

        # img_with_text_path = os.path.join(save_path, "Filtered_img" + ".jpg")
        # img_with_text.save(img_with_text_path)
        # print('Image with Text:', img_with_text_path)

    window = tkinter.Toplevel(root)
    window.title("Add Text to Photo")
    window.geometry('600x300')
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    text_lab = Label(window, text='Text', bg=BACKGROUND_COLOR)
    text_lab.grid(row=1, column=0, pady=5)
    text_ent = Entry(window)
    text_ent.grid(row=1, column=1, padx=5, pady=5)
    submit_button = Button(window, text="Submit", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                           command=save_text_parameters)
    submit_button.grid(row=5, column=0, pady=5)


# GUI Creation
root = tkinter.Tk()
root.title("Photo Editor")
root.geometry('500x450+50+50')
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
select_files_button = Button(text="select_file", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                             command=select_file)
select_files_button.grid(column=0, row=0)
canvas = Canvas(width=223, height=223, bg=COLOR, highlightthickness=0)
selected_img = PhotoImage(file=file_path)
background = canvas.create_image(110, 110, image=selected_img)
canvas.grid(column=0, row=1, pady=20, rowspan=4)

status_label = Label(text='Please select an image:')
status_label.grid(column=0, row=5, pady=20)

crop_button = Button(text="Crop Photo", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0, command=crop)
crop_button.grid(column=3, row=1, padx=50)

resize_button = Button(text="Resize Photo", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0, command=resize)
resize_button.grid(column=3, row=2, padx=50)

rotate_button = Button(text="Rotate Photo", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0, command=rotate)
rotate_button.grid(column=3, row=3, padx=50)

convert_button = Button(text="Convert Photo", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0, command=convert)
convert_button.grid(column=3, row=4, padx=50)

add_text_button = Button(text="Add Text to Photo", fg=FONT_COLOR, bg=BUTTON_COLOR, highlightthickness=0,
                         command=add_text)
add_text_button.grid(column=3, row=0, padx=50)

root.mainloop()
