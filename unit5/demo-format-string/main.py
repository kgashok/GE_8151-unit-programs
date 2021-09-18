print("\nFORMAT OPERATOR")
print("------------------")
single = "My name is {}"
multiple = "My name is {} and my age is {}"

print("Before Format (single):", single)
single = single.format("Shiva")
print("After Format (single):", single)

print("Before Format (multiple):", multiple)
multiple = multiple.format("Shiva", 24)
print("After Format (multiple):", multiple)
