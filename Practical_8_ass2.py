source = input("Enter the source Python file name (e.g., script.py): ")
destination = input("Enter the destination file name (e.g., cleaned_script.py): ")

try:
    with open(source, "r") as src_file:
        lines = src_file.readlines()

    with open(destination, "w") as dest_file:
        for line in lines:
            if not line.strip().startswith("#"):
                dest_file.write(line)

    print("\n" + "="*20)
    print(f"SOURCE FILE: {source}")
    print("="*20)
    with open(source, "r") as f:
        print(f.read())

    print("\n" + "="*20)
    print(f"DESTINATION FILE (No Comments): {destination}")
    print("="*20)
    with open(destination, "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: One of the files could not be found.")
except Exception as e:
    print(f"An error occurred: {e}")
  
