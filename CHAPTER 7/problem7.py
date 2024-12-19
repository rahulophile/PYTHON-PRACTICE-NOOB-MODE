#WAP to print the following pattern
#   *
#  ***
# ***** and so on


#MY TRIAL ANSWER but successful

n = int(input("Enter the value of n : "))
for i in range(1, n + 1):  # Loop for each row
    print(" " * (n - i), end="") #end="" karne se by default wala new line nhi aata h
    print("*" * (2 * i - 1)) 

#NOTE pattern dekh ke hame ye pata lagana hai ki har iteration ke liye space aur star kitni bar print karna hai, then uske according code krna hai aur ye code krne ka dimag ayega practice se
