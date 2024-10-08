'''
ABOUT ORDERS_MODULE
This module is for
Functions in module
1) add_orders()
2) display_orders()
3) update_orders(Ord_id)
4) delete_orders(Ord_id)
'''
import product
import customer
import mysql.connector as ms
db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")

def add_orders():
    '''
    OBJECTIVE:- To add one record in table orders and genrate the bill
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    
    Ord_id=input("Enter order id ")
    Cst_id=input("Enter customer id ")
    res=customer.search1_customer(Cst_id)
    if res==0:
        print("Invalid customer ID")
        print("Enter again")
    else:
        Pdt_id=input("Enter product id ")
        res=product.search1_product(Pdt_id)
        if res==0:
            print("Invalid product ID")
        else:
            Qty=int(input("Enter quantity of the product "))
            Discount=int(input("Enter discount "))
    
            cur1=db1.cursor()
            cur1.execute("select P.Price from product P where P.Pdt_id='%s'"%Pdt_id)
            Tprice=cur1.fetchone()
            val=Tprice[0]
            Amt=val*Qty
            Amount=Amt-(Amt*(Discount/100))
    
            cur2=db1.cursor()
            cur2.execute("insert into orders (Ord_id, Cst_id, Pdt_id, Qty, Discount, Amount) VALUES ('%s','%s','%s',%d,%d,%d)" %(Ord_id, Cst_id, Pdt_id, Qty, Discount, Amount))
            db1.commit()
            print("Record saved")
            res=input("Do you want to generate bill? (y/n) ")
            if res=="y" or res=="Y":
                cur3=db1.cursor()
                cur3.execute("""select * from orders
                            where Ord_id='%s'""" %Ord_id)
                row=cur3.fetchone()
                print("Ord_id\t\tCst_id\t\tPdt_id\t\tQuantity\t\tDiscount\t\tAmount")
                print(row[0], "\t\t", row[1], "\t\t", row[2], "\t\t", row[3], "\t\t\t", row[4], "\t\t\t", row[5])
            else:
                print("Thank you")
            db1.commit()
            cur1.close()
            cur2.close()
            cur3.close()

def display_orders():
    '''
    OBJECTIVE:- To display all the orders from table orders
    INPUT PARAMETERS:- NONE
    RETURN TYPE:- NONE
    '''
    cur1=db1.cursor()
    cur1.execute("select * from orders")
    rec=cur1.fetchall()
    print("Ord_id\t\tCst_id\t\tPdt_id\t\tQuantity\t\tDiscount\t\tAmount")
    for row in rec:
        print(row[0], "\t\t", row[1], "\t\t", row[2], "\t\t\t", row[3], "\t\t\t", row[4], "\t\t", row[5])
    db1.commit()
    cur1.close()
    
def update_orders(Ord_id):
    '''
    OBJECTIVE:- To update record(s) from table orders
    INPUT PARAMETERS:- ORDERS ID
    RETURN TYPE:- NONE
    '''
    cur4=db1.cursor()
    print("Enter new information\t")
    Cst_id=input("Enter (new) customer ID ")
    Pdt_id=input("Enter (new) product ID ")
    Qty=int(input("Enter (new) quantity of product "))
    Discount=int(input("Enter (new) discount given "))
    cur2=db1.cursor()
    cur2.execute("select P.Price from product P where P.Pdt_id='%s'"%Pdt_id)
    Tprice=cur2.fetchone()
    val=Tprice[0]
    Amt=val*Qty
    Amount=Amt-(Amt*(Discount/100))
    cur4.execute("update orders set Cst_id='%s', Pdt_id='%s', Qty=%d, Discount=%d, Amount=%d where Ord_id='%s'" \
                  %(Cst_id, Pdt_id, Qty, Discount, Amount, Ord_id))
    db1.commit()
    cur4.close()
    cur2.close()
    print("Record updated")

def delete_orders(Ord_id):
    '''
    OBJECTIVE:- To delete record(s) from table orders
    INPUT PARAMETERS:- ORDERS ID
    RETURN TYPE:- NONE
    '''
    cur1=db1.cursor()
    cur1.execute("delete from orders where Ord_id='%s'" \
                  %(Ord_id))
    db1.commit()
    cur1.close()
    print("Record deleted")


