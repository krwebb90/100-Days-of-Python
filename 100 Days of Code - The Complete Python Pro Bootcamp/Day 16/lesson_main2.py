from prettytable import PrettyTable

# import prettytable

table = PrettyTable()


table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.header = True
table.border = True
table.align = "l"

print(table)
