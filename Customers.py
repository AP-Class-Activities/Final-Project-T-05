from random import seed
from random import randint
class Customers:
    def __init__(self, name , family , birthday_year , birthday_mounth , birthday_day , id , sex , state , city , addres , phone , postal_code):
        self.__name = name
        self.__family = family
        self.__year = birthday_year
        self.__mounth = birthday_mounth
        self.__day = birthday_day
        self.__id = id
        self.__sex = sex
        self.__state = state
        self.__city = city
        self.__addres = addres
        self.__phone = phone
        self.__postalcode = postal_code

        if birthday_year > 1400 or birthday_year < 1300: 
            raise ValueError('the year for a student should be in rnage 1395 ... 1400')
        self.__year = birthday_year

        if birthday_mounth > 12 or birthday_mounth < 0:
            raise ValueError('the Birthday mounth for a customers not in range 1....12')
        self.__mounth = birthday_mounth

        if birthday_day < 0 or birthday_day > 31:
            raise ValueError('the Birthday day for a customers not in range 1....31')
        self.__day = birthday_day

        if sex not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = sex
        
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
    def family(self):
        return self.__family    
    @family.setter
    def family(self,value):
        self.__family = value

    @property
    def year(self):
        return self.__year    
    @year.setter
    def year(self,value):
        if value > 1400 or value < 1300:
            raise ValueError('the Birthday years for a customers not in range 1300....1400')
        self.__year = value
    
    @property
    def mounth(self):
        return self.__mounth
    @mounth.setter
    def mounth(self,value):
        if value > 12 or value < 0:
            raise ValueError('the Birthday mounth for a customers not in range 1....12')
        self.__mounth = value

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self,value):
        if value < 0 or value > 31:
            raise ValueError('the Birthday day for a customers not in range 1....31')
        self.__day = value
    
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
    def sex(self): 
        return self.__sex
    @sex.setter
    def sex(self,value): 
        if value not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = value

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

    @property
    def postal_code(self):
        return self.__postalcode    
    @postal_code.setter
    def postal_code(self,value):
        self.__postalcode = value

    def __str__(self): 
        return 'ID:CU{}   name: {} {}    Birthday_date: {}/{}/{}   sex: {}   addres: {} {} {}    phone: {}  postal_code: {}'\
            .format(self.id,self.name, self.family, self.year, self.mounth, self.day, self.sex, self.state, self.city , self.addres, self.phone , self.postal_code)

'''

a =Customers('amir' , 'hesam' , 1376 , 10 , 30 , randint(100000,1000000) , 'male' , 'guilan' , 'rasht' , 'golsar' , '09113356268' , '235116')
print(a)

'''