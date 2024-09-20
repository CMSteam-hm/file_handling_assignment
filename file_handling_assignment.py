# file_handling_assignment.py

def main():
    try:
        # Step 1: File Creation - Writing to a new file
        with open("my_file.txt", "w") as file:
            file.write("Line 1: This is the first line.\n")
            file.write("Line 2: The number 42 is here.\n")
            file.write("Line 3: End of the initial content.\n")
        print("File created and initial content written.")

        # Step 2: File Reading - Reading and displaying the file content
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nFile Content after initial write:\n")
            print(content)

        # Step 3: File Appending - Appending more lines to the file
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appended text here.\n")
            file.write("Line 5: Another number, 100, added.\n")
            file.write("Line 6: End of appended content.\n")
        print("Additional lines appended to the file.")

        # Step 4: Reading and displaying the updated content
        with open("my_file.txt", "r") as file:
            updated_content = file.read()
            print("\nFile Content after appending:\n")
            print(updated_content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied when accessing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
  
