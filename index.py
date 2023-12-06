# msg='Welcome to Python 101: Strings'
# print(msg)
# # print(msg.upper())
# # print(msg.lower())
# # print(msg.capitalize())
# # print(msg.title())

# # print(len(msg))
# # print(msg.count('o'))

# # print(msg[-1]) #negatives give last letters
# # print(msg[:7]) #this gives letters from the first index to the second index

# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title())
# print(msg1[::-1].title())

# msg="""Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)

# msg='welcome to Python 101: Strings'
# print(msg.replace('Python','Java'))
# msg = msg.replace('Python','Java') 
# print(msg)

# msg='Welcome to Python 101: Strings'
# print('Python' not in msg)

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# print(msg)

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)


# name= input('What is your name? ')
# age= input('What is your age?: ')
# print('Hello ' + name + '! You are ' + age + ' years old.')

# num1=input('Enter a digit: ')
# num2=input('enter a second number: ')
# answer=float(num1)+float(num2) 
# print(answer)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# name=input('what is your name? ')
# km=input('please give distance in km: ')
# miles=float(km) / 1.609
# print(f'Hello {name.capitalize()} you entered {km} and that is {round(miles,1)} miles.')

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
new_friends = list(friends)
print(friends)
print(new_friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)
# print(sum(cars))