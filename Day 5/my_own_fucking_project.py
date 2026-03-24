# Move lists OUTSIDE the loop so data persists
category_list = []
description_list = []
amount_list = []

# Main loop - keeps running until user exits
while True:
    print("\n" + "=" * 40)
    print("💰 EXPENSE TRACKER")
    print("=" * 40)
    work = input(
        "1. Add expense\n2. View all expenses\n3. Total spent\n4. View total by category\n5. Exit\n\nYour choice: ")

    if work == "1":
        print("\n--- Add Expense ---")
        category = input("Category: ")
        category_list.append(category)
        description = input("Description: ")
        description_list.append(description)
        amount = input("Amount: ")
        amount_list.append(amount)
        print("✅ Expense added successfully!")

    elif work == "2":
        print("\n--- All Expenses ---")
        if len(category_list) == 0:
            print("No expenses yet.")
        else:
            for i in range(len(category_list)):
                print(f"{i + 1}. {category_list[i]} | {description_list[i]} | ${amount_list[i]}")

    elif work == "3":
        print("\n--- Total Spent ---")
        total = 0
        for amount in amount_list:
            total = total + float(amount)
        print(f"Total: ${total}")

    elif work == "4":
        print("\n--- Total by Category ---")
        # Will implement this next if you want
        print("Feature coming soon!")

    elif work == "5":
        print("\n👋 Goodbye!")
        break  # This exits the loop

    else:
        print("❌ Invalid choice. Please enter 1-5.")





# work = input("1. Add expense \n2. View all expenses \n3. Total spent \n4. View total by category \n5. Exit")
# category_list = []
# description_list = []
# amount_list = []
# if work == "1":
#     print("Add expense")
#     category = input("Please add Category")
#     category_list.append(category)
#     description = input("Please add Description")
#     description_list.append(description)
#     amount = input("Please add Amount")
#     amount_list.append(amount)
#     input("1. Add an other expense and 2. Back to the main menu")
# elif work == "2":
#     print("View expense")
#     print
# elif work == "3":
#     print("Total spent")
# elif work == "4":
#     print("View total by category")
# elif work == "5":
#     print("Exit")
# print(category_list, description_list, amount_list)