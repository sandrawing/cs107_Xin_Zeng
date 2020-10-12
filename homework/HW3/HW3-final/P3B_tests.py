from Bank import BankAccount, BankUser, AccountType


def test_over_withdrawal():
    user = BankUser("XinZeng")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 100)

    # test for invalid situation
    # deposit a negative value
    try:
        user.deposit(AccountType.SAVINGS, -1)
    except Exception as e:
        print(e)

    # withdraw more than balance
    try:
        user.withdraw(AccountType.SAVINGS, 200)
    except Exception as e:
        print(e)

    # withdraw a negative value
    try:
        user.withdraw(AccountType.SAVINGS, -1)
    except Exception as e:
        print(e)

    # open multiple saving account
    try:
        user.addAccount(AccountType.SAVINGS)
    except Exception as e:
        print(e)

    # withdraw from a different account
    try:
        user.withdraw(AccountType.CHECKING, 20)
    except Exception as e:
        print(e)

    # deposit to a different account
    try:
        user.deposit(AccountType.CHECKING, 1)
    except Exception as e:
        print(e)

    # get balance from wrong account
    try:
        user.getBalance(AccountType.CHECKING)
    except Exception as e:
        print(e)

    # test for valid situation
    user.withdraw(AccountType.SAVINGS, 50)
    print("Balance:", user.getBalance(AccountType.SAVINGS))
    print(user)
    print(str(user))
    print(str(user.account[AccountType.SAVINGS]))
    user.addAccount(AccountType.CHECKING)
    print("Balance:", user.getBalance(AccountType.CHECKING))
    print(user)
    print(str(user.account[AccountType.CHECKING]))


test_over_withdrawal()

# test result
'''
Not able to deposit a negative amount into your account.
Attempting to withdraw more than the current balance.
Not able to withdraw a negative amount from your account.
SAVINGS already exists.
CHECKING not exists.
CHECKING not exists.
CHECKING not exists.
Balance: 50
Account owner: XinZeng, has accounts and balance: [('Savings', 50)]
Account owner: XinZeng, has accounts and balance: [('Savings', 50)]
Account owner: XinZeng. Type of account: SAVINGS
Balance: 0
Account owner: XinZeng, has accounts and balance: [('Savings', 50), ('Checking', 0)]
Account owner: XinZeng. Type of account: CHECKING
'''