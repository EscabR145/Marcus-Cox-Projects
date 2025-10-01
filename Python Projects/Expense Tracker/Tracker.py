import pandas as pn
import matplotlib as plt

# Welcome Message
print("Hello and Welcome to the Expense Tracker, this program\n" \
"will load in your expenses and show and visualize your statistics")

# Load in the file
expenseFile = pn.read_csv(r"C:\Users\DOMINATORV2\Desktop\Python Projects\Expense Tracker\expenses.csv")


#Ask user to load into the file
if(input("Would you Like to Add Expenses (Enter Y/N): ")== "Y" or "y"):
    date = input("Input Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    description = input("Enter Description: ")
    new_row = pn.DataFrame([[date,category,amount,description]],columns=["date","category","amount","description"])
    new_row.to_csv("expenses.csv",mode = 'a',header = False, index = False)

#Print out summary groupby category and amount
print(expenseFile.groupby("category")["amount"].sum())

