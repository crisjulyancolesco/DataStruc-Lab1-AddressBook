Contact = []

# Display the choices
while True:
    Choice = int(input("1. Add Contact \n 2. Edit Contact \n 3. Delete Contact \n 4. View Contacts \n 5. Search Address Book \n 6. Exit \n Enter your Choice: "))

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
        Delete = input("Enter the contact you wish to delete: ")
        New = []
        Del = 0
        for x in range(len(Contact)):
            if Delete == Contact[x][0]:
                Del += 1
                print(Contact[x])
                Contact.pop(x)
                print("The contact has been deleted")
        if Del == 0:
            print("The contact doesn't exist")