# Start with initial shopping list
shopping_list = [] 

# Add items using append()
shopping_list.append("Milk")
shopping_list.append("Candy")
shopping_list.append("Bread")
shopping_list.append("Apples")

print("Shopping List:", shopping_list)

# sort the list alphabetically
shopping_list.sort()
print("Sorted List:", shopping_list)

# count how many times 'Candy' appear
candy_count = shopping_list.count("Candy")
print("Candy appear:", candy_count, "time(s)")

# Remove 'Apples' because they were bought
shopping_list.remove("Apples")
print("Shopping list after removing 'Apples':", shopping_list)

# Make a backup copy of current list
backup_list = shopping_list.copy()
print("Backup List:", backup_list)