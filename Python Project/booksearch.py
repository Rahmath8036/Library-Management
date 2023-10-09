#Written by F211372 on 15/12/2022


'''
This module helps the librarian search for a book by its title.
And then it prompts the user to input the book ID to check for
loan availability
'''

from database import *


def findBookID(b_title):
    '''
    The functionality findBookID(b_title), requires one input parameter- Book Title.
    If the Book Title is located, it will prompt the librarian to input the Book ID
    by looking at the record displayed.
    '''
    foundbook=[]
    #Check if the b_title can be found through the list if found, then append to empty list.
    for record in bookInfo:
        if record[2]==b_title:
            foundbook.append(record)
    #if the list is not empty then we print the records in our list
    if foundbook!=[]:
        for record in foundbook:
            print ("\nBookID      Genre             Title               Author          Price           PurchaseDate")
            print ("==============================================================================================")
            print ("%s %15s %20s %20s %10s %20s"%(str(record[0]),str(record[1]),str(record[2]),str(record[3]),str(record[4]),str(record[5])))
            b_id=input('\nWhat is the book ID? ')
            #Book ID check
            if b_id.isnumeric():
                b_id=int(b_id)
                if b_id>0 and b_id<=20:
                    #move on to find the loan records
                    findlog(str(b_id))
                else:
                    print("\nIncorrect Book ID. Please try again.")
            else:
                print("\nIncorrect Book ID. Please try again.")               
    else:
        print ("\nThis book is not available at the Library. Please try again.")


def findlog(b_id):
    '''
    If the Book ID input is valid from the findBookID(b_title),
    it will  carry out the findlog(b_id) functionality to
    display the loan availability.
    '''
    foundlog=[]
    #check if the b_id is in the record and if the log[2]/ return date should be "-"
    for log in logs:
            if log[0]==b_id and log[3]=="-" and log[2]!="-":
                foundlog.append(log)
                
    #if the list is not empty, then the book is on loan or else, it is available for loan
    if foundlog!=[]:
        print("\nThis book is currently on loan")
    else:
        print("\nThis book is available for loan")




if __name__=="__main__":
    '''
    testing for booksearch.py it works
    '''
    getBookRecords()
    readLogs()
    findBookID("Twilight")
    findBookID("xyz")
