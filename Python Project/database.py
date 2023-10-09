#Written by F211372 on 15/12/2022


'''
This is the module that interacts with my text files, logfile and book_info.
and also interacts with bookselect.py, booksearch.py, bookreturn.py and bookcheckout.py
'''

bookInfo=[]
def getBookRecords():
    '''
    This function reads the Book_Info.txt file and appends the records in the list bookInfo
    returns the Book Info back to the file so we can use it through our program
    No input parameters
    '''
    f = open("Book_Info.txt","r")
    for line in f:
        cleanrecord=line.strip() #strips off the \n  
        record=cleanrecord.split(":") #split the string
        bookInfo.append(record)

    f.close()
    return bookInfo



logs=[]
def readLogs():
    '''
    This function reads the logfile.txt and appends them in the list logs
    returns the logs back to the file so we can us eit through our program
    No input parameters
    '''
    f = open("logfile.txt","r")
    for line in f:
        cleanrecord=line.strip() #strips off the \n
        log=cleanrecord.split(":") #split the string
        logs.append(log) 

    f.close()
    return logs 



def savetransactionlog(logs):
    '''
    This functions writes back into the file to update/add a record taking the input parameter as logs.
    '''
    f=open("logfile.txt","w")
    for log in logs:
        newlog=str(log[0])+":"+str(log[1])+":"+str(log[2])+":"+str(log[3])+":"+str(log[4])+"\n" # creating the log
        f.write(newlog) #writing the new log
    f.close()


if __name__=="__main__":
    '''
    Testing Functionality for getBookRecords()
    '''
    print ("testing getBookRecords()")
    bookInfo=getBookRecords()
    print (bookInfo)
    
    
if __name__=="__main__":
    '''
    Testing Functionality for readLogs()
    '''
    print("testing readLogs()")
    logs=readLogs()
    print(logs)


    
