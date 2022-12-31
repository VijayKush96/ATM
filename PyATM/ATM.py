#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Users={4000300020001001:{'account no.':12345678900001, 'mobile no.': 9876543001, 'ATM PIN':1234, 'balance':1000},
       4000300020001002:{'account no.':12345678900002, 'mobile no.': 9876543002, 'ATM PIN':2345, 'balance':2000},
       4000300020001003:{'account no.':12345678900003, 'mobile no.': 9876543003, 'ATM PIN':3456, 'balance':3000},
       4000300020001004:{'account no.':12345678900004, 'mobile no.': 9876543004, 'ATM PIN':4567, 'balance':4000},
       4000300020001005:{'account no.':12345678900005, 'mobile no.': 9876543005, 'ATM PIN':5647, 'balance':5000},
       4000300020001006:{'account no.':12345678900006, 'mobile no.': 9876543006, 'ATM PIN':6789, 'balance':6000},
       4000300020001007:{'account no.':12345678900007, 'mobile no.': 9876543007, 'ATM PIN':7890, 'balance':7000},
       4000300020001008:{'account no.':12345678900008, 'mobile no.': 9876543008, 'ATM PIN':8901, 'balance':8000},
       4000300020001009:{'account no.':12345678900009, 'mobile no.': 9876543009, 'ATM PIN':9012, 'balance':9000},
       4000300020001010:{'account no.':12345678900010, 'mobile no.': 9876543010, 'ATM PIN':1011, 'balance':10000},
       4000300020001011:{'account no.':12345678900011, 'mobile no.': 9876543011, 'ATM PIN':1112, 'balance':11000},
       4000300020001012:{'account no.':12345678900012, 'mobile no.': 9876543012, 'ATM PIN':1213, 'balance':12000},
       4000300020001013:{'account no.':12345678900013, 'mobile no.': 9876543013, 'ATM PIN':1314, 'balance':13000},
       4000300020001014:{'account no.':12345678900014, 'mobile no.': 9876543014, 'ATM PIN':1415, 'balance':14000},
       4000300020001015:{'account no.':12345678900015, 'mobile no.': 9876543015, 'ATM PIN':1516, 'balance':15000},
       4000300020001016:{'account no.':12345678900016, 'mobile no.': 9876543016, 'ATM PIN':1617, 'balance':16000},
       4000300020001017:{'account no.':12345678900017, 'mobile no.': 9876543017, 'ATM PIN':1718, 'balance':17000},
       4000300020001018:{'account no.':12345678900018, 'mobile no.': 9876543018, 'ATM PIN':1819, 'balance':18000},
       4000300020001019:{'account no.':12345678900019, 'mobile no.': 9876543019, 'ATM PIN':1920, 'balance':19000},
       4000300020001020:{'account no.':12345678900020, 'mobile no.': 9876543020, 'ATM PIN':2021, 'balance':20000},
       4000300020001021:{'account no.':12345678900021, 'mobile no.': 9876543021, 'ATM PIN':2122, 'balance':21000},
       4000300020001022:{'account no.':12345678900022, 'mobile no.': 9876543022, 'ATM PIN':2223, 'balance':22000},
       4000300020001023:{'account no.':12345678900023, 'mobile no.': 9876543023, 'ATM PIN':2324, 'balance':23000},
       4000300020001024:{'account no.':12345678900024, 'mobile no.': 9876543024, 'ATM PIN':2425, 'balance':24000},
       4000300020001025:{'account no.':12345678900025, 'mobile no.': 9876543025, 'ATM PIN':2526, 'balance':25000},
       4000300020001026:{'account no.':12345678900026, 'mobile no.': 9876543026, 'ATM PIN':2627, 'balance':26000},
       4000300020001027:{'account no.':12345678900027, 'mobile no.': 9876543027, 'ATM PIN':2728, 'balance':27000},
       4000300020001028:{'account no.':12345678900028, 'mobile no.': 9876543028, 'ATM PIN':2829, 'balance':28000},
       4000300020001029:{'account no.':12345678900029, 'mobile no.': 9876543029, 'ATM PIN':2930, 'balance':29000},
       4000300020001030:{'account no.':12345678900030, 'mobile no.': 9876543030, 'ATM PIN':3031, 'balance':30000},
       4000300020001031:{'account no.':12345678900031, 'mobile no.': 9876543031, 'ATM PIN':3132, 'balance':31000},
       4000300020001032:{'account no.':12345678900032, 'mobile no.': 9876543032, 'ATM PIN':3233, 'balance':32000},
       4000300020001033:{'account no.':12345678900033, 'mobile no.': 9876543033, 'ATM PIN':3334, 'balance':33000},
       4000300020001034:{'account no.':12345678900034, 'mobile no.': 9876543034, 'ATM PIN':3435, 'balance':34000},
       4000300020001035:{'account no.':12345678900035, 'mobile no.': 9876543035, 'ATM PIN':3536, 'balance':35000},
       4000300020001036:{'account no.':12345678900036, 'mobile no.': 9876543036, 'ATM PIN':3637, 'balance':36000},
       4000300020001037:{'account no.':12345678900037, 'mobile no.': 9876543037, 'ATM PIN':3738, 'balance':37000},
       4000300020001038:{'account no.':12345678900038, 'mobile no.': 9876543038, 'ATM PIN':3839, 'balance':38000},
       4000300020001039:{'account no.':12345678900039, 'mobile no.': 9876543039, 'ATM PIN':3940, 'balance':39000},
       4000300020001040:{'account no.':12345678900040, 'mobile no.': 9876543040, 'ATM PIN':4041, 'balance':40000},
       4000300020001041:{'account no.':12345678900041, 'mobile no.': 9876543041, 'ATM PIN':4142, 'balance':41000},
       4000300020001042:{'account no.':12345678900042, 'mobile no.': 9876543042, 'ATM PIN':4243, 'balance':42000},
       4000300020001043:{'account no.':12345678900043, 'mobile no.': 9876543043, 'ATM PIN':4344, 'balance':43000},
       4000300020001044:{'account no.':12345678900044, 'mobile no.': 9876543044, 'ATM PIN':4445, 'balance':44000},
       4000300020001045:{'account no.':12345678900045, 'mobile no.': 9876543045, 'ATM PIN':4546, 'balance':45000},
       4000300020001046:{'account no.':12345678900046, 'mobile no.': 9876543046, 'ATM PIN':4647, 'balance':46000},
       4000300020001047:{'account no.':12345678900047, 'mobile no.': 9876543047, 'ATM PIN':4748, 'balance':47000},
       4000300020001048:{'account no.':12345678900048, 'mobile no.': 9876543048, 'ATM PIN':4849, 'balance':48000},
       4000300020001049:{'account no.':12345678900049, 'mobile no.': 9876543049, 'ATM PIN':4950, 'balance':49000},
       4000300020001050:{'account no.':12345678900050, 'mobile no.': 9876543050, 'ATM PIN':5051, 'balance':50000},
       4000300020001051:{'account no.':12345678900051, 'mobile no.': 9876543051, 'ATM PIN':5152, 'balance':51000},
       4000300020001052:{'account no.':12345678900052, 'mobile no.': 9876543052, 'ATM PIN':5253, 'balance':52000},
       4000300020001053:{'account no.':12345678900053, 'mobile no.': 9876543053, 'ATM PIN':5354, 'balance':53000},
       4000300020001054:{'account no.':12345678900054, 'mobile no.': 9876543054, 'ATM PIN':5455, 'balance':54000},
       4000300020001055:{'account no.':12345678900055, 'mobile no.': 9876543055, 'ATM PIN':5556, 'balance':55000},
       4000300020001056:{'account no.':12345678900056, 'mobile no.': 9876543056, 'ATM PIN':5657, 'balance':56000},
       4000300020001057:{'account no.':12345678900057, 'mobile no.': 9876543057, 'ATM PIN':5758, 'balance':57000},
       4000300020001058:{'account no.':12345678900058, 'mobile no.': 9876543058, 'ATM PIN':5859, 'balance':58000},
       4000300020001059:{'account no.':12345678900059, 'mobile no.': 9876543059, 'ATM PIN':5960, 'balance':59000},
       4000300020001060:{'account no.':12345678900060, 'mobile no.': 9876543060, 'ATM PIN':6061, 'balance':60000},
       4000300020001061:{'account no.':12345678900061, 'mobile no.': 9876543061, 'ATM PIN':6162, 'balance':61000},
       4000300020001062:{'account no.':12345678900062, 'mobile no.': 9876543062, 'ATM PIN':6263, 'balance':62000},
       4000300020001063:{'account no.':12345678900063, 'mobile no.': 9876543063, 'ATM PIN':6364, 'balance':63000},
       4000300020001064:{'account no.':12345678900064, 'mobile no.': 9876543064, 'ATM PIN':6465, 'balance':64000},
       4000300020001065:{'account no.':12345678900065, 'mobile no.': 9876543065, 'ATM PIN':6566, 'balance':65000},
       4000300020001066:{'account no.':12345678900066, 'mobile no.': 9876543066, 'ATM PIN':6667, 'balance':66000},
       4000300020001067:{'account no.':12345678900067, 'mobile no.': 9876543067, 'ATM PIN':6768, 'balance':67000},
       4000300020001068:{'account no.':12345678900068, 'mobile no.': 9876543068, 'ATM PIN':6869, 'balance':68000},
       4000300020001069:{'account no.':12345678900069, 'mobile no.': 9876543069, 'ATM PIN':6970, 'balance':69000},
       4000300020001070:{'account no.':12345678900070, 'mobile no.': 9876543070, 'ATM PIN':7071, 'balance':70000},
       4000300020001071:{'account no.':12345678900071, 'mobile no.': 9876543071, 'ATM PIN':7172, 'balance':71000},
       4000300020001072:{'account no.':12345678900072, 'mobile no.': 9876543072, 'ATM PIN':7273, 'balance':72000},
       4000300020001073:{'account no.':12345678900073, 'mobile no.': 9876543073, 'ATM PIN':7374, 'balance':73000},
       4000300020001074:{'account no.':12345678900074, 'mobile no.': 9876543074, 'ATM PIN':7475, 'balance':74000},
       4000300020001075:{'account no.':12345678900075, 'mobile no.': 9876543075, 'ATM PIN':7576, 'balance':75000},
       4000300020001076:{'account no.':12345678900076, 'mobile no.': 9876543076, 'ATM PIN':7677, 'balance':76000},
       4000300020001077:{'account no.':12345678900077, 'mobile no.': 9876543077, 'ATM PIN':7778, 'balance':77000},
       4000300020001078:{'account no.':12345678900078, 'mobile no.': 9876543078, 'ATM PIN':7879, 'balance':78000},
       4000300020001079:{'account no.':12345678900079, 'mobile no.': 9876543079, 'ATM PIN':7980, 'balance':79000},
       4000300020001080:{'account no.':12345678900080, 'mobile no.': 9876543080, 'ATM PIN':8081, 'balance':80000},
       4000300020001081:{'account no.':12345678900081, 'mobile no.': 9876543081, 'ATM PIN':8182, 'balance':81000},
       4000300020001082:{'account no.':12345678900082, 'mobile no.': 9876543082, 'ATM PIN':8283, 'balance':82000},
       4000300020001083:{'account no.':12345678900083, 'mobile no.': 9876543083, 'ATM PIN':8384, 'balance':83000},
       4000300020001084:{'account no.':12345678900084, 'mobile no.': 9876543084, 'ATM PIN':8485, 'balance':84000},
       4000300020001085:{'account no.':12345678900085, 'mobile no.': 9876543085, 'ATM PIN':8586, 'balance':85000},
       4000300020001086:{'account no.':12345678900086, 'mobile no.': 9876543086, 'ATM PIN':8687, 'balance':86000},
       4000300020001087:{'account no.':12345678900087, 'mobile no.': 9876543087, 'ATM PIN':8788, 'balance':87000},
       4000300020001088:{'account no.':12345678900088, 'mobile no.': 9876543088, 'ATM PIN':8889, 'balance':88000},
       4000300020001089:{'account no.':12345678900089, 'mobile no.': 9876543089, 'ATM PIN':8990, 'balance':89000},
       4000300020001090:{'account no.':12345678900090, 'mobile no.': 9876543090, 'ATM PIN':9091, 'balance':90000},
       4000300020001091:{'account no.':12345678900091, 'mobile no.': 9876543091, 'ATM PIN':9192, 'balance':91000},
       4000300020001092:{'account no.':12345678900092, 'mobile no.': 9876543092, 'ATM PIN':9293, 'balance':92000},
       4000300020001093:{'account no.':12345678900093, 'mobile no.': 9876543093, 'ATM PIN':9394, 'balance':93000},
       4000300020001094:{'account no.':12345678900094, 'mobile no.': 9876543094, 'ATM PIN':9495, 'balance':94000},
       4000300020001095:{'account no.':12345678900095, 'mobile no.': 9876543095, 'ATM PIN':9596, 'balance':95000},
       4000300020001096:{'account no.':12345678900096, 'mobile no.': 9876543096, 'ATM PIN':9697, 'balance':96000},
       4000300020001097:{'account no.':12345678900097, 'mobile no.': 9876543097, 'ATM PIN':9798, 'balance':97000},
       4000300020001098:{'account no.':12345678900098, 'mobile no.': 9876543098, 'ATM PIN':9899, 'balance':98000},
       4000300020001099:{'account no.':12345678900099, 'mobile no.': 9876543099, 'ATM PIN':9910, 'balance':99000},
       4000300020001100:{'account no.':12345678900100, 'mobile no.': 9876543100, 'ATM PIN':1001, 'balance':100000}}


