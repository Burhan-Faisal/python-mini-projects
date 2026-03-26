import termcolor,sqlite3
""""
This project introduces basic Object-Oriented Programming (OOP) concepts by encapsulating the ATM's logic within a class and 
handling user interactions through a ATMcontroller class.

"""


class ATM:
    options=['Check Balance','Deposit','Withdraw','Transaction History','Exit']
    choices=[1,2,3,4,5]
    MAX_PIN_ATTEMPTS=5
    def __init__(self):
        self.balance=0
        self.conn=sqlite3.connect("userinfo.db")
        self.cursor=self.conn.cursor()
        self.__createtable()
        #self.__addusers() # Executes only when wants to add user ensuring authentication

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
    
        self.balance += amount

        self.cursor.execute(
        "INSERT INTO transactions (user_id, type, amount) VALUES (?, ?, ?)",
        (self.user_id, "DEPOSIT", amount)
        )
        self.cursor.execute(
        "UPDATE credentials SET balance = ? WHERE acc_id = ?",
        (self.balance, self.user_id)
         )
        self.conn.commit()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')

        self.balance-=amount

        self.cursor.execute(
        "INSERT INTO transactions (user_id, type, amount) VALUES (?, ?, ?)",
        (self.user_id, "WITHDRAW", amount)
        )

        self.cursor.execute(
        "UPDATE credentials SET balance = ? WHERE acc_id = ?",
        (self.balance, self.user_id)
         )
        self.conn.commit()


    def get_pin(self,pin):
        if not pin.isdigit():
            raise ValueError("Pin should have only digits")
        if not len(pin)==4:
            raise ValueError("Pin should have only Four Digits.")
        self.cursor.execute('SELECT * from credentials where pin=?',(int(pin),))
        user=self.cursor.fetchone()
        if user:
            self.user_id = user[0]
            self.balance = user[2]
            return True
        return False
    

    def __addusers(self):
        '''UNDERSTANDING THE ATM SYSTEM BY MANUALLY ADDING THE USERS'''
        self.cursor.execute("INSERT INTO Credentials (pin,balance) VALUES (?,?)",(8765,0))
        self.cursor.execute("INSERT INTO Credentials (pin,balance) VALUES (?,?)",(3052,0))
        self.cursor.execute("INSERT INTO Credentials (pin,balance) VALUES (?,?)",(9854,0))
        self.conn.commit()



    def __createtable(self):
        self.cursor.executescript(
        """
    CREATE TABLE IF NOT EXISTS Credentials (
        acc_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pin INTEGER,
        balance REAL
    );
                              
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        amount REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES Credentials(acc_id)
    );
    
    """)
    
    def get_transaction_history(self):    
        self.cursor.execute(
        "SELECT type, amount, timestamp FROM transactions WHERE user_id = ?",
        (self.user_id,)
         )
        return self.cursor.fetchall()

class AtmController:

    def __init__(self):
        self.atm=ATM()

    def display_menu(self):
        for index,option in enumerate(ATM.options,start=1):
            print(f'{index}. {option}')


    def check_balance(self):
        print(f"Your current balance is ${self.atm.balance}")
    

    def deposit_amount(self):
        while True:
            try:
                amount = AtmController.get_number()
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount}.')
                break
            except ValueError as error:
                print(error)  

    @staticmethod
    def get_number():
        while True:
            amount=int(input("Enter the Amount: $"))
            if not amount.is_integer():
                print("Please Enter the Amount in Whole Numbers!")
                continue
            return amount


    def withdraw(self):
        while True:
            try:
                amount = AtmController.get_number()
                self.atm.withdraw(amount)
                print(f'Successfully withdrew ${amount}.')
                break
            except ValueError as error:
                print(error)

         
    @staticmethod
    def get_choice():
        while True:
            try: 
                choice=int(input('Please Choose an option: '))
                if choice not in ATM.choices:
                    print("Invalid Choice !")
                else:
                    return choice
            except ValueError:
                print("Invalid Choice")
    

    def transaction_history(self):

        history = self.atm.get_transaction_history()
        print("\n--- Transaction History ---")

        if not history:
            print("No transactions yet.")

        else:
            for i, (t_type, amount, time) in enumerate(history, start=1):
                print(f"{i}. {t_type}  ${amount}  on {time}")

    def get_pin(self):
        attempts=0
        while attempts<5:
            try:
                pin=input("Enter Your Pin :").strip()
                if self.atm.get_pin(pin):
                    return True
                else:
                    attempts+=1
                    remaining = ATM.MAX_PIN_ATTEMPTS - attempts
                    if remaining > 0:
                        termcolor.cprint(
                            f"Wrong PIN! {remaining} attempt(s) remaining.", 'red')
            except ValueError as e:
                print(e)
    
        termcolor.cprint("Too many failed attempts. Card blocked.", 'red')
        return False
    
    def main(self):
        print("Welcome to the ATM..")

        if not self.get_pin():
            exit()

        else:
            while True:
                print("Welcome to the ATM")
                self.display_menu()
                choice=self.get_choice()
                if choice==1:
                    self.check_balance()
                elif choice==2:
                    self.deposit_amount()
                elif choice==3:
                    self.withdraw()
                elif choice==4:
                    self.transaction_history()
                else:
                    exit()
        termcolor.cprint("You have used your maximum attempts",'red',on_color='on_white') 

p1=AtmController()
p1.main()
