from random import seed
from random import randint
class Product:
    def __init__(self,id,name,company,price,point,specifications,avalible):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__price = price
        self.__point = point
        self.__specifications = specifications
        self.__avalible = avalible

        if point > 5 or point < 0:
            raise ValueError('the Product price should be in range 0 ... 5')
        self.__point = point
        
        if avalible == 0:
            raise ValueError('the product is empty')
        self.__avalible = avalible
   
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value1):
        seed(1)
        for _ in range(1):
            value1 = randint(100000,1000000)
        self.__id = value1
    
    @property
    def name(self):
        return self.__name    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def company(self):
        return self.__company    
    @company.setter
    def company(self,value):
        self.__company = value
    
    @property
    def price(self):
        return self.__price    
    @price.setter
    def price(self,value):
        self.__price = value

    @property
    def point(self):
        return self.__point    
    @point.setter
    def point(self,value):
        if point > 5 or point < 0:
            raise ValueError('the Product price should be in range 0 ... 5')
        self.__point = value

    @property
    def specifications(self):
        return self.__specifications    
    @specifications.setter
    def specifications(self,value):
        self.__specifications = value
    
    @property
    def avalible(self):
        return self.__avalible    
    @avalible.setter
    def avalible(self,value):
        self.__avalible = value

    def __str__(self):
        return 'ID:PR{}   NAME_PRODUCT: {}    COMPANY: {}   PRICE: {}Toman   POINT: {}   SPECIFICATIONS: {}  AVALIBLE: {}'\
            .format(self.id,self.name,self.company,self.price,self.point,self.specifications,self.avalible)
'''

c = Product(randint(100000,1000000),'khorma','golestan',1700,3,'baste bandi ziba','100')
print(c)

'''
