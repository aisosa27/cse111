

from tkinter import Tk, Frame, Canvas, BOTH
from numbers import Number

_started = False


def start_drawing(title, width, height):
    
    global _started
    assert not _started, "your program must call start_drawing once only"
    assert isinstance(title, str), _wrong_type(title, "title", "string")
    min_width = 100
    min_height = 100
    assert isinstance(width, Number), \
        _wrong_type_2(width, "width", "number", min_width)
    assert isinstance(height, Number), \
        _wrong_type_2(height, "height", "number", min_height)
    assert width >= min_width,  _less_than(width, "width", min_width)
    assert height >= min_height, _less_than(height, "height", min_height)

    # Create the root Tk object.
    root = Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = Frame()
    frame.master.title(title)
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Call canvas.update to update the stored width and height
    # with the actual width and height after packing.
    canvas.update()

    _started = True
    return canvas


def draw_line(canvas, x0, y0, x1, y1, *args, width=1, fill="black"):
    
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    for i in range(len(args)):
        assert isinstance(args[i], Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(fill, str), _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    args = list(args)
    for i in range(1, len(args), 2):
        args[i] = height - args[i]
    canvas.create_line(x0, height-y0, x1, height-y1, *args,
            width=width, fill=fill)


def draw_oval(canvas, x0, y0, x1, y1, *,
        width=1, outline="black", fill=""):
   
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_oval(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_arc(canvas, x0, y0, x1, y1, *,
        start=0, extent=90, width=1, outline="black", fill=""):
    
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(start, Number),  _wrong_type(start, "start", "number")
    assert isinstance(extent, Number), _wrong_type(extent, "extent", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_arc(x0, height-y0, x1, height-y1,
            start=start, extent=extent,
            width=width, outline=outline, fill=fill)


def draw_rectangle(canvas, x0, y0, x1, y1, *,
        width=1, outline="black", fill=""):

    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_rectangle(x0, height-y0, x1, height-y1,
            width=width, outline=outline, fill=fill)


def draw_polygon(canvas, x0, y0, x1, y1, x2, y2, *args,
        width=1, outline="black", fill=""):
    
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(x0, Number), _wrong_type(x0, "x0", "number")
    assert isinstance(y0, Number), _wrong_type(y0, "y0", "number")
    assert isinstance(x1, Number), _wrong_type(x1, "x1", "number")
    assert isinstance(y1, Number), _wrong_type(y1, "y1", "number")
    assert isinstance(x2, Number), _wrong_type(x2, "x2", "number")
    assert isinstance(y2, Number), _wrong_type(y2, "y2", "number")
    for i in range(len(args)):
        assert isinstance(args[i], Number), "each coordinate must be a number"
    assert isinstance(width, Number), _wrong_type_2(width, "width", "number", 0)
    assert width >= 0, _less_than(width, "width", 0)
    assert isinstance(outline, str), _wrong_type(outline, "outline", "string")
    assert isinstance(fill, str),    _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    args = list(args)
    for i in range(1, len(args), 2):
        args[i] = height - args[i]
    canvas.create_polygon(x0, height-y0, x1, height-y1, x2, height-y2,
            *args, width=width, outline=outline, fill=fill)


def draw_text(canvas, center_x, center_y, text, *, fill="black"):
    
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    assert isinstance(center_x, Number), \
        _wrong_type(center_x, "center_x", "number")
    assert isinstance(center_y, Number), \
        _wrong_type(center_y, "center_y", "number")
    assert isinstance(text, str), _wrong_type(text, "text", "string")
    assert isinstance(fill, str), _wrong_type(fill, "fill", "string")

    height = canvas.winfo_height()
    canvas.create_text(center_x, height-center_y, text=text, fill=fill)


def finish_drawing(canvas):
   
    assert _started
    assert isinstance(canvas, Canvas), _wrong_type(canvas, "canvas", "Canvas")
    canvas.mainloop()


def _wrong_type(param, name, expected):
    # Of course, it's possible to rewrite this function so that it
    # includes an assertion statement which would make less code in this
    # file. Unfortunately, placing the assert in this function adds
    # another level to the stack trace that is printed when the computer
    # raises an AssertionError. It's best not to have the additional
    # level in the stack trace because the error messages in this file
    # are for students.
    return f"wrong data type for parameter {name};" \
        f" {name} is a {type(param)} but must be a {expected}"


def _wrong_type_2(param, name, expected, minimum):
    return _wrong_type(param, name, expected) + \
        f" greater than or equal to {minimum}"


def _less_than(param, name, minimum):
    return f"parameter {name} is {param}" \
        " but must be greater than or equal to {minimum}"


if __name__ == "__main__":
    assert False, \
    f"{__file__} is not a program. It is a library of functions that" \
    " draw 2-dimensional shapes to a canvs in a computer window. You" \
    " are not supposed to run this file but instead import its" \
    " functions into your program and run your program."
