class Money:
    
    def __init__(self, curtype, curvalue):
        self.curtype = curtype
        self.curvalue = curvalue


    def Revert_Currency(self):   
        if(self.curtype == "WON"):
            Revert_value = 33.72
            str = "WON"
        elif(self.curtype == "USD"):
            Revert_value = 0.028
            str = "USD"
        elif(self.curtype == "YEN"):
            Revert_value = 3.4
            str = "YEN"
        else:
            print("Currency Type Incorrect")

        Result_revert =  Revert_value*int(self.curvalue)
        return  "Number of converted : ",Result_revert ,str
         
    


Input_Money_THB = input("Please enter money: ")
print("Please Enter Convert To Currency Type (WON , USD or YEN) :")

Input_Currency_Type = input("input Currency Type: ")



Money_THB = Money(Input_Currency_Type,Input_Money_THB)


print(Money_THB.Revert_Currency())


#class test
Money_THB_to_WON = Money("WON",10000)
print(Money_THB_to_WON.Revert_Currency())


Money_THB_to_USD = Money("USD",10000)
print(Money_THB_to_USD.Revert_Currency())


Money_THB_to_YEN = Money("YEN",10000)
print(Money_THB_to_YEN.Revert_Currency())