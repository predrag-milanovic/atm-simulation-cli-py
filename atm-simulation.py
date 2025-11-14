# ----------------------
# ATM core functionality
# ----------------------
# The `ATM` class encapsulates the account balance and provides
# methods to check the balance, deposit funds and withdraw funds.
class ATM:
	def __init__(self):
		# Initialize account balance to zero.
		self.balance = 0.0

	def check_balance(self):
		# Return the current balance (float).
		return self.balance

	def deposit(self, amount):
		# Deposit a positive amount into the account.
		# Raises ValueError for non-positive amounts.
		if amount <= 0:
			raise ValueError('Deposit amount must be positive.')

		self.balance += amount

	def withdraw(self, amount):
		# Withdraw a positive amount from the account if funds exist.
		# Raises ValueError for non-positive amounts or insufficient funds.
		if amount <= 0:
			raise ValueError('Withdrawal amount must be positive.')
		if amount > self.balance:
			raise ValueError('Insufficient funds.')

		self.balance -= amount


# -------------------------
# User interaction / control
# -------------------------
# The `ATMController` handles input/output and uses an `ATM` instance
# to perform operations requested by the user.
class ATMController:
	def __init__(self):
		# Create an ATM instance to manage the balance.
		self.atm = ATM()

	def get_number(self, prompt):
		# Prompt the user for a numeric value (float). Keeps asking until
		# a valid number is entered.
		while True:
			try:
				number = float(input(prompt))
				return number
			except ValueError:
				print('Please enter a valid number.')

	def display_menu(self):
		# Print the main menu options.
		print('\nWelcome to the ATM!')
		print('1. Check Balance')
		print('2. Deposit')
		print('3. Withdraw')
		print('4. Exit')

	def check_balance(self):
		# Retrieve balance from ATM and display it formatted to 2 decimals.
		balance = self.atm.check_balance()
		print(f'Your current balance is: ${balance:.2f}')

	def deposit(self):
		# Prompt for deposit amount and attempt to deposit, showing errors
		# for invalid input.
		while True:
			try:
				amount = self.get_number('Enter the amount to deposit: ')
				self.atm.deposit(amount)
				print(f'Successfully deposited ${amount:.2f}.')
				break
			except ValueError as error:
				print(error)

	def withdraw(self):
		# Prompt for withdrawal amount and attempt to withdraw, showing
		# errors for invalid input or insufficient funds.
		while True:
			try:
				amount = self.get_number('Enter the amount to withdraw: ')
				self.atm.withdraw(amount)
				print(f'Successfully withdrew ${amount:.2f}.')
				break
			except ValueError as error:
				print(error)

	def run(self):
		# Main loop: display the menu and dispatch user choices until exit.
		while True:
			self.display_menu()

			choice = input('Please choose an option: ')
			if choice == '1':
				self.check_balance()
			elif choice == '2':
				self.deposit()
			elif choice == '3':
				self.withdraw()
			elif choice == '4':
				print('Thank you for using the ATM.')
				break
			else:
				print('Invalid choice. Please try again.')


# -----------------
# Program entrypoint
# -----------------
# Create an `ATMController` and start the interactive loop when the
# module is executed directly.
def main():
	atm = ATMController()
	atm.run()


if __name__ == '__main__':
	main()

