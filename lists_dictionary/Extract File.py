string = input().split('\\')
file = string[-1]
file_name_split = file.split(".")
file_name = file_name_split[0]
extension = file_name_split[1]

print(f'File name: {file_name}')
print(f'File extension: {extension}')