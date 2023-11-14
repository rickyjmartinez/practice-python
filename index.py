msg='Welcome to Python 101: Strings'
print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())

# print(len(msg))
# print(msg.count('o'))

# print(msg[-1]) #negatives give last letters
# print(msg[:7]) #this gives letters from the first index to the second index

msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title())

msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)

msg='welcome to Python 101: Strings'
print(msg.replace('Python','Java'))
msg = msg.replace('Python','Java') 
print(msg)

msg='Welcome to Python 101: Strings'
print('Python' not in msg)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
print(msg)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)


name= input('What is your name? ')
age= input('What is your age?: ')
print('Hello ' + name + '! You are ' + age + ' years old.')

num1=input('Enter a digit: ')
num2=input('enter a second number: ')
answer=float(num1)+float(num2) 
print(answer)