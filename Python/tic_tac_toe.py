#github - akrishna5

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('Tic-Tac-Toe')

clicked = True
count = 0

def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red", fg = "white")
        b2.config(bg="red", fg = "white")
        b3.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations Player 1 !\n You Won!!")
        disable_buttons()

    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b6.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations Player 1 !\n You Won!!")
        disable_buttons()

    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red", fg = "white")
        b8.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations Player 1 !\n You Won!!")
        disable_buttons()

    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red", fg = "white")
        b4.config(bg="red", fg = "white")
        b7.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations Player 1 !\n You Won!!")
        disable_buttons()

    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b8.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red", fg = "white")
        b6.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b7.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    #Check for O's win

    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red", fg = "white")
        b2.config(bg="red", fg = "white")
        b3.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b6.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red", fg = "white")
        b8.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red", fg = "white")
        b4.config(bg="red", fg = "white")
        b7.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b8.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red", fg = "white")
        b6.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b9.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red", fg = "white")
        b5.config(bg="red", fg = "white")
        b7.config(bg="red", fg = "white")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations player 1 !\n You Won!!")
        disable_buttons()

    elif count==9 and winner== False:
        messagebox.showinfo("Tic-Tac-Toe", " Tie!!")
        disable_buttons()

def b_click(b):
    global clicked, count
    if b["text"]== " " and clicked==True:
        b["text"]="X"
        clicked= False
        count+=1
        checkifwon()

    elif b["text"]== " " and clicked==False:
        b["text"]="O"
        clicked= True
        count+=1
        checkifwon() 
    else:
        messagebox.showerror("Tic-Tac-Toe", "Already Selected!")

def reset():
#create buttons
    global b1, b2, b3, b4, b5, b6 , b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b1))
    b2= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b2))
    b3= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b3))

    b4= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b4))
    b5= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b5))
    b6= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b6))

    b7= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b7))
    b8= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b8))
    b9= Button(root, text=" ", height=3, width=6, font=("helvetica", 20), bg= "SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row =0 , column=0)
    b2.grid(row = 0, column=1)
    b3.grid(row = 0, column=2)

    b4.grid(row = 1, column=0)
    b5.grid(row = 1, column=1)
    b6.grid(row = 1, column=2)

    b7.grid(row = 2, column=0)
    b8.grid(row = 2, column=1)
    b9.grid(row = 2, column=2)

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu= Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)

reset()

root.mainloop()
# print("Namste Duniya")

def sum(a, b, c):
    return a + b + c


def printBoard(xState, zState):
    one = 'X' if xState[1] else ('0' if zState[1] else 1)
    two = 'X' if xState[2] else ('0' if zState[2] else 2)
    three = 'X' if xState[3] else ('0' if zState[3] else 3)
    four = 'X' if xState[4] else ('0' if zState[4] else 4)
    five = 'X' if xState[5] else ('0' if zState[5] else 5)
    six = 'X' if xState[6] else ('0' if zState[6] else 6)
    senven = 'X' if xState[7] else ('0' if zState[7] else 7)
    eight = 'X' if xState[8] else ('0' if zState[8] else 8)
    nine = 'X' if xState[9] else ('0' if zState[9] else 9)
    print(f"{one} | {two} | {three} ")
    print(f"--|---|---")
    print(f"{four} | {five} | {six} ")
    print(f"--|---|---")
    print(f"{senven} | {eight} | {nine} ")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X's win")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O's win")
            return 0
    return -1
    


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1for X and for 0
    print("Welcome to tic tac toe")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("0's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Match Over")
            break
        
        turn = 1 - turn

