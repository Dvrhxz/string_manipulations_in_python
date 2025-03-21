# ask for full name in incorrect casing
full_name = input("Input full name in incorrect spacing: ")

# convert to snake case
snake_case_name = full_name.lower().replace(" ", "_")

# print result
print(f"Output: {snake_case_name}")