#WAP to fill in a letter template given below with name and date
# letter = '''
# Dear <|Name|>,
# You are selected
# <|Date|>
# '''

name = input("Enter your name : ")
date = input("Enter Date : ")

#SOLOTION-1
letter = '''
Dear <|Name|>,
You are selected
<|Date|>
'''
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

#SOLUTION-2
letter = f'''Dear {name},
You are selected
{date}''' 
print(letter)