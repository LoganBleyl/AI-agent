from functions.run_python_file import run_python_file

# Case 1

print("Results for 'main.py':")
results = run_python_file("calculator", "main.py")
print(results)

# Case 2 

print("Results for 'main.py, [3 + 5]':")
results = run_python_file("calculator", "main.py", ["3 + 5"])
print(results)

# Case 3

print("Results for 'tests.py':")
results = run_python_file("calculator", "tests.py")
print(results)

# Case 4

print("Results for '../main.py':")
results = run_python_file("calculator", "../main.py")
print(results)

# Case 5

print("Results for 'nonexistence.py':")
results = run_python_file("calculator", "nonexistent.py")
print(results)

# Case 6

print("Results for 'lorem.txt':")
results = run_python_file("calculator", "lorem.txt")
print(results)
