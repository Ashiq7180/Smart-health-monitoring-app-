total = 0
n = int(input("Enter number on blood sugar readings: "))

for i in range(0,n-1):
        sugar = int(input("Enter blood sugar value"))
        total = total + sugar

average = total/n
 
if average > 140:
    print("High risk")
else:
    print("Low risk")
