#Send a email with details of online purchasing
#max. of 3 (three) attempts.

confirmed_order = True

purchase_data = '$12,50 buy order confirmed, and the package has sended.'

for sendMessage in range(3): #the for loop "sendMessage" with range (3)
    if confirmed_order: #if "confirmed_order" variable is true, execute:
        print(purchase_data)
        print('Order details sended to your email.')
        break #break is here to stops the for loop with just one successful attempt
else:
    print('Order failed.')