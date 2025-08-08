import pandas

# looping through rows in dataframes instead of columns to grab values better
# something.iterrows()

# should be able to take a name as an input, iterate through the values, then returns the NATO phonetic alphabet from those letters

#TODO create a dict in this format {"A":"Alpha", "B":"Bravo", etc.} using dataframes

data = pandas.read_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 26/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO create a list of the phonetic codewords based on user input
# converting to uppercase to match the csv inputs
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)