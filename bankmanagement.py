from abc import ABC
from tabulate import tabulate
import random
class namee(ABC):
    def __init__(self,name , email , address,phone) -> None:
        self.name = name 
        self.email = email 
        self.address = address
        self.phone = phone
        


class User(namee):
    #1st qstn requirement
    def __init__(self, name, email, address,phone , AccountType) -> None:
        super().__init__(name, email, address,phone)
        self.AccountType = AccountType
        self.LoanTaka  = 0 
        self.TwoTimeLoan = []
    
        #2.Initially, the balance will be 0. An account number will be generated automatically
        self.__balance = 0
        self.AcountNumber = f"{self.email}{random.randint(1,100)}"

        self.Transaction_History_Record = []
        self.TakeLoan = 0 



    #3. Can deposit and withdraw amount.
    def withdrawal(self,BankName,money): #bankName Here Bank Object , Money - Withdrawal Amount
        if money>self.__balance:
            print(f"\t\t\t\t\nWithdrawal amount exceded")
        elif BankName.bankRupt == True :
            print(f"\t\t\t\t\nYour Bank Is bankrupt ... Because You created Account Laxmi Chit Fund Bank ")
        else:
            AvailableBalanceBeforeDeposite = self.__balance
            self.__balance -= money 
            BankName.AvalableBalance = (money * -1)
            transactionInfo  = f"Transaction Type : Debit\tAmount:{money}\tBalance After Transaction::{self.__balance}"
            self.Transaction_History_Record.append(transactionInfo)
            print(f"\t\t Heyy {self.name}\n")
            print(f"\t\tYou successfully Withdraw {money} Taka\n")

            print(f"\t\t Your Before Withdraw Amount {money} Your Bank Balance : {AvailableBalanceBeforeDeposite}")
            AfterAvailable_balance = self.__balance
            print(f"\t\t Your After Withdraw Amount {money} Taka, Your Bank Balance: {AfterAvailable_balance}")
                
    def deposite(self,BankName , Money , typee ):
        if BankName.bankRupt == True:
            print(f"\t\t\t\tYour Bank is Bankrupt...")
            return 
        self.__balance+=Money
        BankName.AvalableBalance = Money  
        # type = 'c'
        if 'c' == typee:
            transactionInfo  = f"Transaction Type : Credit\tAmount:{Money}\tBalance After Transaction::{self.__balance}"
            self.Transaction_History_Record.append(transactionInfo) 
        elif 's' == typee:
            transactionInfo  = f"Transaction Type : Saving\tAmount:{Money}\tBalance After Transaction::{self.__balance}"
            self.Transaction_History_Record.append(transactionInfo) 
        else:
            transactionInfo  = f"Transaction Type : Receive Taka\tAmount:{Money}\tBalance After Transaction::{self.__balance}"
            self.Transaction_History_Record.append(transactionInfo) 

          


    #4 qstn requirement - Can check available balance. 
    @property
    def Available_balance(self):
        return self.__balance

    #5qsnt requirement - Can check transaction history. 
    def TransactionHistory(self):
        if not self.Transaction_History_Record:
            print('\t\t\tNo Transaction History recorded ')
            return
        
        for record in self.Transaction_History_Record : 
            print(record)
        print("\n")
        # return self.Transaction_History_Record
 
    #6. Can take a loan from the bank at most two times.
    def Loan(self ,BankName, loanAmount ): #take bank object and loan amount
        if self.TakeLoan <=2 and BankName.LoanActive == True and BankName.AvalableBalance > loanAmount and BankName.MaxLoan >= loanAmount: 
            BankName.TotalLoanAmount =loanAmount #setter mthod use here 
            BankName.AvalableBalance = (loanAmount * -1) 
            # self.__balance+= loanAmount
            self.LoanTaka += loanAmount

            # self.__balance+=1
            self.TakeLoan+=1 


            #Loan list track (extra)
            self.TwoTimeLoan.append(loanAmount)
            
            print(f"{loanAmount} taka Loan successfully done")

            transactionInfo  = f"Transaction Type:TakeLoan\tAmount:{loanAmount}\tLoan Balance After Take Loan:{self.LoanTaka} "
            self.Transaction_History_Record.append(transactionInfo)
        else:
            if BankName.AvalableBalance < loanAmount:
                print(f"\t\t\t\t\nThe bank doesn't have that much money.")
            elif BankName.LoanActive == False:
                print(f"\t\t\t\t\nBank Loan System is now Deactivate....")
            elif BankName.MaxLoan < loanAmount :
                print(f"\t\t\t\t\nYou can maximum loan {BankName.MaxLoan} amount Taka")
            else: 
                print(f"\t\t\t\t\nYou can loan from the bank at most two time . ")

    #7. Can transfer the amount from his account to another user account
    def TransferAmount(self,BankName,ReceiverAccount,TransferAmount):
        if ReceiverAccount in BankName.UserList:
            if TransferAmount > self.__balance:
                print(f"Transfer amount {TransferAmount} is more than Your Bank Amount : {self.__balance}")
                return
            self.__balance-=TransferAmount
            ReceiverUserObject = BankName.UserList[ReceiverAccount]
            d = 'receive'
            ReceiverUserObject.deposite(BankName,TransferAmount,d)

            transactionInfo  = f"Transaction Type :TransferTaka\tAmount:{TransferAmount}\tBalance After Transaction::{self.__balance}"
            self.Transaction_History_Record.append(transactionInfo)
            print(f"This Account : {ReceiverAccount}\n Name : {ReceiverUserObject.name}\nTranfer :{TransferAmount} Taka Successfully . ")


        else:
            print(f"\nAccount does not exist\n")

    # (extra feature add)
    def payLoan(self,BankName , tk):

        if self.LoanTaka == 0:
            print(f"You have chosen the wrong option \nbecause you don’t need to make a loan payment. Your loan balance is zero.")
            return
        
        if tk > self.LoanTaka :
            val = tk - self.LoanTaka
            lloanTk = self.LoanTaka
            beforePayingLoan = self.__balance
            self.__balance+= val
            self.LoanTaka = 0 
            self.TakeLoan= 0 # সে দুইবার লোণ নিয়েছে এবং তা পরিশোধ করে দিয়েছে তাই সে আবার লোণ নিতে পারবে । 
            self.TwoTimeLoan = []
            BankName.AvalableBalance = tk
            BankName.TotalLoanAmount = (val * -1)
            print(f"\t\tYou Pay Your Full Loan Amount Successfully . Your Loan Amount {lloanTk} Taka . But You pay more than {val} Taka \n\t\tSo, the excess amount {val} Taka after paying off the loan has been added back to your main balance.")
            print(f"\t\tBefore Your Bank Balance : {beforePayingLoan}")
            print(f"\t\tNow Your Bank Balancee {self.__balance}")
            print(f"\t\t Now You Can Take Loan Again Two Times")

            transactionInfo  = f"Transaction Type :PayLoan\tAmount:{val}\tBalance After Transaction:{self.__balance} Add Remaining Taka Your Balance"
            self.Transaction_History_Record.append(transactionInfo)
      

            return
        
        if tk == self.LoanTaka : 
            self.LoanTaka = 0 
            self.TakeLoan = 0 
            self.TwoTimeLoan = []
            BankName.AvalableBalance = tk
            BankName.TotalLoanAmount = (tk * -1)
            print(f"\t\tYou Pay Your Full laon Successfully... Now You Can Take Loan Again")
            transactionInfo  = f"Transaction Type :PayLoan\tAmount:{tk}\tRemaining Loan Amount :{self.LoanTaka}"
            self.Transaction_History_Record.append(transactionInfo)
      
            return
        
        if tk > self.TwoTimeLoan[0] :
            fstLoanAmnt = self.TwoTimeLoan[0]
            val = tk - self.TwoTimeLoan[0]
            self.TwoTimeLoan[1] - val
            del self.TwoTimeLoan[0]
            self.TakeLoan -= 1 
            self.LoanTaka -= tk
            BankName.AvalableBalance = tk
            BankName.TotalLoanAmount  = (tk * -1)
            # print(f"\t\tYou Pay Your Loan SuccessFully . \n\t\tYour Repay Loan Amount More Than Your First Loan Amount {fstLoanAmnt}. That's Why deposited the remaining {val} taka towards the second loan.")
            print(f"\t\tYou Pay Your Loan SuccessFully...Now You Can Take Loan Again ")

            transactionInfo  = f"Transaction Type :PayLoan\tAmount:{tk}\tRemaining Loan Amount :{self.LoanTaka}"
            self.Transaction_History_Record.append(transactionInfo)
      
            return
        
        if tk == self.TwoTimeLoan[0] : 
            del self.TwoTimeLoan[0]
            self.TakeLoan -= 1 
            self.LoanTaka -= tk
            BankName.AvalableBalance = tk
            BankName.TotalLoanAmount  = (tk * -1)

            print(f"\t\tYou Pay Your First Loan Successfully...")

            transactionInfo  = f"Transaction Type :PayLoan\tAmount:{tk}\tRemaining Loan Amount :{self.LoanTaka}"
            self.Transaction_History_Record.append(transactionInfo)
      
            return
        
        self.TwoTimeLoan[0] -= tk 
        self.LoanTaka -= tk
        BankName.AvalableBalance = tk
        BankName.TotalLoanAmount = (tk * -1)
        print(f"Pay Loan {tk} Taka Successfully...")
        transactionInfo  = f"Transaction Type :PayLoan\tAmount:{tk}\tRemaining Loan Amount :{self.LoanTaka}"
        self.Transaction_History_Record.append(transactionInfo)
      
        
    def Take_Loan(self):
        if self.TakeLoan == 0 :
            print(f"Take Loan 2 times ")
        elif self.TakeLoan == 1 : 
            print(f"Take Loan 1 Times ")
        else: 
            print(f"You Can't Take Loan")


    def Loan_amount(self):
        if self.LoanTaka == 0 : 
            print(f"Your Loan Amount 0 . so you no need paying any loan ")
            return
        print(f"\t\tRemaining Loan Amount {self.LoanTaka}")



    



   
  

