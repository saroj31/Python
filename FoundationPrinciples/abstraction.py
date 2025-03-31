from protocol import Logger

class PaymentBase:

    def __init__(self, amount: int):
        self.amount: int = amount

    def process_payment(self):
        pass

class CreditCard(PaymentBase):
    def process_payment(self):
        msg = f"Credit card payment: {self.amount}"
        print(msg)

    def log(self, message: str):
        print(f"logging CreditCard: {message}")

class PayPal(PaymentBase):
    def process_payment(self):
        msg = f"Paypal payment: {self.amount}"
        print(msg)

    def log(self, message: str):
        print(f"logging paypal payment: {message}")


def log_message(logger: Logger, msg: str):
    print(logger.log(msg))

if __name__ == '__main__':
    
    payments = [CreditCard(100), PayPal(200)]

    for payment in payments:
        payment.process_payment()

        log_message(payment, "Testing protocol")

