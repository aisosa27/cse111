import tkinter as tk
def main():
        # The width and height of the scene window.
        width = 800
        height = 500
        # Create the Tk root object.
        root = tk.Tk()
        root.geometry(f"{width}x{height}")
        # Create a Frame object.
        frame = tk.Frame(root)
        frame.master.title("Scene")
        frame.pack(fill=tk.BOTH, expand=1)
        # Create a canvas object that will draw into the frame.
        canvas = tk.Canvas(frame)
        canvas.pack(fill=tk.BOTH, expand=1)
        # Call the draw_scene function.
        draw_scene(canvas, 0, 0, width-1, height-1)
        root.mainloop()
def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
        #print (scene_left, scene_top, scene_right, scene_bottom) = 0 0 799 499
        draw_sky(canvas, scene_left, scene_right, 1)
        tree_center = scene_left + 450
        tree_top = scene_top + 100
        tree_height = 400
        draw_mountain(canvas, 499, 550, 750, 200, 799, 250, 799, 499)
        draw_cloud(canvas, 50, 110, 150, 170)
        draw_cloud(canvas, 75, 125, 200, 75)
        draw_pine_tree(canvas, tree_center, tree_top, tree_height)
        tree_center = scene_left + 100
        tree_top = scene_top + 200
        tree_height = 300
        draw_pine_tree(canvas, tree_center, tree_top, tree_height)
        tree_center = scene_left + 750
        tree_top = scene_top + 300
        tree_height = 200
        #Draw moon
        draw_moon(canvas, 700, 50)
        #Draw stars
        draw_star(canvas, 25, 25)
        draw_star(canvas, 200, 250)
        draw_star(canvas, 350, 350)
        draw_star(canvas, 210, 20)
        draw_star(canvas, 180, 180)
        draw_star(canvas, 200, 125)
        draw_star(canvas, 400, 250)
        draw_star(canvas, 300, 75)
        draw_star(canvas, 640, 120)
        draw_star(canvas, 480, 90)
        draw_star(canvas, 710, 40)
        draw_star(canvas, 525, 100)
        draw_star(canvas, 600, 80)
        #Draw grid for guidance
        #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 50)
def draw_cloud(canvas, x, y, x1, y1):
        #Dram cloud
        canvas.create_oval(x, y, x1, y1, fill="gray64", width=0)
def draw_mountain(canvas, x, y, x1, y1, x2, y2, x3, y3):
        #Draw mountain
        canvas.create_polygon(x, y, x1, y1, x2, y2, x3, y3, fill="gray20", width=0)
def draw_star(canvas, x, y):
        #Draw star
        canvas.create_oval(x, y, x + 5, y + 5, fill="gold", width=0)
def draw_sky(canvas, scene_left, scene_right, grid_spacing):
        #Draw vertical lines
        for i in range(scene_left, scene_right, grid_spacing):
            canvas.create_line(i, scene_left, i, scene_right, fill="midnightBlue")
def draw_moon(canvas, x, y):
        canvas.create_oval(x, y, x + 75, y + 75, fill="lightGray", width=0)
def draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom,
    grid_spacing):
        margin_value_1 = 10
        margin_value_2 = 15
        #Draw horizontal lines
        for i in range(scene_top, scene_bottom, grid_spacing):
            canvas.create_line(scene_left, i, scene_right, i)
            canvas.create_text(scene_left + margin_value_2, i + margin_value_1,
    text=f"{i}", fill="white")
        #Draw vertical lines
        for i in range(scene_left, scene_right, grid_spacing):
            canvas.create_line(i, scene_left, i, scene_right)
            canvas.create_text(i + margin_value_2, scene_left + margin_value_1,
    text=f"{i}", fill="white")
def draw_pine_tree(canvas, x, y, h):
        tw = h / 10
        th = h / 8
        tl = x - tw / 2
        tr = x + tw / 2
        tb = y + h
        sw = h / 2
        sh = h - th
        sl = x - sw / 2
        sr = x + sw / 2
        sb = y + sh
        # Draw the trunk of the pine tree.
        canvas.create_rectangle(tl, sb,
tr, tb,
                outline="gray20", width=1, fill="tan4")
        # Draw the crown (also called skirt) of the pine tree.
        canvas.create_polygon(x, y,
                sr, sb,
                sl, sb,
                outline="gray20", width=1, fill="darkOrange3")
    # Call the main function so that
    # this program will start executing.
main()