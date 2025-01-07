'''
name = "vicky"
print(name.upper())

a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a))  

name = "vickyopen"
print("hi " + name)

a = 10
b = 10
c = a+b

print (f"Total {c}")

print(len(name))

print(name.find("i"))
print(name.replace("i","z"))
print(name.isalpha())
print(name.isdigit())
print(name * 5)

otp = 78547 

print(f"your otp is {otp}") 

count = "29"
#result = int(count) + 1
#print(f"count = {result}")
print(int(count)+1)

count = 14.5
print(float(count)+2)

#Assignment

Name = "Anand"
Leave_balance = 15
Year = 2021

print(f"{Name} {Leave_balance} {Year}")


name = input("Whats your name: ")
print ("Hello " + name)

height = float(input("whats your height: "))
height_inches = "{:.2f}".format (height/2.14)
#print(type(height))
print ("Your height " + str(height) + " cm")
print ("Your height " + height_inches + " inches tall")
'''

'''
# Assignment
name = "Vicky "
email_id = "vicky@gmail.com"
phone_number = 7895463215

print(name + "Smile")
print(str(phone_number) + " yup")

name = input("whats your name ")
email = input("your mail id ")
phone_number = input("your phone number ")

print(name + " Thankyou")
print(email + " Thankyou")
print(phone_number + " Thankyou")


pwd_correct = False  

if pwd_correct:
    print("Logged In")
    print("Have A Nice Day")
else:
    print("Incorrect pwd")
    print ("Exited")

print("Bye")

print (" ")

number = 505

if number % 50 == 0: 
    print (str(number) + " its correct")
else:
    print (str(number) + " its incorrect")


#ellif ladder

ind_score = 420

if ind_score >= 450:
    print("India will win")
elif ind_score >= 400:
    print("India might win")
elif ind_score >= 200:
    print("Austraila might win")
else:
    print ("Austraila will win")

#nested if
# logical operators - and or not
num = int(input("Enter a number: "))

if num > 99 and num < 1000:
    if num %2 == 0:
        print(str(num) + " is a three digit even number")
    if num %3 == 0: 
        print(str(num) + " is a three digit odd number")
else:
    print(str(num) + " its not a three digit even number")



name = "poco"

print(name[3])
print(name[:4])
print(name[0:])

'''

# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print('*' * i)

# Number of rows
#n = 5

# Outer loop for rows
#for i in range(1, n + 1):
    # Print '*' i times
    #print('*' * i)

'''
cost_of_apple = 5
apple_input = input("how may apples you need ? ")
total_sum = (int(cost_of_apple * int(apple_input)))
print ("Total you need to pay is " + total_sum)
'''

for x in range(1,6):
    print(x, end=" ")

