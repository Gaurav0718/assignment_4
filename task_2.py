filename = 'output.txt'
with open(filename, 'w') as file:
    write_text = input("Enter text to write to the file: ")
    writing_file = file.write(write_text+'\n')
    file.close()

print(f"Data successfully written to {filename}")

with open(filename, 'a') as file:
    write_text = input("Enter additional text to append: ")
    writing_file2 = file.write(write_text+'\n')
    file.close()

print(f"Data successfully appended")

with open(filename, 'r') as file:
    read_text = file.read()
    print(f"Final contents of {filename}:")
    print(read_text)
    file.close()
