from tkinter import *
from tkinter.messagebox import showinfo
from xml.dom.minidom import Element


root = Tk()

root.title("XO_game")
title = Label(root,text="!!! XO_game !!!",font = ("ALGERIAN",80), foreground="red",background="black",padx=100,pady=20)
title.grid(row=1,column=2,columnspan=60)
root.configure(background="#66ff66")


a = Label(root,background="#66ff66")
a.grid(row=2,column=3,padx=100,pady=30)


player_1 = Label(root,text="player_1 : 'X'",font = ("ALGERIAN",30), foreground="red",background="black")
player_1.grid(row=3,column=1)

player_2 = Label(root,text="player_2 : 'O",font = ("ALGERIAN",30), foreground="red",background="black")
player_2.grid(row=3,column=62)

y = ""
x = 2
player_1 =[]
player_2 =[]

def click(number):
    global x,y
    global player_1,player_2
    
    
    from itertools import permutations
    
    set1 = permutations([1,2,3])
    set2 = permutations([4,5,6])
    set3 = permutations([7,8,9])
    set4 = permutations([1,4,7])
    set5 = permutations([2,5,8])
    set6 = permutations([3,6,9])
    set7 = permutations([1,5,9])
    set8 = permutations([3,5,7])
    
    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            first_player = all(num in player_1 for num in j )
            second_player = all(num in player_2 for num in j )
            
            if first_player == True:
                print("player_1 won the match" )
                showinfo("game result","player_1 won the match")
                
                root.quit()
                break
            if second_player == True:
                print("player_2 won the match" )
                showinfo("game result","player_2 won the match")
                
                
                root.quit()
                break
    
        
        
    if number == 1:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
            
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
            
        b1.config(text=y,font = ("ALGERIAN",60))
        b1.configure(state=DISABLED)
        
        # x = x+1
        
        

    
    if number == 2:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b2.config(text=y,font = ("ALGERIAN",60))
        b2.configure(state=DISABLED)
        
        
        
            
    if number == 3:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b3.config(text=y,font = ("ALGERIAN",60))
        b3.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 4:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b4.config(text=y,font = ("ALGERIAN",60))
        b4.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 5:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b5.config(text=y,font = ("ALGERIAN",60))
        b5.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 6:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b6.config(text=y,font = ("ALGERIAN",60))
        b6.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 7:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b7.config(text=y,font = ("ALGERIAN",60))
        b7.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 8:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b8.config(text=y,font = ("ALGERIAN",60))
        b8.configure(state=DISABLED)
        
        
    # x = x+1
        
    if number == 9:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(number)
        b9.config(text=y,font = ("ALGERIAN",60))
        b9.configure(state=DISABLED)
        
    
    x = x+1        




b1=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(1))
b1.grid(row=4,column=28)
b2=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(2))
b2.grid(row=4,column=29)
b3=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(3))
b3.grid(row=4,column=30)

b4=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(4))
b4.grid(row=5,column=28)
b5=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(5))
b5.grid(row=5,column=29)
b6=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(6))
b6.grid(row=5,column=30)

b7=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(7))
b7.grid(row=6,column=28)
b8=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(8))
b8.grid(row=6,column=29)
b9=Button(root,padx = 15, pady = 5, background="yellow",command=lambda:click(9))
b9.grid(row=6,column=30)


root.mainloop()
