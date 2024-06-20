from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line, "black")
    win.wait_for_close()

main()