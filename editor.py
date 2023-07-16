import os
from tkinter import Image, Label, Entry, Button, StringVar, OptionMenu, LEFT, filedialog, Toplevel, Tk
from tkinter.messagebox import showinfo

from PIL import Image, ImageDraw, ImageFont

from command import Command


class Editor:
    FILE_PATH = "./images/applogo.png"
    _SAVE_PATH = './images'
    BACKGROUND_COLOR = '#898121'
    FONT_COLOR = '#F7F1E5'
    BUTTON_COLOR = '#4C4B16'

    def __init__(self, root: Tk, status_label):
        self.angle_ent = None
        self.root = root
        self.status_label = status_label

    def _handler(self, command: Command):
        with Image.open(f"{self.FILE_PATH}") as img:
            edited_image = img
            match command:
                case Command.CROP:
                    left = int(self.left_ent.get())
                    upper = int(self.upper_ent.get())
                    right = int(self.right_ent.get())
                    lower = int(self.lower_ent.get())
                    edited_image = img.crop((left, upper, right, lower))
                case Command.ROTATE:
                    angle = int(self.angle_ent.get())
                    edited_image = img.rotate(angle=angle)
                case Command.RESIZE:
                    width = int(self.width_ent.get())
                    height = int(self.height_ent.get())
                    edited_image = img.resize((width, height))
                case Command.CONVERT:
                    selected_mode = self.clicked.get()
                    edited_image = img.convert(selected_mode)
                case Command.ADD_TEXT:
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.load_default()
                    draw.text((0, 0), self.text_ent.get(), (255, 255, 255), font=font)
                    img.show()
            edited_img_path = os.path.join(self._SAVE_PATH, f'{command.value}_img' + ".jpg")
            edited_image.save(edited_img_path)

    def crop(self):
        window = Toplevel(self.root)
        window.title("Photo Croper")
        window.geometry('600x300')
        window.config(bg=self.BACKGROUND_COLOR, padx=50, pady=50)
        left_lab = Label(window, text='Left crop value', bg=self.BACKGROUND_COLOR)
        left_lab.grid(row=0, column=0, pady=5)
        self.left_ent = Entry(window)
        self.left_ent.focus_set()
        self.left_ent.grid(row=0, column=1, padx=5, pady=5)
        upper_lab = Label(window, text='Upper crop value', bg=self.BACKGROUND_COLOR)
        upper_lab.grid(row=1, column=0, pady=5)
        self.upper_ent = Entry(window)
        self.upper_ent.grid(row=1, column=1, padx=5, pady=5)
        right_lab = Label(window, text='Right crop value', bg=self.BACKGROUND_COLOR)
        right_lab.grid(row=2, column=0, pady=5)
        self.right_ent = Entry(window)
        self.right_ent.grid(row=2, column=1, padx=5, pady=5)
        lower_lab = Label(window, text='Lower crop value', bg=self.BACKGROUND_COLOR)
        lower_lab.grid(row=3, column=0, pady=5)
        self.lower_ent = Entry(window)
        self.lower_ent.grid(row=3, column=1, padx=5, pady=5)
        notic_lab = Label(window, text='Keep in mind that the axis of these coordinates is at the top left (0,0).',
                          bg=self.BACKGROUND_COLOR)
        notic_lab.grid(row=4, column=0, columnspan=3, pady=5)
        submit_button = Button(window, text="Submit", fg=self.FONT_COLOR, bg=self.BUTTON_COLOR,
                               highlightthickness=0,
                               command=lambda: self._handler(Command.CROP))
        submit_button.grid(row=5, column=0, pady=5)

    def resize(self):
        window = Toplevel(self.root)
        window.title("Photo Resizer")
        window.geometry('600x300')
        window.config(bg=self.BACKGROUND_COLOR, padx=50, pady=50)
        width_lab = Label(window, text='Width value', bg=self.BACKGROUND_COLOR)
        width_lab.grid(row=0, column=0, pady=5)
        self.width_ent = Entry(window)
        self.width_ent.focus_set()
        self.width_ent.grid(row=0, column=1, padx=5, pady=5)
        height_lab = Label(window, text='Height value', bg=self.BACKGROUND_COLOR)
        height_lab.grid(row=1, column=0, pady=5)
        self.height_ent = Entry(window)
        self.height_ent.grid(row=1, column=1, padx=5, pady=5)
        notic_lab = Label(window, text='Keep in mind that the axis of these coordinates is at the top left (0,0).',
                          bg=self.BACKGROUND_COLOR)
        notic_lab.grid(row=2, column=0, columnspan=3, pady=5)
        submit_button = Button(window, text="Submit", fg=self.FONT_COLOR, bg=self.BUTTON_COLOR,
                               highlightthickness=0,
                               command=lambda: self._handler(Command.RESIZE))
        submit_button.grid(row=3, column=0, pady=5)

    def rotate(self):
        window = Toplevel(self.root)
        window.title("Photo Rotater")
        window.geometry('600x300')
        window.config(bg=self.BACKGROUND_COLOR, padx=50, pady=50)
        angle_lab = Label(window, text='angle value', bg=self.BACKGROUND_COLOR)
        angle_lab.grid(row=0, column=0, pady=5)
        self.angle_ent = Entry(window)
        self.angle_ent.focus_set()
        self.angle_ent.grid(row=0, column=1, padx=5, pady=5)
        notic_lab = Label(window, text='Keep in mind that Angle is in degrees counter clockwise',
                          bg=self.BACKGROUND_COLOR)
        notic_lab.grid(row=1, column=0, columnspan=3, pady=5)
        submit_button = Button(window, text="Submit", fg=self.FONT_COLOR, bg=self.BUTTON_COLOR,
                               highlightthickness=0,
                               command=lambda: self._handler(Command.ROTATE))
        submit_button.grid(row=2, column=0, pady=5)

    def convert(self):
        window = Toplevel(self.root)
        window.title("Photo Converter")
        window.geometry('600x300')
        window.config(bg=self.BACKGROUND_COLOR, padx=50, pady=50)
        mode_lab = Label(window, text='Mode', bg=self.BACKGROUND_COLOR)
        mode_lab.grid(row=0, column=0, pady=5)
        options = [
            '1',
            'L',
            'RGB',
            'CMYK',
            'YCbCr',
            'RGBX']
        self.clicked = StringVar()
        mode = OptionMenu(window, self.clicked, *options)
        mode.config(bg=self.BUTTON_COLOR)
        mode["menu"].config(bg=self.BUTTON_COLOR)
        mode.grid(row=0, column=1, pady=5)
        notic_lab = Label(window, text='1: 1-bit pixels, black and white, stored with one pixel per byte;\n'
                                       'L: 8-bit pixels, grayscale;\n'
                                       'RGB: 3x8-bit pixels, true color;\n'
                                       'CMYK: 4x8-bit pixels, color separation;\n'
                                       'YCbCr: 3x8-bit pixels, color video format;\n'
                                       'RGBX: true color with padding', anchor="e", justify=LEFT,
                          bg=self.BACKGROUND_COLOR)
        notic_lab.grid(row=2, column=0, columnspan=3, pady=5)
        submit_button = Button(window, text="Submit", fg=self.FONT_COLOR, bg=self.BUTTON_COLOR,
                               highlightthickness=0,
                               command=lambda: self._handler(Command.CONVERT))
        submit_button.grid(row=3, column=0, pady=5)

    def add_text(self):
        window = Toplevel(self.root)
        window.title("Add Text to Photo")
        window.geometry('600x300')
        window.config(bg=self.BACKGROUND_COLOR, padx=50, pady=50)
        text_lab = Label(window, text='Text', bg=self.BACKGROUND_COLOR)
        text_lab.grid(row=1, column=0, pady=5)
        self.text_ent = Entry(window)
        self.text_ent.grid(row=1, column=1, padx=5, pady=5)
        submit_button = Button(window, text="Submit", fg=self.FONT_COLOR, bg=self.BUTTON_COLOR,
                               highlightthickness=0,
                               command=lambda: self._handler(Command.ADD_TEXT))
        submit_button.grid(row=5, column=0, pady=5)

    def select_file(self):
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
        self.FILE_PATH = os.path.join(self._SAVE_PATH, file_name + ".jpg")
        with Image.open(file) as img:
            img.save(self.FILE_PATH)
        print('Selected:', file_name)
        self.status_label.config(text=f'{file_name} Selected')
