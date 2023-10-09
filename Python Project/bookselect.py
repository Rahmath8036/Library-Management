#Written by F211372 on 15/12/2022

'''
This module does the function of depicting a graph of the number of books loaned
vs the genre. It gives the librarian the idea of the popular genre. After the budget input,
it splits the budget according to each genre to help the librarian purchase books. 
'''

import matplotlib.pyplot as plt
from database import *


def showGraph(budget):
    '''
    The functionality showGraph() is used to list the most popular genres so that the
    librarian could purchase books accordingly.
    It takes the budget as a parameter within this function.It firstly counts the number of times a particular
    book is loaned, likewise done for all 20 book records. Then it classified into their respective genres.
    A graph is produced considering the total number of loans for each genre vs the number of books loaned.
    The total logs are calculated. With this, a ratio is calculated for each genre.
    With this ratio the budget is split among each genres so the
    librarian can spend liekwise on each genre and a message is displayed.
    Requires one input within the function- the budget in pounds
    '''
    bookid1=[]
    bookid2=[]
    bookid3=[]
    bookid4=[]
    bookid5=[]
    bookid6=[]
    bookid7=[]
    bookid8=[]
    bookid9=[]
    bookid10=[]
    bookid11=[]
    bookid12=[]
    bookid13=[]
    bookid14=[]
    bookid15=[]
    bookid16=[]
    bookid17=[]
    bookid18=[]
    bookid19=[]
    bookid20=[]
    #Creates a list of logs for each Book ID 
    for log in logs:
        if log[0]=="1":
            bookid1.append(log)
        elif log[0]=="2":
            bookid2.append(log)
        elif log[0]=="3":
            bookid3.append(log)
        elif log[0]=="4":
            bookid4.append(log)
        elif log[0]=="5":
            bookid5.append(log)
        elif log[0]=="6":
            bookid6.append(log)
        elif log[0]=="7":
            bookid7.append(log)
        elif log[0]=="8":
            bookid8.append(log)
        elif log[0]=="9":
            bookid9.append(log)
        elif log[0]=="10":
            bookid10.append(log)
        elif log[0]=="11":
            bookid11.append(log)
        elif log[0]=="12":
            bookid12.append(log)
        elif log[0]=="13":
            bookid13.append(log)
        elif log[0]=="14":
            bookid14.append(log)
        elif log[0]=="15":
            bookid15.append(log)
        elif log[0]=="16":
            bookid16.append(log)
        elif log[0]=="17":
            bookid17.append(log)
        elif log[0]=="18":
            bookid18.append(log)
        elif log[0]=="19":
            bookid19.append(log)
        else:
            bookid20.append(log)
    
    #Counts the elements of each list having the same book ID       
    if bookid1!=[]:
        id1=(sum(isinstance(i, list) for i in bookid1))

    if bookid2!=[]:
        id2=(sum(isinstance(i, list) for i in bookid2))

    if bookid3!=[]:
        id3=(sum(isinstance(i, list) for i in bookid3))

    if bookid4!=[]:
        id4=(sum(isinstance(i, list) for i in bookid4))

    if bookid5!=[]:
        id5=(sum(isinstance(i, list) for i in bookid5))

    if bookid6!=[]:
        id6=(sum(isinstance(i, list) for i in bookid6))

    if bookid7!=[]:
        id7=(sum(isinstance(i, list) for i in bookid7))

    if bookid8!=[]:
        id8=(sum(isinstance(i, list) for i in bookid8))

    if bookid9!=[]:
        id9=(sum(isinstance(i, list) for i in bookid9))

    if bookid10!=[]:
        id10=(sum(isinstance(i, list) for i in bookid10))

    if bookid11!=[]:
        id11=(sum(isinstance(i, list) for i in bookid11))

    if bookid12!=[]:
        id12=(sum(isinstance(i, list) for i in bookid12))

    if bookid13!=[]:
        id13=(sum(isinstance(i, list) for i in bookid13))

    if bookid14!=[]:
        id14=(sum(isinstance(i, list) for i in bookid14))
        
    if bookid15!=[]:
        id15=(sum(isinstance(i, list) for i in bookid15))

    if bookid16!=[]:
        id16=(sum(isinstance(i, list) for i in bookid16))

    if bookid17!=[]:
        id17=(sum(isinstance(i, list) for i in bookid17))

    if bookid18!=[]:
        id18=(sum(isinstance(i, list) for i in bookid18))

    if bookid19!=[]:
        id19=(sum(isinstance(i, list) for i in bookid19))

    if bookid20!=[]:
        id20=(sum(isinstance(i, list) for i in bookid20))


    #Catergorizes the Book IDs to their respective genre
    genreSciFi=id1+id7+id8+id9+id10
    genreRomance=id2+id3+id5+id11+id12+id13+id14+id15+id16
    genreFantasy=id4+id6+id17
    genreYoungAdult=id18+id19+id20
    totalLoans=genreSciFi+genreRomance+genreFantasy+genreYoungAdult
    
    #Calculates the ratio for each genre using the total logs
    sciFiRatio=genreSciFi/totalLoans
    romanceRatio=genreRomance/totalLoans
    fantasyRatio=genreFantasy/totalLoans
    youngAdultRatio=genreYoungAdult/totalLoans
    
    #Prepares the data for the grapgh
    loanrecords=[genreSciFi,genreRomance,genreFantasy,genreYoungAdult]
    genre=['Sci-Fi','Romance','Fantasy','Young-Adult']
    
    #The budget is split according to the ratio and a message is displayed
    moneyForSciFi=sciFiRatio*budget
    moneyForRomance=romanceRatio*budget
    moneyForFantasy=fantasyRatio*budget
    moneyForYoungAdult=youngAdultRatio*budget
    print("\nDear Librarian, please see below for the respective genre's estimated budget; \n\n£%d on Sci-Fi \n£%d on Romance \n£%d on Fantasy \n£%d on Young-Adult."%(moneyForSciFi,moneyForRomance,moneyForFantasy,moneyForYoungAdult))
    
    #Plotting of graph
    plt.bar(genre,loanrecords)
    plt.xlabel('Genres')  
    plt.ylabel('No: of Books Loaned')
    plt.title('Popularity of genres based on the number of books loaned.')
    plt.show()


if __name__=="__main__":
    '''
    Testing for bookselect.py, requires an input (budget) within the function.
    It works.
    '''
    budget=int(10000)
    getBookRecords()
    readLogs()
    showGraph(budget)
