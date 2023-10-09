#Written by F211372 on 15/12/2022

'''
This module helps the librarian return a book back to the system.
It also helps the librarian search reservations upon a return a book,
it also lists who reserved the book first.
'''

from database import *


def updatelog_return(b_id,reservation_date,checkout_date,return_date,stdID,logs):
    '''
    The function updatelog_return(b_id,reservation_date,checkout_date,return_date,stdID,logs)
    requires 5 inputs.
    The return date will be an input parameter and the respective
    log is updated accordingly by using None for other parameters.
    It will save the transaction logs after updating the record.
    It will then look through the log file to notify the librarian about the reservations for the
    particular book.
    '''
    for log in logs:
        #updating return date for the particular record after a check by updating the logfile
        #and listing reservations.
        if log[0]==b_id and log[4]==stdID and log[2]!="-" and log[3]=="-":
            log[3]=return_date
    print("\nThe book has been returned successfully")
    savetransactionlog(logs)
    search_reservation(b_id,logs)


def findlogforreturn(b_id,stdID,logs):
    '''
    The function findlogforreturn(b_id,stdID,logs) requires two input parameters,
    the Book ID and Student ID.
    According to the user input, it will find the respective log.
    If log is found it will return True and carry out the
    updatelog_return(b_id,reservation_date,checkout_date,return_date,stdID,logs) function.
    Otherwise, False and an error message is displayed.
    '''
    foundlog=[]
    for log in logs:
        #finding the log to return the book
        if log[0]==b_id and log[3]=="-" and log[2]!="-" and log[4]==stdID:
            foundlog.append(log)
            
    #if the list is not empty we print the record and input the return date,
    #otherwise an error is displayed. 
    if foundlog!=[]:
        for log in foundlog:
            print("\n")
            print("BookID      Reservation Date     Checkout Date       Return Date            Student ID")
            print("======================================================================================")
            print("%s %20s %20s %20s %20s"%(str(log[0]),str(log[1]),str(log[2]),str(log[3]),str(log[4])))
        return True
    return False


def search_reservation(b_id,logs):
    '''
    The search_reservation(b_id,logs) requires one paramter, Book ID.
    Upon a return of the book, the search_reservation(b_id,logs)
    displays the reservations for the particular book with the student ID and date,
    so that if there are multiple reservations, the librarian will know who reserved first.
    '''
    for log in logs:
        if log[0]==b_id and log[1]!="-" and log[2]=="-":
            print("\nBook ID",log[0],"has been reserved by Student ID",log[4],"on",log[1]+".")

            


if __name__=="__main__":
    '''
    Testing functionality for findlogforreturn.
    If the log is found, the status is printed- True and the record is displayed,
    otherwise False is displayed.
    '''
    getBookRecords()
    readLogs()
    status = findlogforreturn("5","6328",logs)
    print(status)
    status = findlogforreturn("1289","1",logs)
    print(status)



