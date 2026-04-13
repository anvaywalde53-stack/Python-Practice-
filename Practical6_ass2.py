def capitalize_lines():
    print("Enter lines of text (Press Enter on an empty line to finish):")
    lines = []
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nOutput:")
    for line in lines:
        print(line.upper())

capitalize_lines()
