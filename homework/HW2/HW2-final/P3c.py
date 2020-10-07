def make_withdrawal(balance):
    def inner(amount):
        nonlocal balance
        if amount <= balance:
            new_bal = balance - amount
            balance = new_bal
            return new_bal
        else:
            raise ValueError("attempting to withdraw more than the current balance")
    return inner


# test whether it behaves as expected
try:
    init_balance, withdrawal_amount, new_withdrawal_amount = 300, 20, 10
    wd = make_withdrawal(init_balance)
    print("After the first withdrawl, the remaining amount of money is " + str(wd(withdrawal_amount)))
    print("After the second withdrawl, the remaining amount of money is " + str(wd(new_withdrawal_amount)))
except UnboundLocalError as info:
    print(info)