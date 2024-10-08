from tkinter import *
from tkinter import ttk
import mysql.connector as ms
from final_menu import mainmenu

def login_1():
    '''
    Objective: Insert some tuples in user table
    Input Parameters: None
    Return Value: None
    '''
    db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")
    cur1=db1.cursor()

    master = Tk()
    master.title("STYLE WORLD")
    w, h = master.winfo_screenwidth(), master.winfo_screenheight()
    master.geometry("%dx%d+0+0" % (w, h))
    
    Label(master,text='UserID').grid(row=11)
    e1 = Entry(master)
    Label(master,text='Username').grid(row=12)
    e2 = Entry(master)

    e1.grid(row=11,column=1)
    e2.grid(row=12,column=1)

    def searchCommand():
        userID=e1.get()
        username=e2.get()
        #print(userID, " " , username)

        commandStr = "select * from login_page where UserID= '%s' and Username='%s'" %(userID,username)
        cur1.execute(commandStr)
        res=cur1.fetchone()

        if cur1.rowcount >=1:
            print("You are valid user")
            
            master.destroy()
            mainmenu()
            
        else:
            print("User does not exist")
            master.destroy()

    button1 = ttk.Button(master, text='LOGIN', command=searchCommand).grid(row=13,column=1)  
    
    master.mainloop()

def main():
    '''
    Objective: To insert the records using user interface. 
    Input Parameter: None
    Return Value: None
    '''   
    login_1()
    
if __name__=='__main__':
    main()
    
    
