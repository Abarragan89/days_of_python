try:
    file = open("a_file.txt")
except FileNotFoundError:
    open("a_file.txt", "w")
else:
    print("the file was found!")
finally:
    print("hello world")