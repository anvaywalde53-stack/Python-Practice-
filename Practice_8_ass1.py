source_filename = "data.txt"
destination_filename = "data_uppercase.txt"

try:
    with open(source_filename, "r") as source_file:
        content = source_file.read()
    
    with open(destination_filename, "w") as dest_file:
        dest_file.write(content.upper())
    
    print(f"Content from '{source_filename}' has been converted to uppercase and saved to '{destination_filename}'.")

except FileNotFoundError:
    print("The source file was not found.")
  
