class  Student:
    def __init__(self,name,score):
     self.name = name
     self.score = score
     self.grade = "NULL"
     self.calGrade()

    def calGrade(self):
        if self.score >= 80 and self.score <= 100:
            self.grade = "A"
        elif self.score >= 75 and self.score <= 79:
            self.grade = "B+"
        elif self.score >= 70 and self.score <= 74:
            self.grade = "B"
        elif self.score >= 65 and self.score <= 69:
            self.grade = "C+"
        elif self.score >= 60 and self.score <= 64:
            self.grade = "C"
        elif self.score >= 55 and self.score <= 59:
            self.grade = "D+"
        elif self.score >= 50 and self.score <= 54:
            self.grade = "D"
        else:
            self.grade = "F"

    def showdata(self):
      print(self.name+" grade is "+self.grade)
    

st=[]
while True:
    st.append(Student(input("Enter student's name : "),int(input("Enter student's score : "))))
    check = input("Containue? (press x to exit):")
    if check == "x":
        break


file=open("student_grade.txt","w")
for obj in st:
   file.write(obj.name+"    "+obj.grade+"\n")
file.close()
