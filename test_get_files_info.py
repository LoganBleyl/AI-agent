from functions.get_files_info import get_files_info
# case 1
print("Result for current directory:")
lines = get_files_info("calculator", ".")
print(lines)
# case 2
print("Result for 'pkg' directory:")
lines = get_files_info("calculator", "pkg")
print(lines)
# case 3
print("Result for '/bin' directory:")
lines = get_files_info("calculator", "/bin")
print(lines)
# case 4
print("Result for '../' directory:")
lines = get_files_info("calculator", "../")
print(lines)
