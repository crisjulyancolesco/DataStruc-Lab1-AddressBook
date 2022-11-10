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
