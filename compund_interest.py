def compund_interest(Profit, interest,time):
    interest  = Profit*((1+rate/100)**time)
    return interest
Profit = int(input("Money You bored: "))
rate=float(input("Enter the rate of interest: "))
time = float(input("The amount of time: "))
total_due =compund_interest(Profit,rate,time)
print("The amount of interest is: ",total_due)
