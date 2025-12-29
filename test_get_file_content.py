from functions.get_file_content import get_file_content

# Case 1

print("Resullt for 'lorem.txt' file:")
line = get_file_content("calculator", "lorem.txt")
print(line)

# Case 2

print("Result for 'main.py' file:")
line = get_file_content("calculator", "main.py")
print(line)

#case 3 

print("Result for 'pkg/calculator.py' file:")
line = get_file_content("calculator", "pkg/calculator.py")
print(line)

# Case 4 

print("Result for '/bin/cat' file:")
line = get_file_content("calculator", "/bin/cat")
print(line)

# Case 5 

print("Result for'pkg/does_not_exist.py' file:")
line = get_file_content("calcultor", "pkg/does_not_exist.py")
print(line)
