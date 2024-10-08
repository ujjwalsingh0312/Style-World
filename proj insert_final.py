def insert_val_product():
    b="""insert into product values('P001','Handbag','F',15000), ('P002','Shoes','M',7000), ('P003','Belt','M',3000), ('P004','Kurti','F',2000),
                                                                ('P005','Shirt','F',4000), ('P006','Night Wear','F',1000), ('P007','One peice','F',3000), ('P008','Trousers','M',2000),
                                                                ('P009','Pants','M',1000), ('P010','Suit','M',8000), ('P011','Bag','U',2000), ('P012','Wallet','U',700)"""
    cur1.execute(b)
    db1.commit()
    print("Values added to table product")

def insert_val_customer():
    b="""insert into customer values('C001','Khanak','Vikaspuri','9988776655','xyz@gmail.com'), ('C002','Ananya','Dwarka Sector-13',' ','abc@gmail'),
                                                                   ('C003','Dipika','Uttam Nagar','4563798753',' '), ('C004','Priyanshi','Dabri Extension',' ','priyanshius@abccom'),
                                                                   ('C005','Mohit','GTB Nagar',' ','mohitabc@dfccom'), ('C006','Rahul','Tagore Garden','1258964302',' ')"""
    cur1.execute(b)
    db1.commit()
    print("Values added to table customer")

def insert_val_orders():
    b="""insert into orders values('Z001','C004','P002',1,0,7000), ('Z002','C002','P003',1,0,3000),
                                                             ('Z003','C002','P004',1,0,2000), ('Z004','C003','P004',2,0,4000)"""
    cur1.execute(b)
    db1.commit()
    print("Values added to table orders")

def  insert_val_login_page():
    b="insert into login_page values ('UJJWAL','SINGH'), ('NITIN', 'KUMAR')"
    cur1.execute(b)
    db1.commit()
    print("Values added to table login_page")

    
import mysql.connector as ms
db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")
cur1=db1.cursor()
if db1.is_connected():
    print(":)")
else:
    print(":(")
    
insert_val_product()
insert_val_customer()
insert_val_orders()
insert_val_login_page()
cur1.close()
db1.close()
