try:
    filename = 'my_file1.txt'
    with open(filename, 'r') as file1:
        reading_file = file1.readlines()
        print("Reading file content:")
        for i in reading_file:
            n = 1
            print(f"Line{n}: {i}")
            n+=1
        file1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")