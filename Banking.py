import random
pp=0
print("------------------------------------")
print("------------------------------------")
print("************ Sai's BANK ************")
print("------------------------------------")
po=1
def Branch(bran):
    nu="01234567899876543210"
    string=nu
    le="ABCDEFGHIJKLMNOPQURSTUVWXYZ"
    string1=nu+le
    length1=9
    string2=le
    length2=12
    rr="".join(random.sample(string2,length2))
    id="".join(random.sample(string1,length1)) 
    ifsc="".join(random.sample(string,length2))
    branh=bran
    Accounts.append(branh)
    an=input("  Enter Your Name: ")
    Accounts.append(an)
    ad=input("  Enter Your Address: ")
    Accounts.append(ad)
    mn=int(input("  Enter Your Mobile Number: "))
    Accounts.append(mn)
    print("  Account Number is: ",ifsc)
    Accounts.append(ifsc)
    print("  Account Id is: ",id)
    Accounts.append(id)
    print("  Account IFSC code is :",rr)
    Accounts.append(rr)
    while(1):
        d=input("Do you want to deposit money(Yes/No): ")
        if (d == 'y' or d == 'Y' or d == 'yes' or d == 'YES'):
            a=int(input("Enter the amount to Deposit: "))
            print(f" your amount {a} is Successfully deposited")
            Accounts.append(a)
            break
        
        elif(d == 'n' or d == 'N' or d == 'no' or d == 'NO'):
            a1=0
            Accounts.append(a1)
            print("     Thank You...")
            print("Your account has been Created...")
            break
        
        else:
            print("Please enter yes or no or y or n")
    
    print("------------------------------------")
    
Accounts=[0]
AccDemo=[]
def Creat_account():
        print("------------------------------------")
        print("     1.State Bank Of India")
        print("     2.Canara Bank")
        print("     3.Karnataka Bank")
        print("     4.HDFC Bank")
        print("     5.Bank Of Baroda Bank")
        print("     6.ICICI Bank")
        print("------------------------------------")
        i=int(input("Enter The Branch:")) 
        if(i==1):
           #Accounts.insert(po,aclist[0])
            print("------------------------------------")
            print("   Welcome To State Bank Of India   ")
            print("------------------------------------")
            bran="          STATE BANK OF INDIA"
            Branch(bran)
        elif(i==2):
           # Accounts.insert(po,aclist[1])
            print("------------------------------------")
            print("       Welcome To Canara Bank       ")
            print("------------------------------------")
            bran="          CANARA BANK"
            Branch(bran)
        elif(i==3):
           # Accounts.insert(po,aclist[2])
            print("------------------------------------")
            print("     Welcome To Karnataka Bank      ")
            print("------------------------------------")
            bran="          KARNATAKA BANK"
            Branch(bran)
        elif(i==4):
            #Accounts.insert(po,aclist[3])
            print("------------------------------------")
            print("       Welcome to HDFC Bank         ")
            print("------------------------------------")
            bran="          HDFC BANK"
            Branch(bran)
        elif(i==5):
           # Accounts.insert(po,aclist[4])
            print("------------------------------------")
            print("   Welcome To Bank Of Baroda Bank   ")
            print("------------------------------------")
            bran="          BANK OF BARODA BANK"
            Branch(bran)
        elif(i==6):
            #Accounts.insert(po,aclist[5])
            print("------------------------------------")
            print("       Welcome To ICICI Bank        ")
            print("------------------------------------")
            bran="          ICICI BANK"
            Branch(bran)
        else:
            print("Invalid Choice Please Try Again!")
            
#print(Accounts)
def pin():
    print("1.PIN Generation ")
    print("2.PIN reset")
    e=int(input("Enter your choice:"))
    if(e==1):
        pp=1
        nu="01234567899876543210"
        string=nu
        length=4
        po = "".join(random.sample(string,length))
        print("Your PIN is:",po)
        Accounts.append(po)
        
    else:
        print("PIN reset is not possible because your new to Account(To reset pin wait one day)")

def Account():
        print(Accounts[1])
        print("Account name:",Accounts[2])
        print("Account Addres:",Accounts[3])
        print("Account Mobile Number:",Accounts[4])
        print("Account Account Number:",Accounts[5])
        print("Account Id:",Accounts[6])
        print("Account IFSC:",Accounts[7])
        print("Account Balance:",Accounts[8])
        print("You'r Secret PIN is:",Accounts[9])
def deposit():
        a=input("Enter the PIN:")
        if a==Accounts[9]:
            d=int(input("Enter the Amount to Deposit:"))
            Accounts[8]+=d
            print("You have been creadited:",d)
            print("Total Amount :",Accounts[8])
        else:
            print("Wrong Pin Entered")

def transfer():
    t=int(input("Enter The amount you want to Transfer: "))
    if (t<=Accounts[8]):
        po1=(input("Enter You'r Secret PIN:"))
        if (po1 == Accounts[9]):
            Accounts[8]-=t
            print("Transfer Successful!!")
        else:
            print("You have entered wrong pin")
    else:
        print("Insufficient balance in account")
        print("Current Balance: ",Accounts[8])
def balance_enquery():
        b=(input("Enter Your Secret Pin:"))
        if (b==Accounts[9]):
            print("Balance Enquiry Successfull!!")
            print("Current Balance: ",Accounts[8])
        else:
            print("You have entered wrong pin")
def withdraw():
    
    w=int(input("Enter the amount you want to Withdraw:"))
    if (w <= Accounts[8]):
        po1=(input("Enter You'r Secret PIN:"))
        if (po1 == Accounts[9]):
            Accounts[8] -= w
            print("Withdraw Successful!!")
        else:
            print("You have entered wrong pin")
    else:
        print("Insufficient balance in account")
        print("Current Balance: ",Accounts[8])
ch1 = 0
while(1):
    print("------------------------------------")
    print("         1.Create Account")  
    print("         2.Account")
    print("         3.Transfer")
    print("         4.Balance Enquery")
    print("         5.Withdraw")
    print("         6.Deposit")
    print("         7.Pin")
    print("         8.EXIT")
    print("------------------------------------")
    z=(input("      Enter your Choice:"))
    print("------------------------------------")
    
    if(z=="1"):
        ch1 += 1
        Creat_account()
        
    elif(z=='2'):
        if(ch1 == 0):
            print("CREATE ACCOUNT FIRST...")
        elif(pp==0):
            print("PLEASE GENERATE PIN FIRST...")
        else:
            Account()
    elif(z=='3'):
        if(ch1 == 0):
            print("CREATE ACCOUNT FIRST...")
        elif(pp==0):
            print("PLEASE GENERATE PIN FIRST...")
        else:
            transfer()
    elif(z=='4'):
        if(ch1 == 0):
            print("CREATE ACCOUNT FIRST...")
        elif(pp==0):
            print("PLEASE GENERATE PIN FIRST...")
        else:
            balance_enquery()
    elif(z=='5'):
        if(ch1 == 0):
            print("CREATE ACCOUNT FIRST...")
        elif(pp==0):
            print("PLEASE GENERATE PIN FIRST...")
        else:
            withdraw()
    elif(z=='6'):
        if(ch1 == 0):
            print("CREATE ACCOUNT FIRST...")
        elif(pp==0):
            print("PLEASE GENERATE PIN FIRST...")
        else:
            deposit()
    elif(z=='7'):
        pin()
        pp=1
    elif(z=='8'):
        print("Thank You....Visit Again....")
        break
    else:
        print("Please choose appropriate choice....!")

