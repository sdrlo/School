teamlist = ["Richard","Maria","Dave","Ricko","Janelle"]
def printteamlist():
    print(teamlist)
    return teamlist
def addmember():
    newmember = input("Enter new members name: ")
    teamlist.append(newmember)
    return addmember
def removemember():
    oldmember = input("Enter old members name: ")
    teamlist.remove(oldmember)
    return removemember
def editmember():
    member = input("Enter members name to change: ")
    edit_member = input("Enter new name: ")
    teamlist.remove(member)
    teamlist.append(edit_member)
    return editmember

def main_menu():
    print("====Main Menu====")
    print("1. Display Team Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Edit Member")
    print("9. Exit Program")
print("Team Roster Program")
mainmenu = 0
while mainmenu != 9:
    main_menu()
    mainmenu = input("Select a menu option or 9 to exit: ")
    if mainmenu == '9':
        print("Good Bye!")
        break
    else:
        if mainmenu == '1':
            printteamlist()
        else:
            if mainmenu == '2':
                addmember()
            else:
                if mainmenu == '3':
                    removemember()
                else:
                    if mainmenu == '4':
                     editmember()



