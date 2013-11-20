__author__ = 'tim mcguire'
import datetime
import math
import Tkinter
import sys,os

def to_binary(dec, width):
    x = width - 1
    answer = ""

    while x >= 0:
        current_power = math.pow(2, x)
        # how many powers of two fit into dec?
        how_many = int(dec / current_power)
        answer += str(how_many)
        dec -= how_many * current_power
        x -= 1
    return answer


def fill_dots(times_to_use, x,length):

    tup = tens_and_ones(times_to_use)
    for num in tup:
        binary_string = to_binary(num, length)
        length =4
        x += right_step
        y = start_y
        for bit in reversed(binary_string):
            coord = x, y, x + dot_size, y + dot_size
            if bit == '1':
                main_canvas.create_oval(coord, fill="red")
            else:
                main_canvas.create_oval(coord, fill="blue")
            y -= 15

    return x

def tens_and_ones(num):
    tens = int(num / 10)
    ones = num % 10
    return tens, ones

def run(master):

    t = datetime.datetime.now()
    time_collection = t.hour, t.minute, t.second
    x = 15
    length =2
    for val in time_collection:
        # val is the numeric value, x is horizontal offset, length is how many dots tall the stack will be
        x = fill_dots(val, x,length)
        length =3
    main_canvas.pack()
    main_canvas.after(200, run, master)


time_format = sys.argv[1]
start_y = 150
right_step = 20
dot_size = 15

root = Tkinter.Tk()
root.geometry('300x200')
main_canvas = Tkinter.Canvas(root, bg="blue", height=300, width=200)

run(main_canvas)
root.mainloop()