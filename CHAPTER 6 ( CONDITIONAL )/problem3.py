# A spam comment is defined as a text containing following keywords :
# "Make a lot of money", "buy now", "subscribe this", "click this", write a program to detect this

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("Write comment : ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)) :
    print("Spam Detected!")
else :
    print("Not a spam, yo can continue!")   