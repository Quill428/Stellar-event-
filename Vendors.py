"""
With the growing number of events being handled by "Stellar Events", the team often finds it challenging 
to keep track of each vendor's contact details. Misplaced contact information or double bookings due to 
miscommunication often results in losses and a hit to the company's reputation. To streamline this 
process and avoid such pitfalls, there's a need for a basic digital solution to manage all vendor contacts.

You have been approached to develop a basic Contact Book application that helps manage vendor contacts
 efficiently. Using this tool “Stellar Events” must be able to perform followings:

-Add New Vendor Details: Onboard new vendors, their contact details must be easily added to the system. 
This includes their name (or company name), phone number, and email address.
-Access Vendor Information Quickly: For ongoing projects, team members must quickly access specific vendor 
details with a simple search.
-Remove Vendors: If a vendor goes out of business or if there's a decision to cease collaboration due to 
quality issues, their details must be swiftly removed from the system.
-Update Vendors: Vendor details must be able to be updated to provide relevant updated information.
-Add Extra Vendor Details: Give the ability for the users to add extra details they may need from Vendors 
(e.g. Vendor categories)
-Simple Menu: Add a simple terminal menu that allows you to select which operations you want to perform
 when using the application.
"""

Vendors = {
    "Vendor1" : {
        "name":"Mr.truck",
        "number": "22543634",
        "email":"truck@gmail.com"
    },
    "Vendor2" : {
        "name":"Devil Donuts",
        "number": "33845-36688",
        "email":"DevilDonuts@gmail.com"
    },
    "Vendor3" : {
        "name":"Emma's rocks",
        "number": "366236623662",
        "email":"Emmas@gmail.com"
    },
    "Vendor4" : {
        "name":"Mrs.truck",
        "number": "32543634",
        "email":"truck@gmail.com"
    } 
}#the list of vendors that are already added to the program


print(Vendors)#shows the vendors that are currently enterd before going into the loop
Task = 0 #sets Task to 0 starts the loop as its not greater than 6
extrainfo = ""#sets extrainfo as empty so they can be used in other parts of the code even if they weren't used yet by the user
while Task < 6: #loops until something a part from 1,2,3,4,5 is entered
    print('\033[4m' + "what would you like to do?")#the start of it bolds the line to make it stand out more with out contining it 
    print('\033[0m'+"1. add new info/new person") #\033[0m removes the bold from the text]
    print("2. access all the Vendors")
    print("3. delete a Vendors info")
    print("4. update a Vendors info")
    print("5. add new info")
    print("6. Exit")
    Task = int(input()) #allows an input from the user and connects to the if statements 

    if Task == 1:#starts the process to allow the user to add new vendors
        print("what is the Vendor you want to add?")
        vname = input()
        print("what is their phone number")
        Vphone = int(input())
        print("what is their email?")
        Vmail = input()
        Vendors[vname] = {"name": vname, "number": Vphone, "email": Vmail}#the code that adds the code the user entered in to be made into a new character 
        print(Vendors)

    elif Task == 2:
        for vendor, details in Vendors.items():
            print(f"{vendor}: {details}") #this line of code shows each different vendor on a different line to see the list of them and all their info easily
        #with out getting lost which info is for which one 
        print("")
        print("press enter to continue")#lets the user read the vendors before going back to the main code
        input()

    elif Task == 3:#allows thhe user to remove a vendor
        print("which number do you want to get rid of? ")
        num = input()
        
        remove = "Vendor" + num #made so the user just enters a number and it doesn't cause issues 
        if remove in Vendors:
            print(f"you want to delete: {remove} - {Vendors[remove]} yes or no") #confrims if the user wants to delete that vendor
            confirm_delete = input()
            if confirm_delete == "yes":#if the user says yes it will delete the Vendor             
                del Vendors[remove]        
                print(Vendors)#prints the new list vendors after the old one was deleted
            else:
                print("delete removed returning to menu")
        else:
            print("vendor doesn't exist")



    elif Task == 4:
        print("who would you want to update? ")
        updates = input()
        print("what would you like to update")
        print(f"name, number, email, " + extrainfo) #shows all info available to add as well asif there is any new one created by a user 
        infos = input()
        print("what would you change it to")
        newinfo = input() #allows the info to be added or changed 
        updated = "Vendor" + updates        
        Vendors [updated] [infos] = newinfo
        print("Updated")


    elif Task == 5: #adding new info 
        print("what is the new form of information? ")
        extrainfo = input()
        print("add the info you want")
        newlineinfo = input()
        Vendors.update({extrainfo: newlineinfo}) #allows the user to add the info if needed but allows them to update einfo and add it to each vendor 
        #this is done incase the user doesn't wanted to add the info 
        print (Vendors)

    else:
        print("exiting")
        break #ends the loop closing the program

