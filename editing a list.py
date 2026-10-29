#4 commands to interact with the list: add, change and delete elements or view the list
def addName(list):
    name = input("Enter a name to add:")
    list.append(name)
    return list
def changeName(list):
    name = input("Enter a name to change:")
    newName = input("Enter a name to change it to:")
    return [x if x != name else newName for x in list]
def deleteName(list):
    name = input("Enter a name to delete:")
    list.remove(name)
    return list
def viewNames(list):
    print(list)
names = []
addMore = True
#creating the list of names (or generally a list of anything)
while addMore == True:
    name = input("Enter a name")
    names.append(name)
    print(names)
    keepAdding = input("Continue adding names to the list? Y/N")
    if keepAdding.upper() != "N" and keepAdding.upper() != "Y":
        keepAdding = input("Invalid input, try again.")
    if keepAdding.upper() == "N":
        break
    elif keepAdding.upper() == "Y":
        continue
#asking user to interact with the list by using the 4 commands
while True:
    command = input("Enter a command (add, change, delete, view)")
    if command.lower() == "add":
        print(addName(names))
    elif command.lower() == "change":
        print(changeName(names))
    elif command.lower() == "delete":
        print(deleteName(names))
    elif command.lower() == "view":
        viewNames(names)
    else:
        print("Invalid command.")
