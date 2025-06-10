from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

result = get_file_content("calculator", "main.py")
print(result)

result = get_file_content("calculator", "lorem.txt")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print(result)

result = get_file_content("calculator", "/bin/cat")
print(result)