class Admin:

    #1st qstn requirement - Can create an account 
    def Create_An_User_Accounts(self,BankName , Accounts):
        BankName.Creat_An_User_Acount(Accounts)


    #2nd qstn requirement - Can delete any user account
    def Delete_User_Account(self, BankName,AccountNumber): #take Bank object and Acount Number
        BankName.DeleteUserAccount(AccountNumber)

    #3rd qstn requirement Can see all user accounts list
    def View_All_User_Account(self,BankName): #take bankObject  
        BankName.ViewAllUserAcount()

    #4th Qstn requirement Can check the total available balance of the bank
    def Available_balance(self,BankName):
        bankAvailableBalance  = BankName.AvalableBalance #getter method access
        print(f"Bank Total Balance : {bankAvailableBalance}")

    #5th qstn requirement - Can check the total loan amount
    def Loan_Amount(self, bankName):
        bankaTotalLoanAmount = bankName.TotalLoanAmount #getter method access
        print(f"Bank Total Loan Amount : {bankaTotalLoanAmount}")
    #6th qstn requirement - Can on or off the loan feature of the bank. 
    def LoanOnOfFeature(self, bankName,OnOf): #take bankObje and loan activate value
        bankName.LoanActive = OnOf #set value 
        if bankName.LoanActive == False :
            print(f"\t\t\tLoan Off Feature Activate successfully\n")
        else:
            print(f"\t\t\tLoan On Feature Activate SuccessFully\n")

        

    def bankRuptt(self,bankName):
        bankName.bankRupt = True
        if bankName.bankRupt == True :
            print(f"You set Bank rupt successfully \n")
        else:
            print('You set Bank Don\'t Rupt successfully  ')




