import product
import customer
import orders

def mainmenu():
    ans="y" or "Y"
    while ans=="y" or ans=="Y":
        print("MAIN MENU")
        print("1. Product Table")
        print("2. Customer Table")
        print("3. Orders Table")
        choice=int(input("Enter your choice "))
        if choice==1:
            ans="y" or "Y"
            while ans=="y" or ans=="Y":
                print("PRODUCT MODULE")
                print("1. Add a new product")
                print("2. Display all products")
                print("3. Search product on the basis of product ID")
                print("4. Search product on the basis of product name")
                print("5. Update product's information")
                print("6. Delete product")
                print("7. Display Bar Chart (Product VS Price)")
                print("8. Display Pie Chart (on the basis of Gender)")
                productchoice=int(input("Enter your choice "))
                if productchoice==1:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        product.add_product()
                        ans=input("Do you want to add more records? y/n ")
                elif productchoice==2:
                    product.display_product()
                elif productchoice==3:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Pdt_id=input("Enter product id to be searched ")
                        rec=product.search1_product(Pdt_id)
                        if rec==0:
                            print("Record not found")
                        else:
                            print(rec)
                        ans=input("Do you want to search any other record? y/n ")
                elif productchoice==4:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Pdt_name=input("Enter product name to be searched ")
                        product.search2_product(Pdt_name)
                        ans=input("Do you want to search any other record? y/n ")
                elif productchoice==5:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Pdt_id=input("Enter product id to be updated ")
                        product.update_product(Pdt_id)
                        ans=input("Do you want to update any other record? y/n ")
                elif productchoice==6:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Pdt_id=input("Enter product id to be deleted ")
                        product.delete_product(Pdt_id)
                        ans=input("Do you want to delete any other record? y/n ")
                elif productchoice==7:
                    product.show_chart1()
                elif productchoice==8:
                    product.show_chart2()
                else:
                    print("Invalid Choice")
                    continue
                ans=input("Do you want to go back in PRODUCT MODULE? (y/n) ")
        elif choice==2:
            ans="y" or "Y"
            while ans=="y" or ans=="Y":
                print("CUSTOMER MODULE")
                print("1. Add a new customer")
                print("2. Display all customers")
                print("3. Search customer on the basis of customer ID")
                print("4. Search customer on the basis of customer name")
                print("5. Update customer's information")
                print("6. Delete customer")
                customerchoice=int(input("Enter your choice "))
                if customerchoice==1:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        customer.add_customer()
                        ans=input("Do you want to add more records? y/n ")
                elif customerchoice==2:
                    customer.display_customer()
                elif customerchoice==3:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Cst_id=input("Enter customer id to be searched ")
                        rec=customer.search1_customer(Cst_id)
                        if rec==0:
                            print("Record not found")
                        else:
                            print(rec)
                        ans=input("Do you want to search any other record? y/n ")
                elif customerchoice==4:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Cst_name=input("Enter customer name to be searched ")
                        customer.search2_customer(Cst_name)
                        ans=input("Do you want to search any other record? y/n ")
                elif customerchoice==5:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Cst_id=input("Enter customer id to be updated ")
                        customer.update_customer(Cst_id)
                        ans=input("Do you want to update any other record? y/n ")
                elif customerchoice==6:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Cst_id=input("Enter customer id to be deleted ")
                        customer.delete_customer(Cst_id)
                        ans=input("Do you want to delete any other record? y/n ")
                else:
                    print("Ïnvalid choice")
                    continue
                ans=input("Do you want to go back in CUSTOMER MODULE? (y/n) ")
        elif choice==3:
            ans="y" or "Y"
            while ans=="y" or ans=="Y":
                print("ORDERS MODULE")
                print("1. Add a new order and generate bill")
                print("2. Display all orders")
                print("3. Update order's information")
                print("4. Delete order")
                orderchoice=int(input("Enter your choice "))
                if orderchoice==1:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        orders.add_orders()
                        ans=input("Do you want to add more records? (y/n) ")
                elif orderchoice==2:
                    orders.display_orders()
                elif orderchoice==3:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Ord_id=input("Enter order id to be updated ")
                        orders.update_orders(Ord_id)
                        ans=input("Do you want to update any other record? y/n ")
                elif orderchoice==4:
                    ans="y" or "Y"
                    while ans=="y" or ans=="Y":
                        Ord_id=input("Enter order id to be deleted ")
                        orders.delete_orders(Ord_id)
                        ans=input("Do you want to delete any other record? y/n ")
                else:
                    print("Ïnvalid choice")
                    continue
                ans=input("Do you want to go back in ORDERS MODULE? (y/n) ")
        ans=input("Do you want to go back in MAIN MENU? (y/n) ")
