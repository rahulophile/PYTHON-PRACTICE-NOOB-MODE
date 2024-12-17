#WAP to find out whether a given post is about Rahul or not?
name = "Rahul"
post = input("Write Your Post : ")
if(name.lower() in post.lower()) :
    print("You have written about ",name)
else :
    print("You have not written about ",name)    