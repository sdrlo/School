## Team member class
class memberClass:
    name = ""
    phone = ""
    jerseynum = ""
    displaydata = ""

    def __init__(self, name, phone, jerseynum):
        self.name = name
        self.phone = phone
        self.jerseynum = jerseynum
       
#mutator methods
    def setname(self, name):
        self.name =name
    def setphone(self, phone):
        self.phone = phone
    def setjerseynum(self, jerseynum):
        self.jerseynum = jerseynum
    
# accessor methods
    def getname(self):
        return self.name
    def getphone(self):
        return self.phone
    def getjerseynum(self):
        return self.jerseynum
    def getdisplaydata(self):
        return self.displaydata
    def displayData(self):
        print("")
        print("Team Roster")
        print("_____________")
        print("Name:", self.name)
        print("Phone Number:", self.phone)
        print("Jersey Number:", self.jerseynum)
        print("")
        return


# Program methods and import data
def menu():
    print("====Main Menu====")
    print("1. Display roster: ")
    print("2. Add team member: ")
    print("3. Add member phone number: ")
    print("4. Add member jersey number: ")
    print("5. Edit member: ")
    print("6. Remove member: ")
    print("9. Exit program: ")
    print("")
    return int(input("Selection>"))

def printMembers(members):
    if len(members) ==0:
        print("No current members in roster.")
    else:
        for x in members.keys():
            members[x].displayData()
def addMember(members):
   newMember = input("Enter new members name: ")
   newPhone = input("Enter new members phone number: ")
   newJerseynum = input("Enter new members jersey number: ")
   members[newMember] = memberClass(newMember, newPhone, newJerseynum)
   return members

def addPhone(members):
    newMember = input("Enter new members name: ")
    newPhone = input("Enter new members phone number: ")
    newJerseynum = input("Enter new members jersey number: ")
    members[newMember] = memberClass(newMember, newPhone, newJerseynum)
    return members

def addJerseynum(members):
    newMember = input("Enter new members name: ")
    newPhone = input("Enter new members phone number: ")
    newJerseynum = input("Enter new members jersey number: ")
    members[newMember] = memberClass(newMember, newPhone, newJerseynum)
    return members

def removeMember(members):
    removeName = input("Enter members name to remove: ")
    if removeName in members:
        del members[removeName]
    else:
        print("Member not found")

def editMembers(members):
    oldName = input("Enter members name to edit: ")
    if oldName in members:
        newName = input("Enter new member name: ")
        newPhone = input("Enter new member's phone number: ")
        newJerseynum = input("Enter new member's jersey number: ")
        members[oldName] = memberClass(newName, newPhone, newJerseynum)
    else:
        print("No such member")
        return members
#Start Code
print("Welcome to the Team Manager")
members = {}
menuSelection = menu()
while menuSelection != 9:
    if menuSelection == 1:
        printMembers(members)
        menuSelection = menu()
    elif menuSelection == 2:
        members = addMember(members)
        menuSelection = menu()
    elif menuSelection == 3:
        members = addPhone(members)
        menuSelection = menu()
    elif menuSelection == 4:
        members = addJerseynum(members)
        menuSelection = menu()
    elif menuSelection == 5:
        members = editMembers(members)
        menuSelection = menu()
    elif menuSelection == 6:
        members = removeMember(members)
        menuSelection = menu()
        print("Exiting Program...")