# In[ ]:


def end_lines():
    print(".........Please Try again.........")
    print("***THANK YOU for bankng with us***")
    print("-------Please Take Your Card------")
def end_lines1():
    print("---------Remove your card---------")
    print("***THANK YOU for bankng with us***")
    
print("Welcome to SBI bank ATM service")
print()

print("Insert your card")
print()
card_no=int(input("Enter 16 digit Card No. : "))
if card_no in Users:
    print()
    print("User Found")
    print()

    print("Select language")
    print("1 >> English")
    print("2 >> Hindi")
    print("3 >> Marathi")
    language=int(input('Please select language options : '))
    if language==1:
        print()
        print("English")
        print()
    
        print("Account Type")
        print("1 >> Current Account")
        print("2 >> Saving Account")
        account_type=int(input("Select Account Type : "))
        if account_type == 1:
            print()
            print("Current Account")
            print()
        
            pin_code=int(input("Enter 4 digit PIN : "))
            if pin_code == Users[card_no]['ATM PIN']:
                print()
                print("PIN is Correct")
                print()
    
                print("Transaction Type")
                print("1 >> Cash Withrawal")
                print("2 >> Balance Enquiry")
                print("3 >> Cash Deposit")
                print("4 >> Change Pin") 
                transaction_type=int(input("Select Your Transaction Option : "))
                if transaction_type == 1:
                    print()
                    print("Cash Withrawal")
                    print()
                    
                    print("*NOTE : Only multiple of 100 will be dispense ")
                    print("*NOTE : Entered Amount should be less than or equal to 10000 ")
                    print("*NOTE : Entered Amount should be less than or equal to Balance Amount")
                    print()
                    print("Account Balance is : ₹",Users[card_no]['balance'])
                    print()
                    w_amount=int(input("Enter Amount : ₹ "))
                    if w_amount%100 == 0:
                        if w_amount <= 10000:
                            if Users[card_no]['balance']-w_amount >= 0:
                                Users[card_no]['balance']=Users[card_no]['balance']-w_amount
                                print()
                                print("Please wait while your transaction is being processed...")
                                print()
                                print("$$$ Please Take Your Case $$$$")
                                print()
                                print("Remaining Balance is : ₹",Users[card_no]['balance'])
                                print()
                                end_lines1()
                            else:
                                print("ERROR : Entered Amount is more than Balance Amount")
                                end_lines()
                        else:
                            print("ERROR : Out of one time transaction limit")
                            end_lines()
                    else:
                        print("ERROR : Entered Amount is not Withdrawable")
                        end_lines()
        
                elif transaction_type == 2:
                    print()
                    print("Balance Enquiry")
                    print()
                    print("Options")
                    print("1 >> Yes")
                    print("2 >> No")
                    option1=int(input("Do you want Reciept? "))
                    print()
                    if option1 == 1:
                        print("Printing Reciept.....")
                        print()
                        print("Please Take Your Reciept")
                        print()
                        end_lines1()
                        
                    elif option1 == 2:
                        print(" Your Account Balance is : ₹",Users[card_no]['balance'])
                        print()
                        end_lines1()
                        
                    else:
                        print("ERROR : Inavalid Option Choosen")
                        end_lines()
        
                elif transaction_type == 3:
                    print()
                    print("Cash Deposit")
                    print()
                    print("*NOTE : Only combinations 100, 500, 2000 notes will be deposited ")
                    print("*NOTE : Entered Amount should be less than or equal to 10000 ")
                    print()
                    d_amount=int(input("Enter Amount : ₹ "))
                    if d_amount%100 == 0:
                        if d_amount <= 10000:
                            Users[card_no]['balance']=Users[card_no]['balance']+d_amount
                            print()
                            print("Please wait while your transaction is being processed...")
                            print("Your Money Successfully Deposited to your Account")
                            print()
                            print("New Account Balance is : ₹",Users[card_no]['balance'])
                            print()
                            end_lines1()
                        else:
                            print("ERROR : Out of one time transaction limit")
                            end_lines()
                    else:
                        print("ERROR : Entered amount is not depositable")
                        end_lines()
    
                elif transaction_type == 4:
                    print()
                    print("Change Pin")
                    print()
                    print("Options")
                    print("1 >> via OTP")
                    print("2 >> via Entering and Matching Account Number and Linked Mobile Number")
                    print()
                    options2=int(input("Choose Option : "))
                    if options2 == 1:
                        print()
                        print("< Sorry this service is not available at this movement >")
                        end_lines()
                    elif options2 == 2:
                        print()
                        print("*NOTE : Your Mobile number must be linked with your Account number")
                        account_no=int(input("Enter Your 14 Digit Account Number : "))
                        if account_no == Users[card_no]['account no.']:
                            mobile_no=int(input("Enter Your 10 Digit Mobile Number : "))
                            if mobile_no == Users[card_no]['mobile no.']:
                                print()
                                print("Entered Account no. and Mobile no. are Matched and Verified")
                                print()
                                print("Set New PIN")
                                print()
                                print("*NOTE : ATM PIN should be 4 digits")
                                print()
                                New_PIN=int(input("Enter New PIN : "))
                                New_PIN=str(New_PIN)
                                if len(New_PIN) == 4:
                                    New_PIN=int(New_PIN)
                                    print()
                                    print("Confirm new PIN")
                                    Confirm_New_PIN=int(input("Confirm New PIN : "))
                                    Confirm_New_PIN=str(Confirm_New_PIN)
                                    if len(Confirm_New_PIN) == 4:
                                        Confirm_New_PIN=int(Confirm_New_PIN)
                                        if Confirm_New_PIN == New_PIN:
                                            Users[card_no]['ATM PIN']=Confirm_New_PIN
                                            print()
                                            print("PIN has been Changed")
                                            print()
                                            end_lines1()
                                        else:
                                            print("ERROR : New PIN and Confirm New PIN are not matched")
                                            end_lines()
                                    else:
                                        print("ERROR : Confirm New Pin is INCORRECT")
                                        end_lines()
                                else:
                                    print("ERROR : New Pin is INCORRECT")
                                    end_lines()
                            else:
                                print("ERROR : Entered Mobile Number is INCORRECT")
                                end_lines()
                        else:
                            print("ERROR : Entered Account Number is INCORRECT")
                            end_lines()
                    else:
                        print("ERROR : Inavalid Option Choosen")
                        end_lines()
                else:
                    print("ERROR : Inavalid Option Choosen")
                    end_lines()
            else:
                print("PIN is INCORRECT")
                end_lines()
            
        elif account_type == 2:
            print()
            print("Saving Account")
            print()
            print("< Sorry this service is not available at this movement >")
            end_lines()
        else:
            print("ERROR : Inavalid Option Choosen")
            end_lines()
        
    elif language==2:
        print("Hindi")
        print()
        print("< Sorry this service is not available at this movement >")
        end_lines()
    elif language==3:
        print("Marathi")
        print()
        print("< Sorry this service is not available at this movement >")
        end_lines()
    else:
        print("ERROR : Inavalid Option Choosen")
        end_lines()

else:
    print("ERROR : User Not Found")
    end_lines()

