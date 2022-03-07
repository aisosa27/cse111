a
    'b!4  �                   @   s�   d Z ddlmZmZmZmZ ddlmZ dadd� Z	ddd	�d
d�Z
dddd�dd�Zdddddd�dd�Zdddd�dd�Zdddd�dd�Zdd�dd�Zdd� Zdd� Zdd � Zd!d"� Zed#kr�ds�J e� d$���d%S )&a�  
This is a library of drawing functions used by BYU-Idaho CSE 111
students to complete an assignment that draws an outdoor scene to a
window. The intent of the assignment is to teach students to separate a
large program into functions with parameters.

The functions in this library are simply wrapper functions that create
and use tkinter objects. The benefits provided by these wrapper
functions are as follows:
1. Elminate the need for students' code to call object-oriented canvas
   methods. Students' code calls functions instead of methods.
2. Simplify the options available to only those needed to complete the
   CSE 111 assignment.
3. Include type and value checking for the parameters passed to tkinter.

Advantages of tkinter over kivy
1. tkinter is installed as part of Python.
2. With tkinter colors are passed as part of the calls to create_oval,
   create_line, create_polygon, etc. which makes more sense to students
   than kivy where they are added to the canvas before a shape is added.
�    )�Tk�Frame�Canvas�BOTH)�NumberFc                 C   s�   t rJ d��t| t�s&J t| dd���d}d}t|t�sJJ t|dd|���t|t�sfJ t|dd|���||ks~J t|d|���||ks�J t|d|���t� }|�|� d|� �� t	� }|j
�| � |jtd	d
� t|�}|jtd	d
� |��  da |S )a'  Create a window with a canvas where a program can draw
    2-dimensional shapes.

    Parameters
        title: the title that will appear in the frame's title bar
        width: the width in pixels of the canvas
        height: the height in pixels of the canvas
    Return: the new canvas
    z.your program must call start_drawing once only�title�string�d   �width�number�height�x�   )�fillZexpandT)�_started�
isinstance�str�_wrong_typer   �_wrong_type_2�
_less_thanr   �geometryr   �masterr   Zpackr   r   �update)r   r
   r   �	min_width�
min_height�root�frame�canvas� r   �:/Users/doubradaunemigha/Desktop/CSE111/Week four/draw2d.py�start_drawing   s,    ��r    r   Zblack�r
   r   c          
      G   sj  t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|dd���tt|��D ]}t|| t�s�J d	��q�t|t�s�J t|d
dd���|dks�J t|d
d���t|t	��sJ t|dd���| �
� }	t|�}tdt|�d�D ]}|	||  ||< �q&| j||	| ||	| g|�R ||d�� dS )a-  Draw a that line goes through the series of points
        (x0, y0), (x1, y1), ... (xn, yn)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the line's width; default is 1 pixel
        fill: the line's color; default is black
    Return: nothing
    z>your program must call start_drawing before it calls draw_liner   r   �x0r   �y0�x1�y1� each coordinate must be a numberr
   r   r   r   r   �   r!   N)r   r   r   r   r   �range�lenr   r   r   �winfo_height�listZcreate_line)
r   r"   r#   r$   r%   r
   r   �args�ir   r   r   r   �	draw_lineJ   s(    
��r.   � �r
   �outliner   c          	   	   C   s"  t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|dd���t|t�s�J t|d	dd
���|d
ks�J t|d	d
���t|t�s�J t|dd���t|t�s�J t|dd���| �� }| j	||| ||| |||d� dS )a�  Draw an oval (ellipse) inside the bounding box defined by the
        coordinates (x0, y0), (x1, y1)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the oval's outline; default is 1 pixel
        outline: the color of the oval's outline; default is black
        fill: the color of the oval's interior; default is "" which
            means transparent
    Return: nothing
    z>your program must call start_drawing before it calls draw_ovalr   r   r"   r   r#   r$   r%   r
   r   r1   r   r   r0   N)
r   r   r   r   r   r   r   r   r*   Zcreate_oval�	r   r"   r#   r$   r%   r
   r1   r   r   r   r   r   �	draw_ovali   s     ��r3   �Z   ��start�extentr
   r1   r   c                C   s^  t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|dd���t|t�s�J t|d	d���t|t�s�J t|d
d���t|t�s�J t|ddd���|dks�J t|dd���t|t��sJ t|dd���t|	t��s.J t|	dd���| �� }
| j	||
| ||
| |||||	d�	 dS )a4  Draw a wedge shaped slice taken from an oval (ellipse) defined by
        the bounding box coordinates (x0, y0), (x1, y1).

    Parameters
        canvas: the canvas returned from the start_drawing function
        start: starting angle for the slice, in degrees, measured
            counterclockwise from the positive x axis; default is
            0 degrees.
        extent: width of the slice in degrees; default is 90 degrees.
            The slice starts at the angle given by the start parameter
            and extends counterclockwise for extent degrees.
        width: the width of the oval's outline; default is 1 pixel
        outline: the color of the oval's outline; default is black
        fill: the color of the oval's interior; default is "" which
            means transparent
    Return: nothing
    z=your program must call start_drawing before it calls draw_arcr   r   r"   r   r#   r$   r%   r6   r7   r
   r   r1   r   r   r5   N)
