import json
import os
import csv
from datetime import datetime

fileName = 'Data.json'
csvFile = 'transaction.csv'

if os.path.exists(fileName):
    with open(fileName, 'r') as file:
        transaction = json.load(file)
else:
    transaction = []
    
def saveData():
    with open(fileName, 'w') as file:
        json.dump(transaction, file, indent=4)  

def showMenu():
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transaction")
    print("4. Show Balance")
    print("5. Deleted all transaction")
    print("6. Export to CSV file")
    print("7. Exit")

def addTransaction(type_):
    try:
        amount = float(input(f"Enter {type_} amount: ₹"))
        description = input("Enter Description: ")
        now = datetime.now()
        transaction.append({
        'date': now.strftime("%Y-%m-%d"),
        'time': now.strftime("%H:%M:%S"),    
        'type': type_,
        'amount' : amount,
        'description' : description
        })
        saveData()
        print(f"{type_} added successfuly!")
    except ValueError:
        print("Invalid amount pleases re-enter")
    
    
def clearTransaction():
    confirm = input("Are you sure (yes/no): ") 
    if confirm == "yes":
        transaction.clear()
        saveData()
        print("Successfully deleted")
    else:
        print("Not deleted")          

def viewTransaction():
    if not transaction:
        print("No transaction")
    
    for t in transaction:
        print(f"{t['date']} | {t['time']} | {t['type']} : ₹{t['amount']} - {t['description']}")    
     
def showBalance():
    income = sum(t['amount'] for t in transaction if t['type'] == 'Income')
    expense = sum(t['amount'] for t in transaction if t['type'] == 'Expense')
    balance = income - expense
    print(f"\nTotal Income: ₹{income}")
    print(f"\nTotal Expense: ₹{expense}")
    print(f"\ncurrent balance: ₹{balance}")
    
def saveCSV():
    if not transaction:
        print("There is no data to export")
        return
    
    with open(csvFile, 'w', newline='') as file:
       writer = csv.DictWriter(file, fieldnames=transaction[0].keys())
       writer.writeheader()
       writer.writerows(transaction)
            
    print(f"Data exported successfully to {csvFile}")           
    

while True:
    showMenu()
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        addTransaction("Income")            
    elif choice == 2:
        addTransaction("Expense")
    elif choice == 3:
        viewTransaction()
    elif choice == 4:
        showBalance()
    elif choice == 5:
        clearTransaction() 
    elif choice == 6:
        saveCSV()    
    elif choice == 7:
        exit()    
    else:
        print("Invalid choice")                