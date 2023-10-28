import mysql.connector

# MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Admin123',  # Replace with your MySQL root user password
    'database': 'anmol_bank',  # Replace with the name of your database
}

def display_menu():
    print("Welcome to Anmol Bank")
    print("1. Add Customer")
    print("2. Add Account")
    print("3. Add Transaction")
    print("4. View Customers")
    print("5. View Accounts")
    print("6. View Transactions")
    print("0. Exit")

def add_customer(cursor):
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    contact_details = input("Enter customer contact details: ")
    
    # Insert customer data into the Customers table
    cursor.execute(
        "INSERT INTO Customers (name, address, contact_details) VALUES (%s, %s, %s)",
        (name, address, contact_details)
    )
    print("Customer added successfully!")

def add_account(cursor):
    customer_id = int(input("Enter customer ID: "))
    account_number = input("Enter account number: ")
    account_type = input("Enter account type: ")
    balance = float(input("Enter account balance: "))
    
    # Insert account data into the Accounts table
    cursor.execute(
        "INSERT INTO Accounts (customer_id, account_number, account_type, balance) VALUES (%s, %s, %s, %s)",
        (customer_id, account_number, account_type, balance)
    )
    print("Account added successfully!")

def add_transaction(cursor):
    account_id = int(input("Enter account ID: "))
    transaction_type = input("Enter transaction type (deposit/withdrawal/transfer): ")
    amount = float(input("Enter transaction amount: "))
    
    # Insert transaction data into the Transactions table
    cursor.execute(
        "INSERT INTO Transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)",
        (account_id, transaction_type, amount)
    )
    print("Transaction added successfully!")

def view_customers(cursor):
    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()
    if customers:
        print("Customers:")
        for customer in customers:
            print(customer)
    else:
        print("No customers found.")

def view_accounts(cursor):
    cursor.execute("SELECT * FROM Accounts")
    accounts = cursor.fetchall()
    if accounts:
        print("Accounts:")
        for account in accounts:
            print(account)
    else:
        print("No accounts found.")

def view_transactions(cursor):
    cursor.execute("SELECT * FROM Transactions")
    transactions = cursor.fetchall()
    if transactions:
        print("Transactions:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions found.")

def main():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")

        cursor = connection.cursor()

        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                add_customer(cursor)
            elif choice == '2':
                add_account(cursor)
            elif choice == '3':
                add_transaction(cursor)
            elif choice == '4':
                view_customers(cursor)
            elif choice == '5':
                view_accounts(cursor)
            elif choice == '6':
                view_transactions(cursor)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

    except mysql.connector.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
