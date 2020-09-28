def make_withdrawal(balance):
    def inner(amount):
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

# explain why this does not behave correctly
explain = "This time it would give an error: local variable 'balance' referenced before assignment. " \
          "The reason is that : "\
          "If a name is bound in a block, it is a local variable of that block, unless declared as nonlocal or global. " \
          "In Python, assignments to names always go into the innermost scope. Assignments do not copy data " \
          "— they just bind names to objects. " \
          "Here inside inner(), balance is assigned through balance = new_bal. However, we have used amount <= balance before. " \
          "At that time, balance is unassigned so we can't use that."
print(explain)