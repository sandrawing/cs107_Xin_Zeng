from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():
	def __init__(self, owner, accountType: AccountType):
		self.owner = owner
		self.accountType = accountType
		self.balance = 0

	def withdraw(self, amount):
		if amount > self.balance:
			raise ValueError('Attempting to withdraw more than the current balance.')
		elif amount < 0:
			raise ValueError('Not able to withdraw a negative amount from your account.')
		else:
			self.balance -= amount

	def deposit(self, amount):
		if amount < 0:
			raise ValueError('Not able to deposit a negative amount into your account.')
		else:
			self.balance += amount

	def __str__(self):
		return "Account owner: {}. Type of account: {}".format(self.owner, self.accountType.name)

	def __len__(self):
		return self.balance


class BankUser():
	def __init__(self, owner):
		self.owner = owner
		self.account = {}
		self.account_dict = {AccountType.SAVINGS: 0, AccountType.CHECKING: 0}

	def addAccount(self, accountType):
		self.account_dict[accountType] += 1
		if self.account_dict[accountType] > 1:
			raise TypeError('{} already exists.'.format(accountType.name))
		else:
			self.account[accountType] = BankAccount(self.owner, accountType)

	def getBalance(self, accountType):
		if accountType not in self.account.keys():
			raise TypeError('{} not exists.'.format(accountType.name))
		else:
			return self.account[accountType].balance

	def deposit(self, accountType, amount):
		if accountType not in self.account.keys():
			raise TypeError('{} not exists.'.format(accountType.name))
		else:
			self.account[accountType].deposit(amount)

	def withdraw(self, accountType, amount):
		if accountType not in self.account.keys():
			raise TypeError('{} not exists.'.format(accountType.name))
		else:
			self.account[accountType].withdraw(amount)

	def __str__(self):
		a = [('Savings' if k.value == 1 else 'Checking', len(value)) for k, value in self.account.items()]
		return "Account owner: {}, has accounts and balance: ".format(self.owner) + str(a)


def ATMSession(user):
	def Interface():
		while True:
			try:
				operation = int(input("Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n"))
				if operation == 1:
					break
				elif operation >= 2 and operation <= 5:
					acc_num = int(input("Enter Option:\n1)Checking\n2)Savings\n"))
					if acc_num != 1 and acc_num != 2:
						print('Please enter a integer 1 or 2.')
						continue
					acc_type = AccountType(-acc_num+3)
					if operation == 2:
						user.addAccount(acc_type)
						print("Account {} created successfully.".format(acc_type.name))
					elif operation == 3:
						print("{} Balance: {}".format(acc_type.name, user.getBalance(acc_type)))
					elif operation == 4:
						amount = int(input("Enter Interger Amount, Cannot Be Negative."))
						user.deposit(acc_type, amount)
						print("{} deposit {} successfully.".format(acc_type.name, amount))
					else:
						amount = int(input("Enter Interger Amount, Cannot Be Negative or More Than Balance:"))
						user.withdraw(acc_type, amount)
						print("{} withdraw {} successfully.".format(acc_type.name, amount))
				else:
					print('Please enter a integer between 1 and 5.')
			except Exception as e:
				print(e)
	return Interface


# if __name__ == '__main__':
# 	user = BankUser('test')
# 	ATMSession(user)()