class Bank:
    def __init__(self,name,Balance) -> None:
        self.name = name
       
    # I used a dictionary here to reduce complexity. I will store user information like this: the key will hold the user's accountNumber, and the value will store the user's object. When I need to delete a user account, I'll search using the accountNumber key, which will have a complexity of O(1).
        self.__totalBalance  = Balance
        self.__isLoanActive = True 
        self.__TotalLoanAmount = 0 
        self.UserList = {}  
        self.AdminList = []
        self.__bankRupt = False
        self.MaxLoan = 300000

    @property
    def bankRupt(self):
        return self.__bankRupt
    
    @bankRupt.setter
    def bankRupt(self,rupt):
        self.__bankRupt = rupt
        
    def Creat_An_User_Acount(self, User): #take user object 
        UserAccountNumber = User.AcountNumber #take Account Number from the User object 
        self.UserList[UserAccountNumber] = User #save UserList key as AccountNumber and save value as account object

    def ViewAllUserAcount(self):
        print(f"View All Users Details")
        table_data = []
        for value in self.UserList.values():

            # print('Account Number : ', value.AcountNumber)
            # print('Name : ', value.name)
            # print('Email : ',value.email)
            # print('Address : ',value.address)
            # print('Phone Number : ',value.phone)

            # print('\n\n')
            

            # now show table wise 
            user_details = [
                
                value.AcountNumber,
                value.name,
                value.email,
                value.address,
                value.phone,
                value.AccountType

            ]
            table_data.append(user_details)

            # print('\n\n')

        print(tabulate(table_data , headers=["Account Number" , "Name" , "Email" , "Address" , "Phone Number,Account Type"],tablefmt="grid"))
    def Create_An_Admin_Account(self,Adminn):
        self.AdminList.append(self,Adminn)
        # self.AdminList[]

    def DeleteUserAccount(self,AccountNumber):
        if AccountNumber in self.UserList:
            userr = self.UserList[AccountNumber] 
            Name = userr.name 
            del self.UserList[AccountNumber]

            print(f"\t\t\t\t\nDeleted Successfully this User Acount - Name:{Name}\tAccountNumber : {AccountNumber}")
        else:
            print(f"\t\t\t\t\nThis Account Number : {AccountNumber} Not Exist.... Enter Valid Acount Number")


    @property
    def AvalableBalance(self):
        return self.__totalBalance
    
    @AvalableBalance.setter
    def AvalableBalance(self,money):
        self.__totalBalance+=money

    


    @property
    def TotalLoanAmount(self):
        return self.__TotalLoanAmount
    
    @TotalLoanAmount.setter
    def TotalLoanAmount(self,newLoan):
        self.__TotalLoanAmount+=newLoan

    @property
    def LoanActive(self):
        return self.__isLoanActive 
    @LoanActive.setter
    def LoanActive(self , OnOf):
        self.__isLoanActive = OnOf



