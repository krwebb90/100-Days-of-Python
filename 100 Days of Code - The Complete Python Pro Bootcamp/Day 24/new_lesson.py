# #had to put a raw string show the directory of my filepath since vscode was being difficult

# with open(r"C:\Users\webkerry\Documents\GitHub\100-Days-of-Python\100 Days of Code - The Complete Python Pro Bootcamp\Day 24\my_file.txt") as file:
#     contents = file.read()
#     print(contents)



# with open(r"C:\Users\webkerry\Documents\GitHub\100-Days-of-Python\100 Days of Code - The Complete Python Pro Bootcamp\Day 24\my_file.txt", "a") as file:
#     file.write("\nNew text.")


# #creates a new file if you don't have one called 'new_file' in the folder yet
# with open(r"C:\Users\webkerry\Documents\GitHub\100-Days-of-Python\100 Days of Code - The Complete Python Pro Bootcamp\Day 24\new_file.txt", "w") as file:
#     file.write("\nNew text.")



#this helps map the directory if you are within a nested folder

import os

script_path = os.path.abspath(__file__)  # Gets the full path of the current script
script_dir = os.path.dirname(script_path)  # Gets the directory containing the script
file_path = os.path.join(script_dir, "data.txt") #this can change with the new file names as needed

with open(file_path) as file:
    print(file.read())
