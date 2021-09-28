class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.other_user = other_user
        self.amount = amount
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

User1 = User("James Bond", "jb@email.com")
User2 = User("John Wick", "jw@email.com")
User3 = User("Jack Ryan", "jr@email.com")

User1.make_deposit(1000000)
User1.make_deposit(2500000)
User1.make_withdrawal(750000)
User1.display_user_balance()

User2.make_deposit(500000)
User2.make_deposit(3000000)
User2.make_withdrawal(250000)
User2.make_withdrawal(75000)
User2.display_user_balance()

User3.make_deposit(100000)
User3.make_withdrawal(10000)
User3.make_withdrawal(5000)
User3.make_withdrawal(7500)
User3.display_user_balance()

User1.transfer_money(User3, 500000)
User1.display_user_balance()
User3.display_user_balance()