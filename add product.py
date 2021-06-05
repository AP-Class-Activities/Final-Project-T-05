from Product import Product
from random import seed
from random import randint

class addproduct:
    def addproducts():
        n = int(input("Enter the no.of.items need to be added : "))
        for i in range(n):
        new_id = randint(100000,1000000)
        new_Name = input("Enter Name : ")
        new_company = input("Enter company name :")
        new_available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        new_point = int(input('enter point :'))
        new_specifications = input("Enter specifications : ")
