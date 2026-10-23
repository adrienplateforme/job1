def draw_rectangle(width,height):
    for x in range(height):
        if x == 0 or x == height - 1:
            print("|",(width - 2) * "-","|")
        else:
            print("|",(width - 2) * " ","|")


draw_rectangle(10,3)