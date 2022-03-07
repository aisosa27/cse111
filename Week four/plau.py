# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
   
    scene_width = 800
    scene_height = 500

  
    canvas = start_drawing("Scene", scene_width, scene_height)

   



    finish_drawing(canvas)



main()