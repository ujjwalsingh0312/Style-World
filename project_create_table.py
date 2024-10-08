def create_product():
    a="""create table product
    (Pdt_id varchar(10) NOT NULL PRIMARY KEY,
     Pdt_name varchar(20),
     Gender char(1) DEFAULT 'F' ,
     Price int )"""
    cur1.execute(a)
    print("Table product created")
    return
def create_customer():
    b="""create table customer
    (Cst_id varchar(10) NOT NULL PRIMARY KEY,
     Cst_name varchar(20),
     Address varchar(30) NOT NULL,
     Contact varchar(10),
     Email varchar(30))"""
    cur1.execute(b)
    print("Table customer created")
    return
def create_orders():
    c="""create table orders
    (Ord_id varchar(10) NOT NULL PRIMARY KEY,
     Cst_id varchar(10) NOT NULL ,
     Pdt_id varchar(20) NOT NULL ,
     Qty int,
     Discount int,
     Amount decimal(9,2),
     FOREIGN KEY (Pdt_id) REFERENCES product(Pdt_id),
     FOREIGN KEY (Cst_id) REFERENCES customer(Cst_id)
     )"""
    cur1.execute(c)
    print("Table orders created")
    return
def create_login_page():
    d="""create table login_page
    (UserID varchar(25),
     Username varchar(25))"""
    cur1.execute(d)
    print("Table Login Page created")
    return

import mysql.connector as ms
db1=ms.connect(host="localhost", user="root", passwd="1234", db="fashion")
cur1=db1.cursor()
if db1.is_connected():
    print(":)")
else:
    print(":(") 
create_product()
create_customer()
create_orders()
create_login_page()
