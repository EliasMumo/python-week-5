# file_handling_assignment.py

def main():
    try:
        # File Creation
        with open('my_file.txt', 'w') as file:
            file.write('This is the first line.\n')
            file.write('Here is the second line with a number: 123.\n')
            file.write('Finally, the third line with some more text.\n')

        # File Reading and Display
        print("Reading the contents of 'my_file.txt':")
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print(content)

        # File Appending
        with open('my_file.txt', 'a') as file:
            file.write('Appending a new line.\n')
            file.write('Another line added.\n')
            file.write('And one more line for good measure.\n')

        # Confirm appending
        print("Appending new lines to 'my_file.txt':")
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
