from enum import Enum


class Command(Enum):
    CROP = "crop"
    ROTATE = "rotate"
    RESIZE = "resize"
    CONVERT = "convert"
    ADD_TEXT = "add_text"
