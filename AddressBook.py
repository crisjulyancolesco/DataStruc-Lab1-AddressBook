# To define display()
from IPython.display import display

# List
Contact = []

# Display the choices
def MainMenu():
    print("-------------------------Address Book-------------------------")
    print("What would you like to do?")
    print("1. Add Contact \n2. Edit Contact \n3. Delete Contact \n4. View Contacts \n5. Search Address Book \n6. Exit")
    
# 1. Add contact
def Add(Contact):
    print("\nAdd Contact")
    NewContact = []
    FirstName = input("\tFirst name: ")
    LastName = input("\tLast name: ")
    Address = str(input("\tAddress: "))
    ContactNumber = int(input("\tContact Number: "))
    NewContact = [FirstName, LastName, Address, ContactNumber]
    Contact.append(NewContact)
    return Contact
print()

# 2. Edit Contact
# Edit the contact based on the first name of the contact
def Edit(Contact):
    print("\nEdit Contact")
    Edit = input("Enter the First name of the contact you wish to edit: ")
    NewContact = []
    Scan = 0
    for x in range(len(Contact)):
        if Edit == Contact[x][0]:
            Scan += 1
            print(Contact[x])
            Contact.pop(x)
            print("\nEdit Contact")
            EditedFirstName = input("\tFirst name: ")
            EditedLastName = input("\tLast name: ")
            EditedAddress = input("\tAddress: ")
            EditedContactNumber = int(input("\tContact Number: "))
            EditedContact = [EditedFirstName, EditedLastName, EditedAddress, EditedContactNumber]
            Contact.append(EditedContact)
            return Contact
    if Scan == 0:
        print("\nContact doesn't exist!")
        return Contact
print()

# 3. Delete Contact
# Delete the contact based on the first name of the contact
def Delete(Contact):
    print("\nDelete Contact")
    Deleted = input("Enter the First name of the contact you wish to delete: ")
    NewContact = []
    Del = 0
    for y in range(len(Contact)):
        if Deleted in Contact[y][0]:
            Del += 1
            print(Contact[y])
            Contact.pop(y)
            print("\nContact has been deleted!")
            return Contact
    if Del == 0:
        print("\nContact doesn't exist!")
        return Contact
print()

# 4. View Contacts
def View(Contact):
    print("\nAll Contacts")
    for x in range(len(Contact)):
            print(Contact[x])
    if not Contact:
        print("\nNo Contacts")
    print()

# 5. Search Address Book
def Search(Contact):
    print("\nSearch Book Address")
    print("\tCriterias to choose from:")
    Search = int(input("\t 1. First Name \n\t 2. Last Name \n\t 3. Address \n\t 4. Contact Number \n\n\tChoose criteria: ")) 
    SearchContact = []
    Find = -1

    # Search based on First Name
    if Search == 1: 
        SearchFirstName = str(input("\t First Name: "))
        for a in range(len(Contact)):
            if SearchFirstName == Contact[a][0]:
                Find = a
                SearchContact.append(Contact[a])

    # Search based on Last Name
    elif Search == 2:
        SearchLastName = str(input("\t Last Name: "))
        for b in range(len(Contact)):
            if SearchLastName == Contact[b][1]:
                Find = b
                SearchContact.append(Contact[b])

    # Search based on Address
    elif Search == 3:
        SearchAddress = str(input("\t Address: "))
        for c in range(len(Contact)):
            if SearchAddress == Contact[c][2]:
                Find = c
                SearchContact.append(Contact[c])

    # Search based on Contact Number
    elif Search == 4:
        SearchContactNumber = int(input("\t Contact Number: "))
        for d in range(len(Contact)):
            if SearchContactNumber == Contact[d][3]:
                Find = d
                SearchContact.append(Contact[d])

    # The user's input is none of the choices 
    else:
        print("\nInvalid Search Criteria!")
        return -1
    if Find == -1:
        return -1
    else:
        display(SearchContact)
        return Find
print()

# 6 Exit Contact
def Exit():
    print("\nThank you for using Address Book!!")
    print("Leaving Address Book................")
    print()

# For the main menu to call the functions based on the user's input
Choice = 0
while Choice in (0, 1, 2, 3, 4, 5):
    MainMenu()
    Choice = int(input("Please enter your Choice: "))
    if Choice == 1:
        Contact = Add(Contact)
    if Choice == 2:
        Contact = Edit(Contact)
    if Choice == 3:
        Contact = Delete(Contact)
    if Choice == 4:
        Contact = View(Contact)
    if Choice == 5:
        S = Search(Contact)
        if S == -1:
            print("The Contact doesn't exist. Please try again")
    if Choice == 6:
        Contact = Exit()