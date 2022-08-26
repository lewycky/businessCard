
import email
from turtle import pos, position
from faker import Faker

fk=Faker()


class businessCard:
    def __init__(self, name, second_name, company_name, position, email):
        self.name = name
        self.second_name = second_name
        self.company_name = company_name
        self.position = position
        self.email = email

        #property
        self._length = (len(self.name)) + len("   ") + (len(self.second_name))
    
    def __str__(self):
        return 'firstname: {}, secondname: {}, email: {}'.format(self.name,self.second_name,self.email)

    def __repr__(self):
        return 'firstname: {}, secondname: {}, email: {}'.format(self.name,self.second_name,self.email)
    
    def contact(self):
        return "dzwonię do {} {}," .format(self.name ,self.second_name)   

    @property
    def length(self):   
       return self._length

    @length.getter
    def length(self):
        return f"Długość znaków to {self._length}"   

   



class BaseContact(businessCard):    
    def __init__(self, private_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_number = private_number
    def contact(self, *args, **kwargs):
        return f"Wybieram numer {self.private_number} i {super().contact(*args, **kwargs)}"
    @property   
    def length(self):
        return super().length 
       
        

class BusinessContact(businessCard):
    def __init__(self, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.business_phone = business_phone 
    def contact(self, *args, **kwargs):
        return f"Wybieram numer {self.business_phone} i {super().contact(*args, **kwargs)}"    
    @property   
    def length(self):
        return super().length          
        

 
card_1=businessCard(name="Rafał", second_name="Kucharski", company_name="Adiatic Solution",position="Audio control engineer",email="RafałKucharski@dayrep.com")
card_2=businessCard(name="Maciej",second_name= "Iwańczuk",company_name= "Bose Audio System",position= "salsman", email= "MaciejIwanczuk@gmail.com")
card_3=businessCard(name="Dorota",second_name= "Maciejewska", company_name="National Record Mart",position= "Secondary school teacher", email="DorotaMaciejewska@teleworm.us")
card_4=businessCard(name="Elżbieta", second_name="Król", company_name= "Four Leaf Clover",position= "EEO representative",email= "ElzbietaKrol@armyspy.com")
card_5=businessCard(name="Gracja",second_name= "Nowak",company_name= "Budget Power", position="Credit reporter", email="Gracjanowak@dayrep.com")
card_6=businessCard(name="Michał",second_name= "Antoniak",company_name="DrLift",position="selsman",email="Antoniak@gmail.com")

card_7=BaseContact(name="Józef", second_name="Kowalczyk", company_name="Ultimate Fighting Championship", position="Accountant", email="Ufc@yahooo.com", private_number=800212312)
card_8=BusinessContact(name="Paulinka", second_name= "Fryda", company_name="Lewycky Technology Solution", position="CEO", email="PaulaFrytka@lewycky.com", business_phone=328121432)

card_9=BusinessContact(name=fk.first_name(), second_name=fk.last_name(), company_name=fk.company(), position=fk.job(), email=fk.email(), business_phone=fk.phone_number() )

#print(card_9)

def create_contacts(kind, amount):

        list = []
        for i in range(amount):
            if kind == "business":
                list.append(BusinessContact)
            elif kind == "base":
                list.append(BaseContact) 
        return list

if __name__== "__main__":
    kind = input("select the type of business card: business/base :")
    amount=int(input("select number of cards: "))
    list= create_contacts(kind, amount)
    print(list)




#print(create_contacts())

#print(card_8.length)
#print(card_8.contact())



# Dodatkowa klasa do pobierania danych z FAKERA
class Customer:
    def __init__(self, first_name, address, email):
        self.first_name = first_name
        self.address = address
        self.email = email
    def __repr__(self):
        return 'first_name: {}, address: {}, email: {}'.format(self.first_name, self.address, self.email)    


random_user = Customer(fk.first_name(),fk.address(),fk.email()) 

def create_contacts(value):
        for i in range(value): 
            print(random_user)       
            


list = [card_1,card_2,card_3,card_4,card_5,card_6]

#for i in list:
 #   print(i.name ,i.second_name , i.email)   


byname = sorted(list, key=lambda name: name.name)                                 # sortowanie listy
bysecond_name = sorted(list, key=lambda surname: surname.second_name)
byemail = sorted(list, key=lambda email: email.email,reverse=True)

#print(byemail)


#print(len(card_1.name)+len(card_1.second_name))
