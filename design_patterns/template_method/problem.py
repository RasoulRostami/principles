# Bank application
# We would like to log every single activities


class ActivityLog:
    def log(self):
        print("> logging activity")


class Deposit:
    def __init__(self) -> None:
        self.activity_log = ActivityLog()

    def deposit(self):
        print("client deposit from his/her account.")
        self.activity_log.log()


class Withdraw:
    def __init__(self) -> None:
        self.activity_log = ActivityLog()

    def withdraw(self):
        print("client withdraw from her account.")
        self.activity_log.log()


if __name__ == "__main__":
    deposit = Deposit()
    withdraw = Withdraw()
    deposit.deposit()
    withdraw.withdraw()

# Problems:
# 1. we will have to many duplicate codes
# 2. we might forget to use activity log in future Activity classes
# 3. we are not forced to implement log function to our method or class,
# when a new developer join to team, he will violate rules.
# 4. overriding log might be very hard
