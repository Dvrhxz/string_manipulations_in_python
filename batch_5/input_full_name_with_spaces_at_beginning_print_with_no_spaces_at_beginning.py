# ask input for full name with spaces at the beginning
full_name = input("Input full name with spaces at beginning: ")
# remove spaces from beginning

fixed_full_name = full_name.lstrip()

# print the result
print(f"The inputted name is {fixed_full_name}")