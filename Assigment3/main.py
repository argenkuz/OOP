from amount import Amount
from personalaccount import PersonalAccount

if __name__ == "__main__":
    deposit = Amount(100.50, "DEPOSIT")
    withdrawal = Amount(50.75, "WITHDRAWAL")
    account1 = PersonalAccount(230120112, "Argen Kulzhanov", 9999 )
    print(deposit)
    print(withdrawal)
    print(f'Current balance account{account1.get_balance()}')

    print(f'Account number: {account1.get_account_number()}')
    account1.set_account_number('987652')
    print(f'After changing the account number {account1.get_account_number()}')

    print(f'Account holder: {account1.get_account_holder()}')
    account1.set_account_holder('Argen ')
    print(f'After changing account holder: {account1.get_account_holder()}')

    print(account1.__str__())

    account1.__add__(200)

    account1.__sub__(100)

    print(f'After adding and sustractig balabce {account1.get_balance()}')