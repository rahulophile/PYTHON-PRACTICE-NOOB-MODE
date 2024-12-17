#WAP to calculate the grade of a student from his marks from the following scheme :
# 90-100 -> Ex, 80-90 -> A, 70-80 -> B, 60-70 -> C, 50-60 -> D,<50 -> fail

mark = int(input("Enter your mark : "))
if(mark <= 100 and mark >= 90) :
    print("Excelant!!")
elif(mark <90  and mark >= 80) :
    print("A Grade")
elif(mark < 80 and mark >= 70) :
    print("B Garde")
elif(mark < 70 and mark >= 60) :
    print("C Grade")
elif(mark < 60 and mark >= 50) :
    print("D Grade")
else :
    print("Fail!")                    