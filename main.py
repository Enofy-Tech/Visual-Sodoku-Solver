import tkinter
from tkinter import *
from tkinter import PhotoImage
root=Tk()
root.title("Sudoku Solver")
root.geometry("325x500")
root.config(bg="#100e17")

tkinter.Button(root, text="Solve", font="Bahnschrift 20", bg="black", fg="white", activebackground="red", activeforeground="black",
               borderwidth=2, relief=tkinter.RAISED, cursor="hand2").place(x=10, y=300)

tkinter.Button(root, text="Enter", font="Bahnschrift 20", bg="black", fg="white", activebackground="red", activeforeground="black",
               borderwidth=2, relief=tkinter.RAISED, cursor="hand2").place(x=216, y=300)

tkinter.Button(root, text="Reset", font="Bahnschrift 20", bg="black", fg="white", activebackground="red", activeforeground="black",
               borderwidth=2, relief=tkinter.RAISED, cursor="hand2").place(x=216, y=400)

tkinter.Button(root, text="Generate", font="Bahnschrift 20", bg="black", fg="white", activebackground="red", activeforeground="black",
               borderwidth=2, relief=tkinter.RAISED, cursor="hand2").place(x=10, y=400)

label = Label(root, text="Fill the numbers in and to solve press SOLVE").grid(row=0, column=1, columnspan=10)

errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel= Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}

def ValidateNumber(P):
    out=(P.isdigit() or P=="") and len(P)<2
    return out

reg = root.register(ValidateNumber)


def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg= bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

def draw9x9Grd():
    color="#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color== "#D0ffff":
                color="#ffffd0"
            else:
                color="#D0ffff"


def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


def getValues():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = ""
            if val =="":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)


draw9x9Grd()
root.mainloop()