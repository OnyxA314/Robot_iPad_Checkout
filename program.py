import datetime
import csv #for checking what robots and iPads are checked out currently

CHECKOUT = 1
CHECKIN = 2
VIEW_CHECKEDOUT = 3
QUIT = 4


def menu():
    print("Press" ,CHECKOUT, "to check out an iPad and Robot")
    print("Press", CHECKIN, "to check in an iPad and Robot")
    print("Press", VIEW_CHECKEDOUT, "to view all currently checked out items")
    print("Press", QUIT, "to exit the program")
    choice = int(input())
    return choice


#deletes any previes iPad data and resets it to a default state
def default_ipad():
    ipad_file = open("ipad.csv", 'w')
    ipad_file.write("iPad ID, Checked Out, Time Out, Time In, Student Name\n")
    ipad_file.close()
    return

#deletes any previous robot data and resets it to a default state
def default_robot():
    robot_file = open("robots.csv", 'w')
    robot_file.write("Robot Name, Checked Out, Time Out, Time In, Student Name\n")
    robot_file.close()
    return


def checkout(ipad_file, robot_file):

    checkout_amount = int(input("How many students are checking out a robot and iPad: "))
    checked_out = 0

    while (checked_out < checkout_amount):
        
        print("\n")

        ipad_id = input("Enter the ipad ID: ")
        robot_id = input("Enter the name of the robot: ")
        checkout_name = input("Enter the name of the student (optional): ")
        timeout = datetime.datetime.now().time() #time of checkout
        timeout = timeout.strftime("%I:%M %p") #converts time to 12 hour clock instead of 24. I => 12, M => Minute, p => AM/PM

        ipad_file.write (f"{ipad_id},T,{timeout},,{checkout_name}\n")
        robot_file.write(f"{robot_id},T, {timeout},,{checkout_name}\n")

        checked_out += 1


def viewCheckout (ipad_file, robot_file):
    
    print("\n\nCurrent iPads checked out:")
    print("\niPad ID,    Time Checked Out,     Student Name")
    reader = csv.DictReader(ipad_file)
    for row in reader:
        if row[" Checked Out"] == 'T':
            print(row["iPad ID"] + ",        " + row[" Time Out"] + ",                " + row[" Student Name"])



    print("\n\nCurrent Robots checked out:")
    print("\nRobot name,    Time Checked Out,   Student Name")
    reader = csv.DictReader(robot_file)
    for row in reader:
        if row[" Checked Out"] == 'T':
            print(row["Robot Name"] + ",        " + row[" Time Out"] + ",              " + row[" Student Name"])
    


def checkin(ipad_file, robot_file):
    
    rows = [] #empty list, going to contain every row to write back to the file
    ipad_found = False #assume the ipad isn't valid first

    ipad_checkin = input("What iPad are you checking in: ")
    robot_checkin = input("What robot are you checking in: ")

    reader = csv.DictReader(ipad_file)
    for row in reader:
        if row["iPad ID"] == ipad_checkin:
            if row[" Checked Out"] == 'T':
                row[" Checked Out"] = 'F'

                timein = datetime.datetime.now().time() #time of checkin
                timein = timein.strftime("%I:%M %p") #converts checkin to 12 hour clock
                row[" Time In"] = timein

                print(f"{ipad_checkin} has been checked in")
            else:
                print(f"{ipad_checkin} has already been marked as checked in...")
            
            ipad_found = True

        rows.append(row)

    
    #done reading all the rows, reopen the file as write and write all the data if we find an ipad, otherwise say no ipad matched
    if (ipad_found):
        ipad_file.close()
        ipad_file = open("ipad.csv", 'w')
       
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(ipad_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    else:
        print("No iPad with that ID was checked out...")





    #Now to do all that above but with the robots 
    rows = [] #empty list, going to contain every row to write back to the file
    robot_found = False #assume the robot isn't valid first

    reader = csv.DictReader(robot_file)
    for row in reader:
        if row["Robot Name"] == robot_checkin:
            if row[" Checked Out"] == 'T':
                row[" Checked Out"] = 'F'

                timein = datetime.datetime.now().time() #time of checkin
                timein = timein.strftime("%I:%M %p") #converts checkin to 12 hour clock
                row[" Time In"] = timein

                print(f"{robot_checkin} has been checked in")
            else:
                print(f"{robot_checkin} has already been marked as checked in...")
            
            robot_found = True

        rows.append(row)

    
    #done reading all the rows, reopen the file as write and write all the data if we found a robot, otherwise say we didn't find a matching one 
    if (robot_found):
        robot_file.close()
        robot_file = open("robots.csv", 'w')
       
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(robot_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    else:
        print("No robot with that name was checked out...")

    


#tries top open up the required files, if not create them
try:
    csv_file = open("ipad.csv", 'r')
    csv_file.close()
except:
    default_ipad()

try:
    csv_file = open("robots.csv", 'r')
    csv_file.close()
except:
    default_robot()


#deciding to reset or not
reset = input("Do you want to reset (y/N): ").lower() 
if (reset == 'y'): #defaults to false, have to explicitly type in Y or y to avoid any potential accidential deletions
    print("Reseting lists...")

    default_ipad()
    default_robot()


print("\n\n")

#loop to decide
choice = 5 #arbitrary value not 4 to initially enter loop, after we enter don't care about this value anymore
while (choice != QUIT):
    choice = menu()
    
    if (choice == CHECKOUT):
        ipad_file = open("ipad.csv", 'a')
        robot_file = open("robots.csv", 'a')

        checkout(ipad_file, robot_file)

    

    elif (choice == CHECKIN):
        print("TODO")

        ipad_file = open("ipad.csv", 'r')
        robot_file = open("robots.csv", 'r')

        checkin(ipad_file, robot_file)


    elif (choice == VIEW_CHECKEDOUT):
        ipad_file = open("ipad.csv", 'r')
        robot_file = open("robots.csv", 'r')

        viewCheckout(ipad_file, robot_file)



    elif (choice == QUIT):
        print("Exiting the program...")

    else:
        print("Please choose a valid option")



    
    #every option requires files to be open, so just closing it all here :)
    ipad_file.close()
    robot_file.close()

    print("\n")
