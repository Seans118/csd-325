# Sean Summers 11/12/2025 Assignment 10.2
# This program will demonstrate inheritance between 2 classes

# The employee superclass
class Employee:
	def __init__(self, name, gender, hourly_rate, emp_number):
		self.__name = name
		self.__gender = gender
		self.__hourly_rate = hourly_rate
		self.__emp_number = emp_number

	# The following methods are mutators for the class's attributes

	def set_name(self, name):
		self.__name = name

	def set_gender(self, gender):
		self.__gender = gender

	def set_hourly_rate(self, hourly_rate):
		self.__hourly_rate = hourly_rate

	def set_emp_number(self, emp_number):
		self.__emp_number = emp_number

	# The following methods are the accessors for the 
	# class's data attributes

	def get_name(self):
		return self.__name

	def get_gender(self):
		return self.__gender

	def get_hourly_rate(self):
		return self.__hourly_rate

	def get_emp_number(self):
		return self.__emp_number

# A method to print the attributes to save time rewriting code
	def print_details(self):
		print('Name:', self.get_name())
		print('Gender:', self.get_gender())
		print('Hourly Rate:', self.get_hourly_rate())
		print('Employee Number:', self.get_emp_number())

# The Production Worker class that inherits from the employee class
class Production_Worker(Employee):
	def __init__(self, name, gender, hourly_rate, emp_number, shift):
		# Use the superclass init method to inherit attributes
		Employee.__init__(self, name, gender, hourly_rate, emp_number)
		self.__shift = shift

	# setter and getter methods
	def set_shift(self, shift):
		self.__shift = shift

	def get_shift(self):
		return self.__shift
# Overriding the original print method to add the new attribute
	def print_details(self):
		print('Name:', self.get_name())
		print('Gender:', self.get_gender())
		print('Hourly Rate:', self.get_hourly_rate())
		print('Employee Number:', self.get_emp_number())
		print('Shift:', self.get_shift())

# The main function
def main():
	employee1 = Employee('Sean Summers', 'Male', 20.50, 1)
	employee2 = Employee('Alex Zwolinksi', 'Male', 19.10, 2)

	prodwork1 = Production_Worker('Marcus Shepherd', 'Male', 22.75, 3, 'Graveyard')
	prodwork2 = Production_Worker('Angelique Summers', 'Female', 18.50, 4, 'Day')
	prodwork3 = Production_Worker('Kelley Borgmann', 'Female', 20.75, 7, 'Morning')

	List_Employees = [employee1, employee2, prodwork1, prodwork2, prodwork3]

	print('The following is a list of employees:\n')

	for emp in List_Employees:
		emp.print_details()
		print('\n')


if __name__ == '__main__':
	main()