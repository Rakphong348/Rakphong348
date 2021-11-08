box=[1,2,3,4,5,6,7,8,9]
for i in range(9):
    box[i]=" "


def showXO_table():
    print("| "+box[0]+" | "+box[1]+" | "+box[2]+" |\n| "+box[3]+" | "+box[4]+" | "+box[5]+" |\n| "+box[6]+" | "+box[7]+" | "+box[8]+" |")

def check_result():
    if box[0]==box[1]==box[2]==("X" or "O"):
        return True
    elif box[3]==box[4]==box[5]==("X" or "O"):
        return True
    elif box[6]==box[7]==box[8]==("X" or "O"):
        return True
    elif box[0]==box[3]==box[6]==("X" or "O"):
        return True
    elif box[1]==box[4]==box[7]==("X" or "O"):
        return True
    elif box[2]==box[5]==box[8]==("X" or "O"):
        return True
    elif box[0]==box[4]==box[8]==("X" or "O"):
        return True
    elif box[2]==box[4]==box[6]==("X" or "O"):
        return True
    


print("Game Start")
showXO_table()

curent="X"

for round in range(9):
    hu_check = 0
    while hu_check == 0:
        print(curent+"'s turn")
        sel_s= int(input("Select space to write (1-9): "))
        if sel_s >= 1 and sel_s <=9:
            if box[sel_s-1]==" ":
                box[sel_s-1] = curent
                hu_check = 1
            else:
                print("\nAlready Selected,Select another one")
        else:
            print("\nJust select 1-9 you idiot!!")
        showXO_table()
    if check_result() == True:
        break
    if curent == "X":
        curent = "O"
    else:
        curent = "X"


if check_result() != True:
    print("Draw!!")
else:
    print(curent+" player win!!")