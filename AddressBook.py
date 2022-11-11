# List
Contact = []

# Display the choices
while True:
    print("-------------------------Address Book-------------------------")
    print("What would you like to do?")
    Choice = int(input("1. Add Contact \n2. Edit Contact \n3. Delete Contact \n4. View Contacts \n5. Search Address Book \n6. Exit \n\nChoose an option: "))
    # 1. Add contact
    if Choice == 1:
        print("\nAdd Contact")
        FirstName = input("\tFirst name: ")
        LastName = input("\tLast name: ")
        Address = input("\tAddress: ")
        ContactNumber = int(input("\tContact Number: "))
        NewContact = [FirstName, LastName, Address, ContactNumber]
        Contact.append(NewContact)
        print()

    # 2. Edit Contact
    elif Choice == 2:
        print("\nEdit Contact")
        Edit = input("Enter the contact you wish to edit: ")
        New = []
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
        if Scan == 0:
            print("\nContact doesn't exist!")
        print()

    # 3. Delete Contact
    elif Choice == 3:
        print("\nDelete Contact")
        Deleted = input("Enter the contact you wish to delete: ")
        New = []
        Del = 0
        for x in range(len(Contact)):
            if Deleted == Contact[x][0]:
                Del += 1
                print(Contact[x])
                Contact.pop(x)
                print("\nContact has been deleted!")
        if Del == 0:
            print("\nContact doesn't exist!")
        print()

    # 4. View Contacts
    elif Choice == 4:
        print("\nAll Contacts")
        for x in range(len(Contact)):
                print(Contact[x])
        if not Contact:
            print("\nNo Contacts")
        print()

    # 5. Search Address Book
    elif Choice == 5:
        print("\nSearch Book Address")
        print("\tCriterias to choose from:")
        Search = int(input("\t 1. First Name \n\t 2. Last Name \n\t 3. Address \n\t 4. Contact Number \n\n\tChoose criteria: ")) 
        if Search == 1:
            SearchFirstName = input("\t First Name: ")
            for a in range(len(Contact)):
                if SearchFirstName == Contact[a][0]:
                    print(Contact[a])
            if not Contact:
                print("\nContact doesn't exist!")
        if Search == 2:
            SearchLastName = input("\t Last Name: ")
            for b in range(len(Contact)):
                if SearchLastName == Contact[b][1]:
                    print(Contact[b])
            if not Contact:
                print("\nContact doesn't exist!")
        if Search == 3:
            SearchAddress = input("\t Address: ")
            for c in range(len(Contact)):
                if SearchAddress == Contact[c][2]:
                    print(Contact[c])
            if not Contact:
                print("\nContact doesn't exist!")
        if Search == 4:
            SearchContactNumber = int(input("\t Contact Number: "))
            for d in range(len(Contact)):
                if SearchContactNumber == Contact[d][3]:
                    print(Contact[d])
            if not Contact:
                print("\nContact doesn't exist!")
        if Search >=5:
            print("\nInvalid Search Criteria!")
        print()

    # 6. Exit
    elif Choice >=6:
        print("\nExit")
        Exit = str(input("Would you like to exit Address Book? y/n: "))
        if (Exit ==' ' or Exit =='n' or Exit =='N' or Exit =='No' or Exit =='NO' or  Exit =='no'):
            print()
            continue
        if (Exit =='' or Exit =='Y' or Exit =='y' or Exit =='yes' or Exit =='YES' or Exit =='Yes'):
            break
