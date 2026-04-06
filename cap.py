
#Capitilize constants. VAR
# raturn 0 <= rate <= 5.  returns true if greater than or equals to 0 and less than or equals to 5

class Bank:
  MIN_BALANCE = 100
  def __init__(self, name, amount, balance):
    self.name = name
    self.amount = amount
    self._balance = balance

  def deposit(self, amount):
    if self._is_valid_amount(amount):
      self._balance += amount
    else:
      raise ValueError("Deposit amount should be positive")
    
  def _is_valid_amount( self, amount):
    return self.amount > 0
  
  def __log_transaction(self, amount):
    print(f"Logging trannsaction of amount: {amount} at {datetime.now()}")


#Encapsulation
class BadBank:
  def __init__(self, balance):
    self.balance = balance

account = BadBank(1000)
account.balance = 300
print(account.balance)

class GoodBank:  #no setter, should not change the balace directly
  def __init__(self):
    self._balance = 1000

  @property
  def balance(self):
    return self._balance
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Insufficient funds")
    self._balance += amount
  
  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Invalid amount")
    if amount > self._balance:
      raise ValueError("Insufficient funds")
    self._balance -= amount

account1 = GoodBank()
print(account1.balance)
account1.deposit(5030)
print(account1.balance)
account1.withdraw(4732)
print(account1.balance)


#Abstraction
class EmailService:

  def _connect(self):
    print("Connecting to Email Server...")

  def _authenticate(self):
    print("Authenticating...")

  def send_email(self):
    self._connect()
    self._authenticate()
    print("Sending email...")
    self._disconnect()

  def _disconnect(self):
    print("Disconnecting from email server...")

email1 = EmailService()
email1.send_email()

#abstraction. 
#instead of
email2 = EmailService()
email2._connect()
email2._authenticate()
email2.send_email()
email2._disconnect()
