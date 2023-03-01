# HOMEWORK MODULE 5

print(pokemon[1])  # prints 'charmander'

# Unpack the values of pokemon into three new variables with names starter1, starter2, starter3. Print each variable using the print() function to verify the unpacking.
starter1, starter2, starter3 = pokemon
print(starter1) 
print(starter2) 
print(starter3) 

# Create a tuple using the tuple() built-in that contains the letters of your name. Print each character using the print() function to verify
name_tuple = tuple('Sian')
print(name_tuple)

# Check if the character i is in your tuple representation of your name.
if 'i' in name_tuple:
    print('The character "i" is in the tuple')
else:
    print('The character "i" is not in the tuple')
