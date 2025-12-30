total = 0
n = int(input("Enter number on blood sugar readings: "))

for i in range(n):
        sugar = int(input("Enter blood sugar value"))
        total = total + sugar

average = total/n
 
if average > 140:
    print("Low risk")
else:
    print("High risk")
