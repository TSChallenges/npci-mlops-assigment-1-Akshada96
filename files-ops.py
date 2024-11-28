import os
import sys


def create_dir(dir_name):
    os.mkdir(dir_name)
    print("Directory is created ")
    return


def change_dir(dir_name):
    os.chdir(dir_name)
    print("Directory is chnaged ")
    return


def delete_dir(dir_name):
    os.rmdir(dir_name)
    print("Directory is deleted ")
    return


def list_dir():
    print("Directory list ", os.listdir())
    return


def display_pwd():
    print("Current working directory is ", os.getcwd())
    return


def create_file(file_name):

    with open(file_name, 'w') as f:
        pass
    print(f"File '{file_name}' is created ")

    return


def write_file(file_name):

    contents = input("Enter the contents into the file ")
    with open(file_name, 'a') as f:
        f.write(contents + '\n')
    print(f"Contents written to file successfully")

    return


def read_file(file_name):

    with open(file_name, 'r') as f:
        print(f.read())

    return


def delete_file(file_name):

    os.remove(file_name)
    return


def main():
    while True:
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Delete a file")
        print("5. Create a directory")
        print("6. Change a directory")
        print("7. Delete a directory")
        print("8. list a directory")
        print("9. display pwd")
        print("0. Exit")
        choice = input("Enter your choice here: ")

        if choice == '1':
            file_name = input("1. Enter the file name ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("2. Enter the file name ")
            write_file(file_name)
        elif choice == '3':
            file_name = input("3. Enter the file name ")
            read_file(file_name)
        elif choice == '4':
            file_name = input("4. Enter the file name ")
            delete_file(file_name)
        elif choice == '5':
            dir_name = input("5. Enter the directory name ")
            create_dir(dir_name)
        elif choice == '6':
            dir_name = input("6. Enter the directory name ")
            change_dir(dir_name)
        elif choice == '7':
            dir_name = input("7. Enter the directory name ")
            delete_dir(dir_name)
        elif choice == '8':
            list_dir()
        elif choice == '9':
            display_pwd()
        elif choice == '0':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
