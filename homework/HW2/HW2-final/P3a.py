def make_withdrawal(balance):
    def inner(amount):
        if amount <= balance:
            new_bal = balance - amount
            return new_bal
        else:
            raise ValueError("attempting to withdraw more than the current balance")
    return inner


# test whether it behaves as expected
init_balance, withdrawal_amount, new_withdrawal_amount = 300, 20, 10
wd = make_withdrawal(init_balance)
print("After the first withdrawl, the remaining amount of money is " + str(wd(withdrawal_amount)))
print("After the second withdrawl, the remaining amount of money is " + str(wd(new_withdrawal_amount)))

# explain why this does not behave correctly
explain = "This does not behave correctly because for the two consecutive withdrawls, " \
          "we both pass 300 to the argument balance. " \
          "And the init_balance doesn't get updated between two consecutive withdrawls. " \
          "So each time, we are withdrawing money from 300."
print(explain)