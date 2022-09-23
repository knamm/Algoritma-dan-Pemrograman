x=input('Enter String : ')
y=['a','i','u','e','o']
z=''

for letter in x:
    if letter.lower() not in y:
        z+=letter
print(z)