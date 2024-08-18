num = float(input("enter num: "))
if(num % 2 != 0):
    
    print("it's odd") 
    for i in range(2, int(num)):
      if(num % i != 0):
         print("it's odd prime") 
         break 
    else: 
         print("it's odd composite")
else:
    print("it's even")