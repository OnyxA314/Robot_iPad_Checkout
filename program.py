import datetime
import csv #for checking what robots and iPads are checked out currently

CHECKOUT = '1'
CHECKIN = '2'
VIEW_CHECKEDOUT = '3'
VIEW_ALL = '4'
QUIT = '5'


def menu():

    print("Press" ,CHECKOUT, "to check out an iPad and Robot")
    print("Press", CHECKIN, "to check in an iPad and Robot")
    print("Press", VIEW_CHECKEDOUT, "to view all currently checked out items")
    print("Press", VIEW_ALL, "to view all iPads and Robots used at this event")
    print("Press", QUIT, "to exit the program")
    choice = input("Your Choice: ")
    return choice



#deletes any previes iPad data and resets it to a default state
def default_ipad():

    ipad_file = open("ipad.csv", 'w')
    ipad_file.write("iPad ID, Checked Out, Time Out, Time In\n")
    ipad_file.close()
    return


#deletes any previous robot data and resets it to a default state
def default_robot():

    robot_file = open("robots.csv", 'w')
    robot_file.write("Robot Name, Checked Out, Time Out, Time In\n")
    robot_file.close()
    return



def checkout(ipad_file, robot_file):

    checkout_amount = int(input("How many students are checking out a robot and iPad: "))
    checked_out = 0

    while (checked_out < checkout_amount):
        
        print("\n")

        ipad_id = input("Scan the iPad checking out: ")
        robot_id = input("Scan the robot checking out: ")
        #checkout_name = input("Enter the name of the student (optional): ")
        timeout = datetime.datetime.now().time() #time of checkout
        timeout = timeout.strftime("%I:%M %p") #converts time to 12 hour clock instead of 24. I => 12, M => Minute, p => AM/PM

        ipad_file.write (f"{ipad_id},T,{timeout},\n")
        robot_file.write(f"{robot_id},T, {timeout},\n")

        checked_out += 1


def viewCheckout (ipad_file, robot_file):
    
    print("\n\nCurrent iPads checked out:")
    print("\niPad ID     Time Checked Out")
    reader = csv.DictReader(ipad_file)
    for row in reader:
        if row[" Checked Out"] == 'T':
            print(row["iPad ID"] + "         " + row[" Time Out"])



    print("\n\nCurrent Robots checked out:")
    print("\nRobot name     Time Checked Out")
    reader = csv.DictReader(robot_file)
    for row in reader:
        if row[" Checked Out"] == 'T':
            print(row["Robot Name"] + "         " + row[" Time Out"])
    


def checkin():

    checkin_amount = int(input("How many sets do you want to check in: "))
    checkedin = 0

    while (checkedin < checkin_amount):
        ipad_file = open("ipad.csv", 'r')
        robot_file = open("robots.csv", 'r')

        rows = [] #empty list, going to contain every row to write back to the file
        ipad_found = False #assume the ipad isn't valid first

        ipad_checkin = input("Scan the iPad you are checking in: ")
        robot_checkin = input("Scan the robot you are checking in: ")

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


        print("\n\n")
        checkedin += 1

    

def viewAll (ipad_file, robot_file):

    print("\nAll iPads used: ")
    for ipad_lines in ipad_file:
        print(ipad_lines)

    print("\nAll Robots used: ")
    for robot_lines in robot_file:
        print(robot_lines)




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
choice = 100 #arbitrary value not 5/QUIT to initially enter loop, after we enter don't care about this value anymore
while (choice != QUIT):
    choice = menu()
    
    if (choice == CHECKOUT):
        ipad_file = open("ipad.csv", 'a')
        robot_file = open("robots.csv", 'a')

        checkout(ipad_file, robot_file)

        ipad_file.close()
        robot_file.close()

    

    elif (choice == CHECKIN):
        
        checkin()


    elif (choice == VIEW_CHECKEDOUT):
        ipad_file = open("ipad.csv", 'r')
        robot_file = open("robots.csv", 'r')

        viewCheckout(ipad_file, robot_file)  

        ipad_file.close()
        robot_file.close()


    elif (choice == VIEW_ALL):
        ipad_file = open("ipad.csv", 'r')
        robot_file = open("robots.csv", 'r')

        viewAll (ipad_file, robot_file)

        ipad_file.close()
        robot_file.close()


    elif (choice == QUIT):
        print("Exiting the program...")

    else:
        print("\n\n\n")
        print("WARNING: INVALID OPTION, RETURNING TO MENU")
        print("Please choose a valid option")
        print("\n\n\n")

  
    print("\n")
