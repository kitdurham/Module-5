# HOMEWORK MODULE 5

# Create a tuple named pokemon with the three strings as its elements 
pokemon = ('picachu', 'charmander', 'bulbasaur')

# Using index notation, print() the string that located at index 1 in pokemon
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

# Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
for i in range(2, 11):
    print(i)

# Use a while loop that prints out the integers 2 through 10.
i = 2
while i <= 10:
    print(i)
    i += 1
    
# Write a for loop that iterates over the string 'This is a simple string' and prints each character.
string = 'This is a simple string'
for char in string:
    print(char)
    
# Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word, three times.
words = ('this', 'is', 'a', 'simple', 'set')
for word in words:
    for i in range(3):
        print(word)
