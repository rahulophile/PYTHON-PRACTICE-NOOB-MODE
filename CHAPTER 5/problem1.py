#WAP to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up

words = {
    "Madad" : "Help",
    "Kursi" : "Chair",
    "Billi" : "Cat",
    "Ghar" : "Home"
}
userWord = input("Enter Hindi word to traslate in English : ")
print("English of ","is",userWord,words[userWord])