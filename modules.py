# import calendar as cal
# print("------calender program in python----\n")
# print("Enter 'X' for Exit ")
# y =input("Enter Year:")
# if y=='x':
#  exit()
# else:
#  m =input("Enter Month:")
# yy=int(y)
# mm=int(m)
# print("\n",cal.month(yy,mm))

#control statements
#If-Else-elif
num=12
if num>0:
    print(f"number {num } is positive")
elif num<0:
    print(f"number {num} is negative")
else:
    print(f"number {num} is zero or not valid input")

    #For loop
for i in range (1,5):
 print(i)
for i in range (5,1,-1):
   print(i)

   #While
   print("while loop")
count=1
while count<=5:
   print(count)
   count = count+1
   #Break
for i in range (1,10):
   if i==5:
      print("Break Apply at ",num)
      break
print(f"Loop iterate:{i}")

#continue
for i in range(1,10):
   if i%2==0:
      continue
   print(i)

   #pass
for i in range(1,5):
   pass

#function
def greet():
   print("hello")
   greet()

   def add(x,y):
      return x+y
   print(add(2,3))