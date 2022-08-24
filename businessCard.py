from faker import Faker

class businessCard:
    def __init__(self, name, second_name, company_name, position, email):
        self.name = name
        self.second_name = second_name
        self.company_name = company_name
        self.position = position
        self.email = email

       

    #def __str__(self):
     #   return 'firstname: {}, secondname: {}, email: {}'.format(self.name,self.second_name,self.email)

    #def __repr__(self):
      #  return 'firstname: {}, secondname: {}, email: {}'.format(self.name,self.second_name,self.email)

    def contact(self):
        return "Kontaktuje się z:  {}, {}, {}, {}" .format(self.name ,self.second_name, self.position ,self.email)   
        
   

fk=Faker()
     
card_1=businessCard("Rafał", "Kucharski", "Adiatic Solution","Audio control engineer","RafałKucharski@dayrep.com")
card_2=businessCard("Maciej", "Iwańczuk", "Bose Audio System", "salsman", "MaciejIwanczuk@gmail.com")
card_3=businessCard("Dorota", "Maciejewska", "National Record Mart", "Secondary school teacher", "DorotaMaciejewska@teleworm.us")
card_4=businessCard("Elżbieta", "Król", "Four Leaf Clover", "EEO representative", "ElzbietaKrol@armyspy.com")
card_5=businessCard("Gracja", "Nowak", "Budget Power", "Credit reporter", "Gracjanowak@dayrep.com")
card_6=businessCard("Michał", "Antoniak","DrLift","selsman","Antoniak@gmail.com")




class Customer:
    def __init__(self, first_name, address, email):
        self.first_name = first_name
        self.address = address
        self.email = email
    def __repr__(self):
        return 'first_name: {}, address: {}, email: {}'.format(self.first_name, self.address, self.email)    

customer1 = Customer(fk.first_name(),fk.address(),fk.email())  #drukowanie classy customer



list = [card_1,card_2,card_3,card_4,card_5,card_6]

#for i in list:
 #   print(i.name ,i.second_name , i.email)   


#print(loopreturn(card_1))



byname = sorted(list, key=lambda name: name.name)                                 # sortowanie listy
bysecond_name = sorted(list, key=lambda surname: surname.second_name)
byemail = sorted(list, key=lambda email: email.email,reverse=True)


#print(byemail)

print(card_1.contact())