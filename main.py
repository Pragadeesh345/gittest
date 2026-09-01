def add_expense(expenses):
    while True:
        while True:
            try:
                amount=int(input("Enter the Amount:"))
                break
            except:
                print("Invalid input .. Try again")
        category=input("Enter the category:")
        date=input("Enter the date:")
        expense={
            "amount":amount,
            "category":category,
            "date":date
        }
        expenses.append(expense)
        back=input("Add Another Expense(yes/no):")
        if back.lower() == "no":
            break
def view_expenses(expenses):
    if not expenses:
        print("NO Expenses were stored")
        return
    for expense in expenses:
        print(f" Amount: ₹{expense['amount']} | Category: {expense['category']} | Date: {expense['date']}")
def total_spending(expenses):
    total=0
    for expense in expenses:
        total+=expense['amount']
    return total
def category_summarize(expenses):
    if not expenses:
        print("No Expenses to Summarize")
        return
    summary={}
    for expense in expenses:
        category=expense['category']
        if category in summary:
            summary[category]+=expense['amount']
        else:
            summary[category]=expense['amount']
    for category,amount in summary.items():
        print(f"{category}:₹{amount}")
def save_expenses(expenses):
    with open("data.txt","w") as file:
        for expense in expenses:
            data=f"{expense['amount']},{expense['category']},{expense['date']}"
            file.write(data+"\n")
def load_expenses():
    expenses=[]
    try:
        with open("data.txt","r") as file:
            for data in file:
                data=data.strip()
                parts=data.split(",")
                if len(parts)!=3:
                    continue
                amt=int(parts[0])
                cat=parts[1]
                dat=parts[2]
                expense={
                    "amount":amt,
                    "category":cat,
                    "date":dat
                    }
                expenses.append(expense)
    except FileNotFoundError:
        return []
    return expenses
def main():

    expenses=load_expenses()
    if not expenses:
        print("No previous data found. Starting fresh.")
    
    while True:

        print("MENU")
        print("1 ADD EXPENSE")
        print("2 VIEW EXPENSES")
        print("3 TOTAL SPENDING")
        print("4 CATEGORY EXPENSE")
        print("5 SAVE AND EXIT")

        while True:
            try:
                choice=int(input("Enter your choice:"))
                break
            except:
                print("Enter the number of your choice")
        
        if choice == 1:
            print("Adding a Expense:")
            add_expense(expenses)
        elif choice == 2:
            print("Viewing All Expenses")
            view_expenses(expenses)
        elif choice == 3:
            print("Calculating Total Amount Spent")
            total=total_spending(expenses)
            print(f"Total Spending:₹{total}")
        elif choice == 4:
            print("Category wise Expense")
            category_summarize(expenses)
        elif choice == 5:
            print("Saving and Exiting")
            save_expenses(expenses)
            break
main()        
        