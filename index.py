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
