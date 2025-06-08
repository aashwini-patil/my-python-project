'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
    file = open("sample.txt","r")    #give wrong file name to handle error
    read_file = file.read()
    print(read_file)
    file.close()
except:
    print("Error: The file 'sample.txt' was not found")


'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''

file = open("output.txt","w")
write_file = file.write(input("Enter text to write to the file: "))
print("Data successfully written to output.txt.")
file.close()

with open("output.txt","a") as file:
    append_file = file.write("\n"+ input("\nEnter additional text to append: "))
    print("Data successfully appended.")
file.close()

file = open("output.txt","r")
read_file = file.read()
print("\nFinal content of output.txt:\n",read_file)
file.close()