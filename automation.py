import os

folder_path = input("Enter the folder path: ")

if os.path.exists(folder_path):
    files = os.listdir(folder_path)

    print("\nText Files in the Folder:")

    found = False

    for file in files:
        if file.endswith(".txt"):
            print(file)
            found = True

    if not found:
        print("No text files found.")

else:
    print("Folder not found.")
