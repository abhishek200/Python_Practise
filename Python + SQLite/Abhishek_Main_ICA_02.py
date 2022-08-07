
# Date = 25 Nov 2021
# In Class Assignment 2 LO2
# COMP 1026
import Abhishek_Modules_v2


def main():
    while (True):
        print("\n" * 30)
        print(" AAbhishek'S MAIN MENU ")
        print("---------------------------------")
        print(" ")
        print("1. Create Database and Table ")
        print("2. New Employee Registration ")
        print("3. List records ")
        print("4. Search records ")
        print("5. Delete records ")
        print("6. Calculate Gross Pay")
        print("7. Calculate Net Pay")
        print("9. EXIT ")
        print(" ")
        print("If you running the app for the first time select option 1 then proceed with other options")
        choice = int(input(" Enter your menu option (1/2/3/4/5/6/) Enter 9 to exit: "))
        if (choice == 2):
            Abhishek_Modules_v2.Abhishek_addEmployee()
        elif (choice == 3):
            Abhishek_Modules_v2.Abhishek_listRecords()
        elif (choice == 4):
            Abhishek_Modules_v2.Abhishek_searcRec()
        elif (choice == 5):
            Abhishek_Modules_v2.Abhishek_delRec()
        elif (choice == 6):
            Abhishek_Modules_v2.Abhishek_CalculateGrossPay()
        elif (choice == 7):
            Abhishek_Modules_v2.Abhishek_CalculateNetPay()
        elif (choice == 9):
            break
        elif (choice == 1):
            Abhishek_Modules_v2.Abhishek_db_table_create()
        else:
             print("Sorry wrong choice try again")

if __name__ == "__main__":
    main()
