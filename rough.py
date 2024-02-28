filename = "data.txt"

def write_data():
    with open(filename, "a") as f:
        data = input("Enter data to write to file: ")
        f.write(data + "\n")

def read_data():
    with open(filename, "r") as f:
        data = f.read()
        print("Data in the file:\n" + data)

def search_data():
    with open(filename, "r") as f:
        search_term = input("Enter search term: ")
        found = False
        for line in f:
            if search_term in line:
                print(line)
                found = True
        if not found:
            print("No matching data found.")
        

def delete_data():
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        delete_term = input("Enter data to delete: ")
        deleted = False
        for line in lines:
            if line.strip() != delete_term:
                f.write(line)
            else:
                deleted = True
        if deleted:
            print("Data deleted successfully.")
        else:
            print("No matching data found.")

def main():
    while True:
        print("Select an option:")
        print("1. Write data to file")
        print("2. Read data from file")
        print("3. Search data in file")
        print("4. Delete data from file")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            write_data()
        elif choice == "2":
            read_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
