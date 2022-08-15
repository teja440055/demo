


username="lucky"
pass_code="1432"
print('welcome to non reserved bank atm')

user=input('enter username:' ' ')
passcode=int(input('enter pass_code: ' ''))

if username=='lucky':
   print('username right')
else:
    print('incorrect username')
print()    

if pass_code=='1432':
         print('Authentication sucessfull') 
else:
         print('get out hacker')  
options= input ('''select an option :
'cash' for cash_withdrawl
'bal' for balance_check
'pin' for pin_change  ''')

if options == 'cash':
    print("you got cash 5000, how much would you with draw")
elif options == 'bal':
    print('balace check 10000') 
elif options == 'pin':
    print('enter new and old pin') 
else:
    print('Request timed out')    



   
    

