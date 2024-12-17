#WAP to find out weather a student have passed or failed if it requies a total of 40% and at least 33% in subject to pass. Assume 3 subjects and take marks as an input from user.

#Assumed 100 marks for each subject
sub1 = int(input("Subject 1 marks : ")) 
sub2 = int(input("Subject 2 marks : ")) 
sub3 = int(input("Subject 3 marks : ")) 

subjectSum = (sub1+sub2+sub3)/3
if(subjectSum>=40 and sub1>=33 and sub2>=33 and sub3>=33) :
    print("Congratulations!! You have passed the examination") 
else :
    print("You failed, better luck next year!")