Laxmi_chit_fund = Bank('Laxmi Chit Fund',2500000)


def UserMethod():
    acountNumber = input("\tEnter Your User Account Number: ")
    if acountNumber in Laxmi_chit_fund.UserList:
        UserAcountObject = Laxmi_chit_fund.UserList[acountNumber]
        Name = UserAcountObject.name
        print(f"\t\t\t\t\nWelcome, {Name}, To Our {Laxmi_chit_fund.name} Bank")
        while True:
            print('\n\n\n')
            print(f"\t\t1.Withdraw Amount ")
            print(f"\t\t2.Deposite Amount ")
            print(f"\t\t3.Check Available Balance ")
            print(f"\t\t4.Check Transaction Histroy ")
            print(f"\t\t5.Take A Loan ")
            print(f"\t\t6.Transfer the amount from Your account to another user account")
            print(f"\t\t7.How many more times can I take a loan?") 
            print(f"\t\t8.Repay Loan")
            print(f"\t\t9.How much loan amount is left to be repaid")
            print(f"\t\t10.Exit ")
        

            chose = int(input("\t\tChose Your Option "))
            print('\n\n\n')

            if chose == 1 : 
                amount = int(input(f"\t\tEnter Your Withdrawal Amount: "))
                UserAcountObject.withdrawal(Laxmi_chit_fund, amount)
            elif chose == 2:
                AvailableBalanceBeforeDeposite  = UserAcountObject.Available_balance

                amount =  int(input(f"\t\tEnter Yout Depoite Amount: "))
                c = 'c'
                UserAcountObject.deposite(Laxmi_chit_fund, amount, c)
                AvailableBalanceAfterDeposite = UserAcountObject.Available_balance
                if (AvailableBalanceBeforeDeposite + amount) == AvailableBalanceAfterDeposite :
                    print(f"\t\t Heyy {Name}")
                    print(f"\t\t Your Before Deposite Amount {amount} Your Bank Balance : {AvailableBalanceBeforeDeposite}")
                    print(f"\t\t You Deposite Your amount : {amount} Taka Successfully... ")
                    print(f"\t\t Your After Deposite Amount {amount} Taka, Your Bank Balance: {UserAcountObject.Available_balance}")
                
            elif chose == 3:
                AvailableBalance = UserAcountObject.Available_balance
                print(f'{Name} Your Available Balance : {AvailableBalance}')
            elif chose == 4:
                UserAcountObject.TransactionHistory()
            elif chose == 5:
                amount = int(input("\t\tHow much money do you want to borrow? "))
                UserAcountObject.Loan(Laxmi_chit_fund,amount)
            elif chose == 6:
                acountNumber = input("\t\tPlease provide the account number of the account you want to send the money to.")
                TransferAmount = int(input("\t\tEnter Transfer Amount: "))
                UserAcountObject.TransferAmount(Laxmi_chit_fund,acountNumber,TransferAmount)
            elif chose == 7:
                # Take_Loan
                UserAcountObject.Take_Loan()
                
            elif chose == 8 :
                amount = int(input(f"\t\tHow much money would you like to pay towards the loan"))
                UserAcountObject.payLoan(Laxmi_chit_fund,amount)
            elif chose == 9: 
                UserAcountObject.Loan_amount()
            elif chose == 10 : 
                break
            else:
                print(f"\t\tEnter InValid Option")

    else: 
        print(f"\t\t\t\t\ncouldn't find any bank account.")
    # print(f"\t\t1.withdrawal Amount")

