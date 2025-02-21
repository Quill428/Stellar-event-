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
}

#figure out how to add a list of info into the same line etc

#ven=Vendors.values()
print(Vendors)
Task = 0
extrainfo = ""
while Task < 6: 
    print("what would you like to do")
    print("1. add new info/new person")
    print("2. access all the Vendors")
    print("3. delete a Vendors info")
    print("4. update a Vendors info")
    print("5. add new info")
    print("6 Exit")
    Task = int(input())

    if Task == 1:
        print("what is the Vendor you want to add?")
        vname = input()
        print("what is their phone number")
        Vphone = int(input())
        print("what is their email?")
        Vmail = input()
        Vendors[vname] = {"name": vname, "number": Vphone, "email": Vmail}
        #Vendors.append(Vphone)
        #Vendors.append(Vmail)
        print(Vendors)

    elif Task == 2:
        for vendor, details in Vendors.items():
            print(f"{vendor}: {details}")
        #print(Vendors)

    elif Task == 3:
        print("which number do you want to get rid of? ")
        num = input()
        remove = "Vendor" + num
        if remove in Vendors:
            del Vendors[remove]        
            print(Vendors)
        else:
            print("Error back to menu")



    elif Task == 4:
        print("who would you want to update? ")
        updates = input()
        print("what would you like to update")
        print(f"name, number, email, " + extrainfo)
        infos = input()
        print("what would you change it to")
        newinfo = input()
        updated = "Vendor" + updates        
        Vendors [updated] [infos] = newinfo 
        print("Updated")


    elif Task == 5:
        print("what is the new form of information? ")
        extrainfo = input()
        print("add the info you want")
        newlineinfo = input()
        Vendors.update({extrainfo: newlineinfo})
        print (Vendors)
    else:
        print("exiting")
        break

