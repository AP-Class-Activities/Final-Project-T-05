class seller:
    def __init__(self, name , id , state , city , addres , phone):
        self.__name = name
        self.__id = id
        self.__state = state
        self.__city = city
        self.__addres = addres
        self.__phone = phone

        if len(phone) > 11 or len(phone) < 11:
            raise ValueError('the phone number not available')
        self.__phone = phone

    @property
    def name(self):
        return self.__name    
    @name.setter
    def name(self,value):
        self.__name = value
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value
    
    @property
    def state(self):
        return self.__state    
    @state.setter
    def state(self,value):
        self.__state = value

    @property
    def city(self):
        return self.__city    
    @city.setter
    def city(self,value):
        self.__city = value

    @property
    def addres(self):
        return self.__addres    
    @addres.setter
    def addres(self,value):
        self.__addres = value

    @property
    def phone(self):
        return self.__phone    
    @phone.setter
    def phone(self,value):
        self.__phone = value

    def __str__(self): 
        return 'ID:SL{}   NAME:Shop {}    ADDRES: {} {} {}    PHONE: {}'\
            .format(self.id,self.name, self.state, self.city , self.addres, self.phone)

a = seller('mac',35651,'guilan','rasht','takhti','01332113307')