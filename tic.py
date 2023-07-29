from tkinter import *
import random
import time

def next_turn(row, column):
    global player
    
    if buttons[row][column]['text'] == '' and check_winner() is False:
        
        if player == players[0]:
            buttons[row][column]['text'] = player   
            
            if check_winner() is False:
                player = players[1]
                turn_label.config(text=players[1]+' Turn', bg = 'blue')
                
            elif check_winner() is True:
                turn_label.config(text =players[0]+ " Wins")
                
            elif check_winner() == "Tie!":
                turn_label.config(text = "Tie!")                
                
        else:
            buttons[row][column]['text'] = player   
            if check_winner() is False:
                player = players[0]
                turn_label.config(text=players[0]+' Turn', bg = 'red')
                
            elif check_winner() is True:
                turn_label.config(text = players[1]+" Wins")
                
            elif check_winner() == "Tie!":
                turn_label.config(text = "Tie!")          
            
        
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True
        
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg='green')
            buttons[1][1].config(bg='green')
            buttons[2][2].config(bg='green')
            return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg='green')
            buttons[1][1].config(bg='green')
            buttons[2][0].config(bg='green')
            return True

    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "Tie!"

    else:
        return False


def empty_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
            
    if spaces == 0:
        return False
    else:
        return True
    

def new_game():
    global player 
    player = random.choice(players)
    if player == 'X':
        turn_label.config(text = player+" turn", bg = 'red')
    else:
        turn_label.config(text = player+" turn", bg = 'blue')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='white')
    

window = Tk()
window.title('Tic Tac Toe')
window_width = 400
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2 - window_width/2)
y = int(screen_height/2 - window_height/2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

players = ['X', 'O']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

if player == 0:
    turn_label = Label(window, text = player + ' turn', font = ('Arial', 12), bg = 'red') 
else:
    turn_label = Label(window, text = player + ' turn', font = ('Arial', 12), bg = 'blue') 
    
turn_label.pack()

reset_button = Button(window, text = "Restart the game", font=('Arial', 12), command=new_game)
reset_button.pack(side='bottom')

frame = Frame(window, width = 10, height = 10)
frame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ('Arial', 12), width=6, height=3,
                                      command = lambda row = row, column = column:next_turn(row, column), bg='white')
        buttons[row][column].grid(row=row, column=column)

window.mainloop()