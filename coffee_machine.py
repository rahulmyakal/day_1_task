Tot_water = 1000
Tot_milk = 1000
Tot_coffee = 1000
class CoffeeMachine:
    '''
    This is a coffee machine.
    '''
    def __init__(self,name):
        self.name=name
        self.money=0

    def resource_check(self,water,milk,coffee):
        global Tot_water
        global Tot_milk
        global Tot_coffee
        self.water,self.milk,self.coffee=water,milk,coffee
        if Tot_water >= self.water:
            if Tot_milk >=self.milk :
                if Tot_coffee >= self.coffee :
                    Tot_water=Tot_water-self.water
                    Tot_milk=Tot_milk-self.milk
                    Tot_coffee=Tot_coffee-self.coffee
                    return True
                else:
                        print("Sorry! There is no sufficient coffee powder")
                        return False
            else:
                    print("Sorry! There is no sufficient Milk")
                    return False
        else:
                print("Sorry! There is no sufficient Water")
                return False
    def report(self,mon):
        self.mon=mon   
        rep="Here is report"
        print(rep.center(50,"-"))
        print("Water:",Tot_water,"ml")
        print("Milk:",Tot_milk,"ml")
        print("Coffee:",Tot_coffee,"gm")
        print(f"Money: ${self.mon}")
    def payment(self):
            st="Insert Coins" 
            print(st.center(50,"-"))
            quarter,dimes,nickles,pennies,=int(input("Quarter:")),int(input("Dimes:")),int(input("Nickles:")),int(input("Pennies:"))
            cus_money=0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies
            if cus_money ==self.money:
                print("Your Payment is successful")
                return True
            elif    cus_money >=self.money:
                self.money = cus_money - self.money
                print("Your payment is sucsessful")
                print(f"Collect your change ${self.money:.2f} dollars")
                return True
            else:
                print("Sorry!! You don't have enough money")
                print(f" Sorry your money is refunded{cus_money:.2f}")
                return False
    def make_coffee(self):
        print(f"------Here is your {self.name}.Enjoy!------")
        return True
def repo(mon):
    want=input("Do you want the report ? Yes or No\t")
    if want in["YES","yes","Y","y"]:
        return obj.report(mon)
    else:
        pass

str="Hellooo!!! Welcome to AJAY RAM COFFEE CAFE"
print(str.center(51,"-"))
while True:
    machine = input("Enter the code(on or off):")
    if machine=="on":
        while True:
            choice=int(input("What would you like to drink?\n1.Espresso\n2.Latte\n3.Cappuccino\t"))
            if choice==1:
                obj=CoffeeMachine("Espresso")
                repo(0)
                obj.money=3.5
                if obj.resource_check(50,225,20)==True:
                   if obj.payment()==True:
                       if obj.make_coffee()==True:
                           repo(3.5)

            elif choice==2:
                obj=CoffeeMachine("Latte")
                repo(0)
                obj.money=4.5
                if obj.resource_check(50,200,16)==True:
                   if obj.payment()==True:
                       if obj.make_coffee()==True:
                           repo(4.5)
            elif choice==3:
                obj=CoffeeMachine("Cappuccino")
                repo(0)
                obj.money=6.5
                if obj.resource_check(50,200,20)==True:
                   if obj.payment()==True:
                       if obj.make_coffee()==True:
                           repo(6.5)
            else:
                print("Sorry!!..Please Enter the correct choice")

            cont=input("Do you wanna continue to enjoy our coffee: YES or NO")
            if cont in["YES","yes","Y","y"]:
                pass
            else:
                break
        a="Visit Again for more fun!!!"
        print(a.center(40,"*"))
    else:
        print("Machine is offed for maintenance")
        break