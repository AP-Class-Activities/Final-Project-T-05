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
        return 'ID: {} NAME: {} COMPANY: {} PRICE: {} POINT: {} SPECIFICATIONS: {}'\
            .format(self.id,self.name,self.company,self.price,self.point,self.specifications)





    
