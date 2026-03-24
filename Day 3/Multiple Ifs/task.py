# weight = float(input("What is your weight "))
# height = float(input("What is your height "))
#
# bmi = weight / ( height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
#
# print(round(bmi, 2))
#
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#         print("Normal weight")
# else:
#     print("overweight")
#

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <=12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Would you like to see the picture? (y/n)")
    if wants_photo == "y":
         bill += 3
    print(f"Your bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
