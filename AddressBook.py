Contact = []

# Display the choices
while True:
    Choice = int(input("1. Add Contact \n2. Edit Contact \n3. Delete Contact \n4. View Contacts \n5. Search Address Book \n6. Exit \nEnter your Choice: "))

    # Add contact
    if Choice == 1:
        FirstName = input("First name: ")
        LastName = input("Last name: ")
        Address = input("Address: ")
        ContactNumber = int(input("Contact Number: "))
        NewContact = [FirstName, LastName, Address, ContactNumber]
        Contact.append(NewContact)
    
    # Edit Contact
    elif Choice == 2:
        Edit = input("Enter the contact you wish to edit: ")
        New = []
        Scan = 0
        for x in range(len(Contact)):
            if Edit == Contact[x][0]:
                Scan += 1
                print(Contact[x])
                Contact.pop(x)
                EditedFirstName = input("First name: ")
                EditedLastName = input("Last name: ")
                EditedAddress = input("Address: ")
                EditedContactNumber = int(input("Contact Number: "))
                EditedContact = [EditedFirstName, EditedLastName, EditedAddress, EditedContactNumber]
                Contact.append(EditedContact)
        if Scan == 0:
            print("The contact doesn't exist")

    # Delete Contact
    elif Choice == 3:
        Deleted = input("Enter the contact you wish to delete: ")
        New = []
        Scan = 0
        for x in range(len(Contact)):
            if Deleted == Contact[x][0]:
                Scan += 1
                print(Contact[x])
                Contact.pop(x)
                print("The contact has been deleted")
        if Scan == 0:
            print("The contact doesn't exist")

    # View Contacts
    elif Choice == 4:
        print("\tContacts\t")
        for x in range(len(Contact)):
                print(Contact[x])
        if not Contact:
            print("No Contacts")

    #Search Address Book
    elif Choice == 5:
        print("\tCriterias to choose from\t")
        Search = int(input("1. First Name \n2. Last Name \n3. Address \n4. Contact Number \nEnter your choice: ")) 
        if Search == 1:
            SearchFirstName = input("First Name: ")
            for a in range(len(Contact)):
                if SearchFirstName == Contact[a][0]:
                    print(Contact[a])
        if Search == 2:
            SearchLastName = input("Last Name: ")
            for b in range(len(Contact)):
                if SearchLastName == Contact[b][1]:
                    print(Contact[b])
        if Search == 3:
            SearchAddress = input("Address: ")
            for c in range(len(Contact)):
                if SearchAddress == Contact[c][2]:
                    print(Contact[c])
        if Search == 4:
            SearchContactNumber = int(input("Contact Number: "))
            for d in range(len(Contact)):
                if SearchContactNumber == Contact[d][3]:
                    print(Contact[d])
        if Search >=5:
            print("Invalid Search Criteria")