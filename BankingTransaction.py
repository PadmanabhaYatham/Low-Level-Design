from abc import ABC, abstractmethod


class BankingOrder:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.price = []
        self.credit_cnt = 0
        self.debit_cnt = 0
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order_id):
        pass


class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, order_id):
        pass


class CreditPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verify = False

    def auth_sms(self, code):
        print("verifying Authentication")
        self.verify = True

    def pay(self, order_id):
        print("processing Payment")
        print(f"verifying user code: {self.security_code}")
        order.credit_cnt += 1
        order.status = "paid"


class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verify = False

    def auth_sms(self, code):
        print("verifying Authentication")
        self.verify = True

    def pay(self, order_id):
        print("Withdrawl has done")
        print(f"verifying user code: {self.security_code}")
        order.debit_cnt += 1
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, email):
        self.email = email
        self.verify = False

    def auth_sms(self, code):
        print("verifying Authentication")
        self.verify = True

    def pay(self, order_id):
        print("Withdrawl has done")
        print(f"verifying user email: {self.email}")
        order.debit_cnt += 1
        order.status = "paid"


class CrreditCardPaymentProcessor(PaymentProcessor):
    def __init__(self, code):
        self.email = code

    def pay(self, order_id):
        print("Withdrawl has done")
        print(f"verifying user email: {self.email}")
        order.debit_cnt += 1
        order.status = "paid"


order = BankingOrder()
order.add_item("keyboard", 1, 200)
order.add_item("SSD", 1, 500)
order.add_item("USB cable", 2, 100)

print(order.total_price())
processor = PaypalPaymentProcessor("12345678908765432")
processor.pay(order)
processor = DebitPaymentProcessor("786")
processor.pay(order)
processor = CreditPaymentProcessor("34567")
processor.pay(order)

print(order.credit_cnt, order.debit_cnt)
