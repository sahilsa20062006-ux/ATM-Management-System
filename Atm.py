class Atm:

    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.__transactions = []

        self.menu()

    # # Setter                      # (This is for Set a amount by ourself)
    # def set_balance(self,amount):
    #     if amount >= 0:
    #         self.__balance = amount
    #     else:
    #         print("Balance cannot be negative")

    def menu(self):
        while True:
            user_input = input("""
                            hi how can i help you!
                            1. Press 1 to create pin
                            2. Press 2 to change pin
                            3. Press 3 to check balance
                            4. Press 4 to withdraw
                            5. Press 5 to Deposit money
                            6. Press 6 to Transaction History
                            7. Press any other key to exit
                            """)
            
            if user_input == '1':
                # Create pin
                self.__create_pin()
            elif user_input == '2':
                # Change pin
                self.__change_pin()
            elif user_input == '3':
                # Check balance
                self.__check_balance()
            elif user_input == '4':
                # Withdrow
                self.__withdraw()
            elif user_input == '5':
                # Deposit money
                self.__money_deposit()
            elif user_input == '6':
                # Transaction History
                self.__transaction_history()
            else:
                print('Thank you for using ATM')
                break

    def __create_pin(self):
        if self.__pin == '':
            user_pin = input('Enter your pin :')
            if user_pin.isdigit() and len(user_pin) == 4:
                self.__pin = user_pin
                print('PIN created successfully')
            else:
                print('Invalid PIN. Please enter a 4-digit PIN.')
        else:
            print('your PIN is already created')
    
    def __change_pin(self):
        if self.__pin != '':
            old_pin = input('Enter your old pin :')
            if old_pin == self.__pin:
                new_pin = input('Enter your new pin :')
                if new_pin.isdigit() and len(new_pin) == 4:
                    self.__pin = new_pin
                    print('PIN Changed successfully')
                else:
                    print('Invalid PIN. Please enter a 4-digit PIN.')
            else:
                print('Given PIN is incorrect')
        else:
            print('create your PIN first. your PIN is not created!')

    def __check_balance(self):
        if self.__pin != '':
            user_pin = input('Enter your pin :')
            if user_pin == self.__pin:
                print(f'Your balance is ₹{self.__balance}')
            else:
                print('Given PIN is incorrect')
        else:
            print('create your PIN first. your PIN is not created!')

    def __withdraw(self):
        if self.__pin != '':
            user_pin = input('Enter you pin :')
            if user_pin == self.__pin:
                try:
                    withdraw_amount = int(input('Enter withdraw amount :'))
                except ValueError:
                    print("Please enter numbers only")
                    return
                if withdraw_amount <= self.__balance and withdraw_amount > 0:
                    self.__balance = self.__balance - withdraw_amount
                    self.__transactions.append(f"Withdrawn ₹{withdraw_amount}")
                    print('Amount withdrawn successfully')
                    print(f'Remaining balance: ₹{self.__balance}')
                else:
                    print('Insufficient balance or pls enter correct amount')
            else:
                print('Given PIN is incorrect')
        else:
            print('create your PIN first. your PIN is not created!')

    def __money_deposit(self):
        if self.__pin != '':
            user_pin = input('Enter your pin :')
            if user_pin == self.__pin:
                try:
                    deposit_amount = int(input('Enter Deposit amount :'))
                except ValueError:
                    print('Please enter numbers only')
                    return
                if deposit_amount > 0:
                    self.__balance = self.__balance + deposit_amount
                    print(f'Amount deposited successfully. New balance: ₹{self.__balance}')
                    self.__transactions.append(f"Deposited ₹{deposit_amount}")
                else:
                    print('Enter your amount correctly')
            else:
                print('Given PIN is incorrect')
        else:
            print('create your PIN first. your PIN is not created!')

    def __transaction_history(self):
        if self.__pin != '':
            user_pin = input('Enter your pin :')
            if user_pin == self.__pin:
                if len(self.__transactions) == 0:
                    print("No transactions found")
                else:
                    for transaction in self.__transactions:
                        print(transaction)
            else:
                print('Given PIN is incorrect')
        else:
            print('create your PIN first. your PIN is not created!')


obj = Atm()