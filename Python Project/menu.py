#Written by F211372 on 15/12/2022

'''
This is the menu for my program, the meny describes my functions.
However my sub modules are database.py,bookselect.py,
booksearch.py,bookreturn.py and bookcheckout.py.
The functions are described in depth under the own modules. 
It contains a GUI and runs all programs.
'''

from tkinter import *
from bookcheckout import *
from database import *
from bookreturn import*
from booksearch import *
from bookselect import *


def say_hello():
    '''
    This is the command that gets called for the button Hello
    It reads the text files, book info and logfile. 
    '''
    bookInfo=getBookRecords()
    logs=readLogs()
    print ("Welcome to the Library")
    return bookInfo, logs




def say_bye():
    '''
    This is the command to exit the program.
    It destoys it.
    '''
    print ("\nSee you soon. Have a nice day.")
    window.destroy()

def search_book():
    '''
    command to search books from the logfile.
    One input required- book title and this will find the logs with the input b_id
    later on within the function. 
    '''
    b_title=input('\nWhat is the title of the book? ')
    findBookID(b_title)


def checkout_book():
        '''
        command to checkout a book
        requires two inputs to do the functionality of finding logs for checkout
        - student id
        - book id
        It then has a sub menu to do all the possible ways of checkout.
        '''
        stdID=input("\nPlease enter the student's ID ")
        #Student ID check
        if stdID.isnumeric():
            stdID=int(stdID)
            if stdID<=9999 and stdID>=1000:
                b_id=input("\nPlease enter the Book ID ")
                #Book ID check
                if b_id.isnumeric():
                    b_id=int(b_id)
                    if b_id<=20 and b_id>=1:
                        #Calls the function to do the find log for checkout and three parameters required given from above,
                        #along with logs
                        findlogforcheckout(str(stdID),str(b_id),logs)
                        #sub menu option and input option
                        print("\n")
                        print("(A) If book is available for loan, enter a.")
                        print("(B) If it is not available for loan, to reserve the book,enter b.")
                        print("(C) If it is reserved by the same student who is trying to loan the book, enter c.")
                        print("(D) If it is reserved by the same student who is trying to loan the book,\
but the book is still on loan, enter d.")
                        print("\n")
                        userinput=input("Please select an option from above:")
                        print("\n")

                        #Check out when book is available for loan
                        if userinput=="a" or userinput=="A":
                            checkout_date=input("Please enter today's date: ")
                            add_log(str(b_id),"-",checkout_date,"-",str(stdID),logs)
                    
                        #Check out when book has to be reserved
                        elif userinput=="b" or userinput=="B":
                            reservation_date=input("Please enter today's date: ")
                            reserve_book(str(b_id),reservation_date,"-","-",str(stdID),logs)

                        #Check out when book is reserved by student
                        elif userinput=="c" or userinput=="C":
                            checkout_date=input("Please enter today's date: ")
                            update_log(str(b_id),None,str(checkout_date),"-",str(stdID),logs)

                        #Check out when book is reserved by student but the book is on loan
                        elif userinput=="d" or userinput=="D":
                            print("The book is still on loan, we will let you know when it is available.")
                    
                        else:
                            print("\nYou have selected an incorrect option")
                    else:   
                        print("\nThis is an invalid Book ID.Please try again.")
                else:
                    print("\nThis is an invalid Book ID.Please try again.")
            else:
                print("\nThis is an invalid Student ID.Please try again.")
        else:
            print("This is an invalid Student ID.Please try again.")



def return_book():
    '''
    command to return a book
    requires two inputs to do the functionality of finding logs for return
    - student id
    - book id
    '''
    #Student ID check
    stdID=input("\nPlease enter the student's ID ")
    if stdID.isnumeric():
        stdID=int(stdID)
        if stdID<=9999 and stdID>=1000:
            #Book ID check
            b_id=input("\nPlease enter the Book ID ")
            if b_id.isnumeric():
                b_id=int(b_id)
                if b_id>=1 and b_id<=20:
                    #calls the function to find logs for return and if found, return date must be an input and updates logs
                    if findlogforreturn(str(b_id),str(stdID),logs):
                        return_date=input("\nPlease enter today's date")
                        updatelog_return(str(b_id),None,None,str(return_date),str(stdID),logs)
                    #if the record is not found, an error message is displayed
                    else:
                        print("\nThis book cannot be returned. Please check your inputs again.")
                else:
                    print("\nThis is an invalid Book ID. Please try again.")
            else:
                print("\nThis is an invalid Book ID. Please try again.")
        else:
            print("\nThis is an invalid Student ID. Please try again.")
    else:
        print("\nThis is an invalid Student ID. Please try again.")



def select_books():
    '''
    command to select book for purchase order
    a graph is drawn given no input paramaters
    and a budget ratio is provided.
    '''
    budget=input("\nPlease enter the budget to purchase books(Enter only numbers): ")
    #budget check
    if budget.isnumeric():
        budget=int(budget)
        showGraph(budget)
    else:
        print("\nInvalid budget. Please try again.")
    


#################################################
#------------------MAIN-------------------------#
#################################################

#creating the tkinter interface
    
window=Tk()
window.title("Library Management System")
window.geometry("400x300")
window.configure(bg='black')

#Creating all GUI components and giving commands to each of my buttons

lblLibrary=Label(window, text="Please Select an Option from Below;", height=1, width=50).pack()
btnHello=Button(window,text="Please Click Here to Begin",command=say_hello,height=2, width=20).pack()
btnSearch=Button(window,text="Search a Book by its Title",command= search_book,height=2, width=20).pack()
btnCheckout=Button(window,text="Checkout a Book", command= checkout_book,height=2, width=20).pack()
btnReturn=Button(window,text="Return a Book", command= return_book,height=2, width=20).pack()
btnSelect=Button(window, text="Select Books for Purchase Order", command= select_books,height=2, width=20).pack()
btnBye=Button(window, text= "Quit", command= say_bye,height=2, width=20).pack()

#This will loop through my GUI

window.mainloop()
