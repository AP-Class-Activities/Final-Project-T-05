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