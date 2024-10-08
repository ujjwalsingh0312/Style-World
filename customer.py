'''
ABOUT CUSTOMER_MODULE
This module is for
Functions in module
1) add_customer()
2) display_customer()
3) search1_customer(Cst_id)
4) search2_customer(Cst_name)
5) update_customer(Cst_id)
6) delete_customer(Cst_id)
'''
import mysql.connector as ms
db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")
def add_customer():
    '''
    OBJECTIVE:- To add one record in customer product
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    Cst_id=input("Enter customer ID ")
    Cst_name=input("Enter customer name ")
    Address=input("Enter customer's address ")
    Contact=input("Enter customer's contact number ")
    Email=input("Enter customer's email ")
    cur1=db1.cursor()
    query="insert into customer (Cst_id, Cst_name, Address, Contact, Email) VALUES ('%s','%s','%s','%s','%s')" %(Cst_id, Cst_name, Address, Contact, Email)
    cur1.execute(query)
    db1.commit()
    cur1.close()
    print ("Row inserted in cuatomer table")

def display_customer():
    '''
    OBJECTIVE:- To display all the records of table customer
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("select * from customer")
    records=cur1.fetchall()
    
    print("Cst_id\t\tCst_name\t\tAddress\t\tContact\t\tEmail")
    for row in records:
        print(row[0], "\t\t", row[1], "\t\t", row[2], "\t\t", row[3], "\t\t", row[4])
    db1.commit()
    cur1.close()

def search1_customer(Cst_id):
    '''
    OBJECTIVE:- To search a record from table customer
    INPUT PARAMETERS:- CUSTOMER ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("""select * from customer
                    where Cst_id='%s'""" %Cst_id)
    record=cur1.fetchone()
    if record==None:
        return 0
        #print("Record not found")
    else:
        return record
        #print(record)
    db1.commit()
    cur1.close()

def search2_customer(Cst_name):
    '''
    OBJECTIVE:- To search record(s) from table customer
    INPUT PARAMETERS:- CUSTOMER NAME
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("""select * from customer
                    where Cst_name='%s'""" %Cst_name)
    records=cur1.fetchall()
    if records==None:
        print("Record not found")
    else:
        for row in records:
            print("Cst_id ", row[0])
            print("Cst_name ", row[1])
            print("Address ", row[2])
            print("Contact ", row[3])
            print("Email ", row[4])
    db1.commit()
    cur1.close()

def update_customer(Cst_id):
    '''
    OBJECTIVE:- To update record(s) from table customer
    INPUT PARAMETERS:- CUSTOMER ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    print("Enter new information\t")
    Cst_name=input("Enter (new) customer name ")
    Address=input("Enter (new) customer's address ")
    Contact=input("Enter (new) customer's contact number ")
    Email=input("Enter (new) customer's email ")
    cur1.execute("update customer set Cst_name='%s', Address='%s', Contact='%s', Email='%s' where Cst_id='%s'" \
                  %(Cst_name, Address, Contact, Email,Cst_id))
    db1.commit()
    cur1.close()
    print("Record updated")

def delete_customer(Cst_id):
    '''
    OBJECTIVE:- To delete record(s) from table customer
    INPUT PARAMETERS:- CUSTOMER ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("delete from customer where Cst_id='%s'" \
                  %(Cst_id))
    db1.commit()
    cur1.close()
    print("Record deleted")
    

'''
ans="y" or "Y"
while ans=="y" or ans=="Y":
    add_customer()
    ans=input("Do you want to add more records? y/n ")
      
display_customer()
    
ans="y" or "Y"
while ans=="y" or ans=="Y":
    Cst_id=input("Enter customer id to be searched ")
    search1_customer(Cst_id)
    ans=input("Do you want to search any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Cst_name=input("Enter customer name to be searched ")
    search2_customer(Cst_name)
    ans=input("Do you want to search any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Cst_id=input("Enter customer id to be updated ")
    update_customer(Cst_id)
    ans=input("Do you want to update any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Cst_id=input("Enter customer id to be deleted ")
    delete_customer(Cst_id)
    ans=input("Do you want to update any other record? y/n ")
'''
