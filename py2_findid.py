string = input("Enter student Name : ")
file = open("student_data.txt","r")

flag = 0
index = 0

for line in file:
    if string in line:
        for letter in line:
            index+=1
            if letter == " ":
                break    
        print("ID :"+line[index:len(line)])
        flag=1
        break

if flag == 0:
    print("not found")

file.close()