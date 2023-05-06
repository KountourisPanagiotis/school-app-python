from model.teacher import Teacher
from dao.teacher_dao import TeacherDAOImpl
from service.teacher_service import TeacherServiceImpl
from database.db_connection import conn
from exceptions.dao_exceptions import TeacherAlreadyExists, TeacherNotFound

# Create a new teacher DAO implementation object
teacher_dao = TeacherDAOImpl(conn)

# Create a new teacher service object using the DAO implementation object
teacher_service = TeacherServiceImpl(teacher_dao)

logo = """\033[34m

░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░  ███████╗░█████╗░░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░  ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░██║██║░░██║██║██╔██╗██║██║░░██╗░  █████╗░░███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
██║░░██╗██║░░██║██║░░██║██║██║╚████║██║░░╚██╗  ██╔══╝░░██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
╚█████╔╝╚█████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
░╚════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

████████╗███████╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░██████╗  ░░░░░░
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗██╔════╝  ░░░░░░
░░░██║░░░█████╗░░███████║██║░░╚═╝███████║█████╗░░██████╔╝╚█████╗░  █████╗
░░░██║░░░██╔══╝░░██╔══██║██║░░██╗██╔══██║██╔══╝░░██╔══██╗░╚═══██╗  ╚════╝
░░░██║░░░███████╗██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║██████╔╝  ░░░░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░  ░░░░░░

███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███╗░░░███╗███████╗███╗░░██╗████████╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░████╗░████║██╔════╝████╗░██║╚══██╔══╝
██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
\033[0m"""

print(logo)

# Prompt user for input
while True:

    # Menu options

    print("\033[1;32;40m" + "╔══════════════════════════════════════════════╗")
    print("\033[1;32;40m" + "║      CODING FACTORY TEACHERS MANAGEMENT      ║")
    print("\033[1;32;40m" + "╟──────────────────────────────────────────────╢")
    print("\033[1;37;40m" + "║   1. Get all teachers                        ║")
    print("\033[1;37;40m" + "║   2. Get a teacher by ID                     ║")
    print("\033[1;37;40m" + "║   3. Add a new teacher                       ║")
    print("\033[1;37;40m" + "║   4. Update a teacher                        ║")
    print("\033[1;37;40m" + "║   5. Delete a teacher                        ║")
    print("\033[1;37;40m" + "║   6. Exit                                    ║")
    print("\033[1;32;40m" + "╚══════════════════════════════════════════════╝")


    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input, please enter a number between 1 and 6")
        continue

    if choice == 1:
        teachers = teacher_service.get_all_teachers()
        for teacher in teachers:
            print(teacher)
    elif choice == 2:
        try:
            id = int(input("Enter the teacher's ID: "))
            teacher = teacher_service.get_teacher(id)
            print(teacher)
        except ValueError:
            print("Invalid input, please enter a valid ID")
        except TeacherNotFound as e:
            print(e)
    elif choice == 3:
        try:
            id = int(input("Enter the teacher's ID: "))
            first_name = input("Enter the teacher's first name: ")
            last_name = input("Enter the teacher's last name: ")
            new_teacher = Teacher(id, first_name, last_name)

            teacher_service.add_teacher(new_teacher)
            print("Teacher added successfully")
        except ValueError:
            print("Invalid input, please enter a valid ID")
        except TeacherAlreadyExists as e:
            print(e)
    elif choice == 4:
        try:
            id = int(input("Enter the teacher's ID: "))
            first_name = input("Enter the teacher's first name: ")
            last_name = input("Enter the teacher's last name: ")
            updated_teacher = Teacher(id, first_name, last_name)

            teacher_service.update_teacher(updated_teacher)
            print("Teacher updated successfully")
        except ValueError:
            print("Invalid input, please enter a valid ID")
        except TeacherNotFound as e:
            print(e)
    elif choice == 5:
        try:
            id = int(input("Enter the teacher's ID to delete: "))

            teacher_service.delete_teacher(id)
            print("Teacher deleted successfully")
        except ValueError:
            print("Invalid input, please enter a valid ID")
        except TeacherNotFound as e:
            print(e)
    elif choice == 6:
        print("Thank you for using CODING FACTORY schoolApp!")
        break
    else:
        print("Invalid input, please enter a number between 1 and 6")

    print("--------------------------------------------------------")

