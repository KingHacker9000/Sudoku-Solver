# ------Imports------
import tkinter as tk
import time
#--------------------

# Initialize Empty Board
Board = [
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""]
]

# Button Function: Find Empty Spaces and Mark Them
def complete():

    # Cycle Through All Entries
    for entry in range(len(Entries)):

        # Find Column And Row Values
        col = entry // 9
        row = entry % 9

        # Check if Entry is Empty; if yes: Mark Value as Empty
        if Entries[entry].get() == "":
            value = ""

        # if not: Mark Its Value And Append To Green Array for Color Coding
        else:
            value = int(Entries[entry].get())
            Green.append(entry)

        # Append These Value to Values Array
        Values.append((value, row, col))

    # Call Next Function
    AddValues()

# Enter Values into Board
def AddValues():

    # For Every Value in The Array place The value into The corresponding Board Location
    for value in range(len(Values)):

        Board[Values[value][1]][Values[value][2]] = Values[value][0]

    Complete()


# Main Function: Print Original, Call Solve Function, Print Result
def Complete():

    print_board(Board)
    solve(Board)
    print_board(Board)


# Prints The 2D Board Array in Terminal / Console
def print_board(board):
    print(("____" * 10) + "_")    # print Top Line

    # For Each Spot On the 2D Array
    for row in range(len(board)):

        for column in range(len(board[row])):

            value = board[row][column]    # Put value of Spot in a Temporary Variable value

            # if value is not empty Then Put tHe Value along with a Line
            if value != "":
                print(" | " + str(value), end="")
            # else Put an Empty String
            else:
                print(" | " + " ", end="")

            # if it is the 3rd Value The put a Line After Value To Separate Blocks
            if (column + 1) % 3 == 0 and column != 0:
                print(" | ", end="")

        # if it is the 3rd row, then add a line after to separate blocks
        if (row + 1) % 3 == 0 and row != 0:
            print("\n" + ("____" * 10) + "_")
        # else Skip to next line
        else:
            print("")

# Checks if Value Given is Valid
def valid(board, value, Valrow, Valcol):

    # Check its row if it is a Valid Move
    for row in range(len(board)):

        # if The Same No is Found Then Return False
        if board[row][Valcol] == value and row != Valrow:
            return False

    # Check its Column if it is a Valid Move
    for col in range(len(board)):

        # if The Same No is Found Then Return False
        if board[Valrow][col] == value and col != Valcol:
            return False

    bl_x = Valcol // 3
    bl_y = Valrow // 3

    # Find Block No
    block = [bl_y, bl_x]

    # Check Each Value in Block
    for i in range(block[0] * 3, (block[0] * 3) + 3):

        for j in range(block[1] * 3, (block[1] * 3) + 3):

            # if The Same No is Found Then Return False
            if board[i][j] == value and [i, j] != [Valrow, Valcol]:
                return False

    # if The Same No is NOT Found in any Row, Column, Block Then It is Valid : Return True
    return True


# Solve The Board
def solve(board):

    # Find an Empty Value
    Empties = find_empty(board)

    # if There are No Empties hence The Board is Complete we can return True
    if Empties[0]:
        return True

    # else Run Through all Possible Nos.
    else:
        for num in range(1, 10):

            board[Empties[1]][Empties[2]] = num

            #  And Check if it is a Valid Option; if it is Then Run it again and Solve for next Empty
            if valid(board, num, Empties[1], Empties[2]):
                Update(board)
                stay_green()
                root.update()    # Update GUI
                solve(board)     # Call Function again for next Empty

                # if there is no Empty then return
                if find_empty(board)[0]:
                    return True

        # BackTrack
        board[Empties[1]][Empties[2]] = ""


# finds the next Empty Spot on Board
def find_empty(board):

    for row in range(len(board)):
        for column in range(len(board[row])):

            # if an Empty is Found then return a tuple of False, row, column
            if board[row][column] == "":
                pos = (False, row, column)
                return pos

    # if no Empty found the return a Tuple of True, 0
    pos = (True, 0)
    return pos

# Color Filled Entries as Green
def stay_green():

    for green in range(len(Green)):

        entry = Green[green]
        Entries[entry].configure(foreground="green")


# Color Empty Entries as Red
def Update(board):

    for entry in range(len(Entries)):

        if Entries[entry] != "":
            Entries[entry].delete(0)
            col = entry // 9
            row = entry % 9
            val = board[row][col]
            Entries[entry].insert(0, val)
            Entries[entry].configure(foreground="red")


# Array of all Values
Values = []
#  Array of all Inputted Values
Green = []


# Tkinter GUI
root = tk.Tk()
root.title("Sudoku Solver")
root.iconbitmap(r"Sudoku_Icon.ico")

# Create a Board Canvas
BoardGrid = tk.Canvas(root, height=450, width=450, bg='white')
BoardGrid.grid(row=0, column=0)

Entries = []

# Creates a Grid
for rows in range(0, 450, 50):
    if rows % 3 == 0:
        BoardGrid.create_line(0, rows, 450, rows, fill="black", width=4)
    else:
        BoardGrid.create_line(0, rows, 450, rows, fill="grey", width=2)

for columns in range(0, 450, 50):
    if columns % 3 == 0:
        BoardGrid.create_line(columns, 0, columns, 450, fill="black", width=4)
    else:
        BoardGrid.create_line(columns, 0, columns, 450, fill="grey", width=2)


# creates Entries
for columns in range(0, 450, 50):
    for rows in range(0, 450, 50):
        e = tk.Entry(BoardGrid, width=6, justify='center', font="Helvetica 15 bold")
        e.place(x=columns, y=rows, height=45)
        Entries.append(e)

# Create a Button and Canvas
Base = tk.Canvas(root, height=75, width=450, bg='light gray')
Base.grid(row=1, column=0)

playButton = tk.Button(Base, text="Auto-Complete!  😇", command=complete)
playButton.pack(ipady=5)

root.mainloop()

# --------END----------#