def AdminMethod():
    admin_instance = Admin()

    while True:
        
        print('\n')
        print(f"\t\t1.Create An User Account ")
        print(f"\t\t2.Can Delete Any User Account ")
        print(f"\t\t3.Can See ALL User Accounts List ")
        print(f"\t\t4.Can check the total available balance of the bank. ")
        print(f"\t\t5.Can check the total loan amount. ")
        print(f"\t\t6.Can on or off the loan feature of the bank.  ")
        print(f"\t\t7.Set BankRupt")
        print(f"\t\t8.Exit ")
        print('\n')
    
        option = int(input("\t\tChose Your Option : "))
        print('\n')
        if option == 1 : 

            name = input("Enter User Name : ")
            email = input("Etner User Email : ")
            address = input("Enter User Address : ")
            Phone = input("Enter User Mobile Number : ")
            # AccountType = input("Enter User AccountType : ")
            print(f"choose Current Account Type : ")
            while True:
                print(f"\t1.Current Account")
                print(f"\t2.Savings")
                accountType = int(input(f"\tChoose option: "))
                if accountType == 1 :
                    userAcountObject = User(name ,email , address ,Phone, 'Current')
                    break
                elif accountType == 2 : 
                    amountt = int(input(f"How much amount would you like to save - "))
                    userAcountObject = User(name ,email , address ,Phone, 'Saving')
                    userAcountObject.deposite(Laxmi_chit_fund, amountt , 's')
                    break
                else : 
                    print(f"\tchoose correct option")
                    

            print(f"\n\n")
            admin_instance.Create_An_User_Accounts(Laxmi_chit_fund,userAcountObject)
        elif option == 2 : 
            AccountNumber = input("Enter User Account Number: ")
            admin_instance.Delete_User_Account(Laxmi_chit_fund,AccountNumber=AccountNumber)
        elif option == 3:
            admin_instance.View_All_User_Account(Laxmi_chit_fund)
        elif option == 4:
            admin_instance.Available_balance(Laxmi_chit_fund)
        elif option ==5:
            admin_instance.Loan_Amount(Laxmi_chit_fund)
        elif option == 6:
            while True:
                print("\n")
                print("\n")
                print(f"\t\t\t\t1.Do You Want To Loan Feature Is On ")
                print(f"\t\t\t\t2.Do You Want To Loan Feature Is OFF ")
                print(f"\t\t\t\t3.Nothing ")
                chose = int(input("\t\t\t\t\n\nChose Your Option : "))
                print("\n")
                print("\n")

                if chose == 1:
                    admin_instance.LoanOnOfFeature(Laxmi_chit_fund,True)
                    break
                elif chose == 2:
                    admin_instance.LoanOnOfFeature(Laxmi_chit_fund,False)
                    break
                elif chose == 3:
                    break
                else :
                    print(f"\t\t\t\tEnter Valid Option ")
        elif option == 7: 
            while True:
                print("\n")
                print(f"\t\t\t\tAre You Want To Bank Rupt Otion Is True ? Chose Your Option --> ")
                print(f"\t\t\t\t1. Yes")
                print(f"\t\t\t\t2. No")
                print("\n")
                
                chose = int(input("Chose Your Option: "))
                if chose == 1 : 
                    admin_instance.bankRuptt(Laxmi_chit_fund)
                    break
                elif chose == 2:
                    break
                else:
                    print("\n")
                    print(f"\t\t\t\tChose Correct Option !!! ")
        elif option == 8:
            break
        else :
            print(f"\t\tEnter Valid Option")

        


while(True):
    print(f"\t\t\t\t\t\t\tWelcome To Our {Laxmi_chit_fund.name} Bank\n\n")
    print(f"\t\t1.Admin ")
    print(f"\t\t2.User ")
    print(f"\t\t3.Exit ")
    option = int(input("\t\tChose Your Option:  "))
    if option == 1:
        print("\n\n")
        AdminMethod()
    elif option ==2:
        print("\n\n")
        UserMethod()
    elif option == 3 : 
        break
    
