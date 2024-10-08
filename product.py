'''
ABOUT PRODUCT_MODULE
This module is for
Functions in module
1) add_product()
2) display_product()
3) search1_product(Pdt_id)
4) search2_product(Pdt_name)
5) update_product(Pdt_id)
6) delete_product(Pdt_id)
7) show_chart()
'''
import matplotlib.pyplot as plt
import mysql.connector as ms
db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")
    
def add_product():
    '''
    OBJECTIVE:- To add one record in table product
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    Pdt_id=input("Enter product ID ")
    Pdt_name=input("Enter product name ")
    Gender=input("For which gender the product is? (M, F, U) ")
    Price=int(input("Enter the price of the product "))
    cur1=db1.cursor()
    query="insert into product (Pdt_id, Pdt_name, Gender, Price) VALUES ('%s','%s','%s',%d)" %(Pdt_id, Pdt_name, Gender, Price)
    cur1.execute(query)
    db1.commit()
    cur1.close()
    print ("Row inserted in product table")

def display_product():
    '''
    OBJECTIVE:- To display all the records of table product
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("select * from product")
    records=cur1.fetchall()
    
    print("Pdt_id\t\tPdt_name\t\tGender\t\tPrice")
    for row in records:
        print(row[0], "\t\t", row[1], "\t\t\t", row[2], "\t\t", row[3])
    db1.commit()
    cur1.close()

def search1_product(Pdt_id):
    '''
    OBJECTIVE:- To search a record from table product
    INPUT PARAMETERS:- PRODUCT ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("""select * from product
                    where Pdt_id='%s'""" %Pdt_id)
    record=cur1.fetchone()
    #print("record in prod table", record)
    #return record
    if record==None:
        return 0
        #print("Record not found")
    else:
        return record
        #print(record)
    db1.commit()
    cur1.close()

def search2_product(Pdt_name):
    '''
    OBJECTIVE:- To search record(s) from table product
    INPUT PARAMETERS:- PRODUCT NAME
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("""select * from product
                    where Pdt_name='%s'""" %Pdt_name)
    records=cur1.fetchall()
    if records==None:
        print("Record not found")
    else:
        for row in records:
            print("Pdt_id ", row[0])
            print("Pdt_name ", row[1])
            print("Gender ", row[2])
            print("Price ", row[3])
    db1.commit()
    cur1.close()

def update_product(Pdt_id):
    '''
    OBJECTIVE:- To update record(s) from table product
    INPUT PARAMETERS:- PRODUCT ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    print("Enter new information\t")
    Pdt_name=input("Enter new product name ")
    Gender=input("For which gender the product is? (M, F, U) ")
    Price=int(input("Enter the new price of the product "))    
    cur1.execute("update product set Pdt_name='%s', Gender='%s', Price= %d where Pdt_id='%s'" \
                  %(Pdt_name, Gender, Price,Pdt_id))
    db1.commit()
    cur1.close()
    print("Record updated")

def delete_product(Pdt_id):
    '''
    OBJECTIVE:- To delete record(s) from table product
    INPUT PARAMETERS:- PRODUCT ID
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur1.execute("delete from product where Pdt_id='%s'" %(Pdt_id))
    db1.commit()
    cur1.close()
    print("Record deleted")

def show_chart1():
    '''
    OBJECTIVE:- To display bar chart Product VS Price
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''   
    cur1=db1.cursor()
    cur2=db1.cursor()
    x=[]
    y=[]    
    cur1.execute("select Price from product")
    rec1=cur1.fetchall()
    cur2.execute("select Pdt_name from product")    
    rec2=cur2.fetchall()
    for i in range(0,len(rec2)):
        x.append(rec2[i][0])
    for j in range(0,len(rec1)):
        y.append(rec1[j][0])
    plt.bar(x,y, color='pink')
    plt.xlabel("Product's Name")
    plt.ylabel("Price")
    plt.show()
    db1.commit()
    cur1.close()
    cur2.close()

def show_chart2():
    '''
    OBJECTIVE:- To display pie chart on the basis Gender
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    cur1=db1.cursor()
    cur2=db1.cursor()
    cur3=db1.cursor()
    cur1.execute("select Pdt_id from product where Gender='M'")
    rec1=cur1.fetchall()
    cur2.execute("select Pdt_id from product where Gender='F'")
    rec2=cur2.fetchall()
    cur3.execute("select Pdt_id from product where Gender='U'")
    rec3=cur3.fetchall()
    x=[len(rec1), len(rec2), len(rec3)]
    y=['For males', 'For female', 'Unisex products']
    clr=['pink', 'yellow', 'grey']
    plt.axis("equal")
    plt.pie(x, labels=y,  colors=clr, autopct="%1.1F%%")
    plt.show()
    
'''
ans="y" or "Y"
while ans=="y" or ans=="Y":
    add_product()
    ans=input("Do you want to add more records? y/n ")
     
display_product()
    
ans="y" or "Y"
while ans=="y" or ans=="Y":
    Pdt_id=input("Enter product id to be searched ")
    search1_product(Pdt_id)
    ans=input("Do you want to search any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Pdt_name=input("Enter product name to be searched ")
    search2_product(Pdt_name)
    ans=input("Do you want to search any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Pdt_id=input("Enter product id to be updated ")
    update_product(Pdt_id)
    ans=input("Do you want to update any other record? y/n ")

ans="y" or "Y"
while ans=="y" or ans=="Y":
    Pdt_id=input("Enter product id to be deleted ")
    delete_product(Pdt_id)
    ans=input("Do you want to update any other record? y/n ")
'''
