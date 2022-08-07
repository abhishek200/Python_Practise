# Payroll Using Lists and FileIO
# Author: Taranjeet Singh
# Date:   30-11-2021

# define all functions
def getHourlyRate():
    # read a hourly rate (must be >= $14) from the keyboard
    # and validate.
    rate = int(input("Enter the hourly pay rate: "))
    while rate < 14:
        rate = input("Enter hourly pay rate that is greater than 14: ")
    return rate

def getHoursWorked(fileObject):
    hoursWorked = []
    for line in fileObject.readlines():
        hw = (line.strip())
        hoursWorked.append(hw)
    
    return hoursWorked

def calcGPay(hpRates, workHours):
    grossPay = []
    index = 0
    while (index < len(workHours)):
        gP = hpRates * float(workHours[index])
        grossPay.append(round(gP, 2))
        index += 1
    return grossPay

def totalAmount (grossPay):
    sum = 0
    for gp in grossPay:
        sum += gp
    return sum

def writeEmpPay(fileObject, grossPay, totalPay):
    for gp in grossPay:
        fileObject.write(str(gp))
    ttl = "Total Pay: " + str(totalPay)
    fileObject.write(ttl)
    

# definition of the program logic where all the functions are called
# input:
    # (1) get a valid hourly rate (must be >= $14)
    
    # get the hours worked from the file
    #   open the input file for reading
    #   (2) make a list of the hours worked
    #   close the file  

# to get hourly Pay of the employees
hrlyRate = getHourlyRate()

# to get employees working hours from the file
hrsWrkd = open("hoursWorked.txt", "r")
wrkngHrs = getHoursWorked(hrsWrkd)
hrsWrkd.close()

# processing:
    # (3)calculate the gross payments for all employees
    #    and make a list of all gross payments

    # (4)calculate the total amount of all payments

# to calculate gross Payment for all the employees
grssPay = calcGPay(hrlyRate, wrkngHrs)

# to calculate total amount of all payments
ttlAmnt = totalAmount(grssPay)    
# output:
    #   open the output file for writing
    #   (5) write all gross payments and the total amount to a file
    #   close the output file

# to save the results in a file
result = open("Payments.txt", "w")
writeEmpPay(result,grssPay,ttlAmnt)
result.close()

    

             
