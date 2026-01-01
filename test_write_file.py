from functions.write_file import write_file

# Case 1
print("Results for 'lorem.txt':")
line = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(line)

# Case 2

print("Results for 'pkg/morelorem.txt':")
line = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(line)

# Case 3

print("Results for '/tmp/temp.txt':")
line = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(line)
