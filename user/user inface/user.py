import requests

# Replace with your actual bank API endpoint and credentials
api_url = "https://api.yourbank.com/accounts"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.get(api_url, headers=headers)
data = response.json()

checking_balance = data['checking_balance']
savings_balance = data['savings_balance']

print(f"Checking Account Balance: ${checking_balance}")
print(f"Savings Account Balance: ${savings_balance}")




import random
from datetime import datetime, timedelta

# Function to generate a fake bank balance
def generate_balance():
    return round(random.uniform(1000, 10000), 2)

# Function to create a fake statement
def generate_statement(account_number):
    start_date = datetime.now() - timedelta(days=30)
    transactions = []
    
    for _ in range(10):  # Generate 10 fake transactions
        date = start_date + timedelta(days=random.randint(1, 30))
        amount = round(random.uniform(-500, 500), 2)
        transactions.append(f"{date.strftime('%Y-%m-%d')}: {'Deposit' if amount > 0 else 'Withdrawal'} ${abs(amount)}")
    
    return transactions

# Main function to display fake balance and statement
def display_fake_account_info():
    account_number = "1234567890"
    balance = generate_balance()
    statement = generate_statement(account_number)

    print(f"Account Number: {account_number}")
    print(f"Current Balance: ${balance}")
    print("\nRecent Transactions:")
    for transaction in statement:
        print(transaction)

if __name__ == "__main__":
    display_fake_account_info()


import random

def generate_fake_balance():
    return round(random.uniform(0, 5000), 2)

def print_fake_account_info(account_type):
    balance = generate_fake_balance()
    print(f"{account_type} Account Balance: ${balance}")

def prank_account_info():
    print("Welcome to the Fake Bank!")
    print_fake_account_info("Checking")
    print_fake_account_info("Savings")

if __name__ == "__main__":
    prank_account_info()

