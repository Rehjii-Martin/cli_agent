from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")
print(result)

result = get_files_info("calculator", "pkg")
print(result)

result = get_files_info("calculator", "/bin")
print(result)

result = get_files_info("calculator", "../")
print(result)

