# ask for full name in incorrect spacing
full_name = input("Input your full name in incorrect spacing: ")

# convert to pascal case
pascal_cased_name = full_name.title().replace(" ", "")

# print result
print(f"Output: {pascal_cased_name}")