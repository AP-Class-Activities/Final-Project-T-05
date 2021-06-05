import math
class Product:
    def __init__(self,id,name,company,price,point,specifications):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__price = price
        self.__point = point
        self.__specifications = specifications
         
        if point > 5 or point < 0:
            raise ValueError('the Product price should be in range 0 ... 5')
        self.__point = point
   
    @property
    def id(self):
        return self.__id   
    @id.setter
    def id(self,value):
        self.__id = value
    
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
    
    def __str__(self):
        return 'ID:PR{}   NAME_PRODUCT: {}    COMPANY: {}   PRICE: {}Toman   POINT: {}   SPECIFICATIONS: {}'\
            .format(self.id,self.name,self.company,self.price,self.point,self.specifications)

'''

c = Product('563258','khorma','golestan',1700,3,'baste bandi ziba')
print(c)


''' 
class storeroom(Product):
    def __init__(self,id ,name ,company , price , point , specifications , mojodi):
        super(storeroom,self).__init__(id , name , company , price , point , specifications)
        self.__mojodi = mojodi
    
    @property
    def mojodi(self):
        return self.__mojodi
    @mojodi.setter
    def mojodi(self,value):
        self.__mojodi = value

    def __str__(self):
      return super(storeroom,self).__str__() + ' AVAILABLE : {} '.format(self.mojodi)


p = storeroom('563258','khorma','golestan',1700,3,'baste bandi ziba',100)
print(p)
        