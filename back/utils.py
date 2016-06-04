def center_window(top_level, width, height):
    top_level.update_idletasks()

    w = top_level.winfo_screenwidth()
    h = top_level.winfo_screenheight()

    x = w / 2 - width / 2
    y = h * 9 / 20 - height / 2

    top_level.geometry("%dx%d+%d+%d" % (width, height, x, y))
