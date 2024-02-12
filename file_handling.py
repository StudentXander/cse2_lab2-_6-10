try:
    # Read from input.txt
    with open('input.txt', 'r') as file:
        content = file.read()  # Corrected: Added () to invoke the read() method

    # Write the content read from input.txt into output.txt
    with open('output.txt', 'a') as file:
        file.write(content)

    print("Content copied successfully from input.txt to output.txt.")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print(f"An error occurred: {e}")
