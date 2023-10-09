#Written by F211372 on 15/12/2022

'''
This function carries out the checkout functionality,
it has many modules, to help with all the
possible ways of checking out a book
'''

from database import *


def findlogforcheckout(stdID,b_id,logs):
    '''
    The function findlogforcheckout(stdID,b_id,logs) requires two input paramters along with the returned logs,
    the Student ID and Book ID, will check the log file to find matching records that display loanability.
    This functionality checks if the requested book to be checked out, is still on loan with another student.
    '''
    #we set the variable found to false 
    found = False
    for log in logs:
        if log[0]==b_id and log[3]=="-" and log[2]!="-":
            print("\nBook ID",b_id,"is still on loan.")
            found = True
            checkoutlogs(str(b_id),logs,str(stdID))
    if found== False:
        checkoutlogs(str(b_id),logs,str(stdID))

def checkoutlogs(b_id,logs,stdID):
    '''
    The function checkoutlogs(b_id,logs) requires two input parameters along with the returned logs,
    the Student ID and Book ID, will check the log file to find matching records that display loanability.
    If the log is found, it is checked if the book is reserved or available for loan.
    '''
    foundlog=[]
    for log in logs:
        if log[0]==b_id and log[3]=="-" and log[2]=="-" and log[4]==stdID:
            foundlog.append(log)
    if foundlog!=[]:
        for log in foundlog:
            print("\n")
            print("Reserved By:")
            print("\n")
            print("BookID      Reservation Date     Checkout Date       Return Date            Student ID")
            print("======================================================================================")
            print("%s %20s %20s %20s %20s"%(str(log[0]),str(log[1]),str(log[2]),str(log[3]),str(log[4])))
    else:
        print("\nIf Book ID",b_id,"is still on loan, it can be reserved.\nOtherwise, it is available for loan")

'''
This carries out the sub menu as defined in the Menu for checking out a book.
'''

def add_log(b_id,reservation_date,checkout_date,return_date,stdID,logs):
    '''
    if the book is available for loan, update the records and checkout
    5 input parameters, leaving return and reservation dates unchanged,
    the checkout date, student ID and book ID is updated.
    '''
    book_checkout=[b_id,reservation_date,checkout_date,return_date,stdID]
    logs.append(book_checkout)
    print ("\nThe book has been checked out successfully.")
    savetransactionlog(logs)

def update_log(b_id,reservation_date,checkout_date,return_date,stdID,logs):
    '''
    if reserved already by the same student, checkout date is updated
    leaving other records unchanged.
    '''
    for log in logs:
        if log[0]==b_id and log[4]==stdID and log[2]=="-" and log[1]!="-":
            log[2]=checkout_date
    print ("\nThe book has been checked out successfully.")
    savetransactionlog(logs)
    

def reserve_book(b_id,reservation_date,checkout_date,return_date,stdID,logs):
    '''
    To reserve a book a new log is added with reservation date, book ID and student ID. Other input parameters remain blank
    '''
    bookreservation=[b_id,reservation_date,checkout_date,return_date,stdID]
    logs.append(bookreservation)
    savetransactionlog(logs)
    print("\nThe book has been reserved successfully")
    


if __name__=="__main__":
    '''
    Testing functionality for checkout.py it works and displays the record.
    '''
    getBookRecords()
    readLogs()
    findlogforcheckout(str(6666),str(3),logs)



    
    
    

