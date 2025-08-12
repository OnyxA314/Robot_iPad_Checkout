import datetime

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


def default_ipad():
    ipad_file = open("ipad.csv", 'w')
    ipad_file.write("iPad ID, Checked Out, Time Out, Time In, Student Name\n")
    ipad_file.close()
    return

def default_robot():
    robot_file = open("robots.csv", 'w')
    robot_file.write("Robot Name, Checked Out, Time Out, Time In, Student Name\n")
    robot_file.close()
    return


def checkout(ipad_file, robot_file):
    ipad_id = input("Enter the ipad ID: ")
    robot_id = input("Enter the name of the robot: ")
    checkout_name = input("Enter the name of the student (optional): ")
    timeout = datetime.datetime.now().time()

    ipad_file.write (f"{ipad_id},T,{timeout},,{checkout_name}\n")
    robot_file.write(f"{robot_id},T, {timeout},,{checkout_name}\n")

    


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
if (reset == 'y'):
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

    elif (choice == VIEW_CHECKEDOUT):
        print("TODO")

    elif (choice == QUIT):
        print("Exiting the program...")

    else:
        print("Please choose a valid option")



    
    #every option requires files to be open, so just closing it all here :)
    ipad_file.close()
    robot_file.close()

    print("\n")