r   r   r   r   r   r   r   r   r*   Z
create_arc)r   r"   r#   r$   r%   r6   r7   r
   r1   r   r   r   r   r   �draw_arc�   s&    ��r8   c          	   	   C   s"  t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|dd���t|t�s�J t|d	dd
���|d
ks�J t|d	d
���t|t�s�J t|dd���t|t�s�J t|dd���| �� }| j	||| ||| |||d� dS )a�  Draw a rectangle with two corners at (x0, y0), (x1, y1)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the rectangle's outline; default is 1 pixel
        outline: the color of the rectangle's outline; default is black
        fill: the color of the rectangle's interior; default is "" which
            means transparent
    Return: nothing
    zCyour program must call start_drawing before it calls draw_rectangler   r   r"   r   r#   r$   r%   r
   r   r1   r   r   r0   N)
r   r   r   r   r   r   r   r   r*   Zcreate_rectangler2   r   r   r   �draw_rectangle�   s     ��r9   c                G   s�  t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|dd���t|t�s�J t|d	d���t|t�s�J t|d
d���tt|
��D ]}t|
| t�s�J d��q�t|t��sJ t|ddd���|dk�s"J t|dd���t|t	��s>J t|dd���t|	t	��sZJ t|	dd���| �
� }t|
�}
tdt|
�d�D ]}||
|  |
|< �qz| j||| ||| ||| g|
�R |||	d�� dS )ac  Draw a polygon with vertices (x0, y0), (x1, y1), ... (xn, yn).
    The polygon is always a closed polygon the same quantity of segments
    as vertices. In other words, the segments are defined as follows:
    (x0, y0) -> (x1, y1) -> ... -> (xn, yn) -> (x0, y0)

    Parameters
        canvas: the canvas returned from the start_drawing function
        width: the width of the polygon's outline; default is 1 pixel
        outline: the color of the polygon's outline; default is black
        fill: the color of the polygon's interior; default is "" which
            means transparent
    Return: nothing
    zAyour program must call start_drawing before it calls draw_polygonr   r   r"   r   r#   r$   r%   �x2�y2r&   r
   r   r1   r   r   r   r'   r0   N)r   r   r   r   r   r(   r)   r   r   r   r*   r+   Zcreate_polygon)r   r"   r#   r$   r%   r:   r;   r
   r1   r   r,   r-   r   r   r   r   �draw_polygon�   s2    ���r<   )r   c                C   s�   t sJ d��t| t�s&J t| dd���t|t�s@J t|dd���t|t�sZJ t|dd���t|t�stJ t|dd���t|t�s�J t|d	d���| �� }| j||| ||d
� dS )a  Draw text with the center of the text at (center_x, center_y).

    Parameters
        canvas: the canvas returned from the start_drawing function
        text: the text to be drawn. To force a line break, include a
            newline character ("
").
    Return: nothing
    z>your program must call start_drawing before it calls draw_textr   r   �center_xr   �center_y�textr   r   )r?   r   N)r   r   r   r   r   r   r*   Zcreate_text)r   r=   r>   r?   r   r   r   r   r   �	draw_text�   s    	�
�
�r@   c                 C   s2   t sJ d��t| t�s&J t| dd���| ��  dS )z�Call all functions that are necessary to display
    the drawing on the computer's monitor.

    Parameters
        canvas: the canvas returned from the start_drawing function
    Return: nothing
    zCyour program must call start_drawing before it calls finish_drawingr   r   N)r   r   r   r   Zmainloop)r   r   r   r   �finish_drawing	  s
    �rA   c                 C   s    d|� d|� dt | �� d|� �S )Nzwrong data type for parameter z; z is a z but must be a )�type)�param�name�expectedr   r   r   r     s    ���r   c                 C   s   t | ||�d|� � S )Nz greater than or equal to )r   )rC   rD   rE   �minimumr   r   r   r   #  s    
�r   c                 C   s   d|� d| � d�S )Nz
parameter z is z/ but must be greater than or equal to {minimum}r   )rC   rD   rF   r   r   r   r   (  s    r   �__main__z� is not a program. It is a library of functions that draw 2-dimensional shapes to a canvs in a computer window. You are not supposed to run this file but instead import its functions into your program and run your program.N)�__doc__Ztkinterr   r   r   r   �numbersr   r   r    r.   r3   r8   r9   r<   r@   rA   r   r   r   �__name__�__file__r   r   r   r   �<module>   s,   + �
�(��'