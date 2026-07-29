
# list

my_list = [1, 2, 3, 4, 5]
print(my_list)

shoping_list = ["milk", "eggs", "bread", "butter"]
print(shoping_list)

print(shoping_list[0])  # Accessing the first item
print(shoping_list[-1])  # Accessing the last item  
print(shoping_list[1:3])  # Accessing a slice of the list
# It prints items at index 1 and 2 ("eggs" and "bread"), but not index 3 because the end index is excluded.
# If you want to include index 3 as well, you need to write:
print(shoping_list[1:4])  # Accessing a slice of the list
shoping_list.append("cheese")  # Adding an item to the list
print(shoping_list)
del shoping_list[2]  # Removing an item from the list
print(shoping_list)

list_num = [1, 2, 3, 4, 5]
list_num.append(6)  # Adding an item to the list
print(list_num)
print(len(list_num))  # Getting the length of the list
print(sum(list_num))  # Getting the sum of the list
print(max(list_num))  # Getting the maximum value in the list
print(min(list_num))  # Getting the minimum value in the list

