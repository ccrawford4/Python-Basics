# Calum Crawford, Section 5
def main(): # Main Function
	print('Welcome to the Payroll Manager!') #Introduces User to the Program
	print('-'*90) #Prints first dotted line
	employee_names = ['Michael', 'Mary', 'Nicole', 'Robert', 'Suzanne'] #Creates list with different names 
	hours_workeds = [38.00, 45.50, 51.20, 42.00, 38.00] # Creates list with different float values for number of hours worked
	pay_rates = [18.34, 15.88, 22.45, 21.34, 19.21] # Creates list with different float values for pay rates in dollars per hour
	sum_regular_salary = 0 # Initializes the sum of the regular salary with 0
	sum_overtime_salary = 0 # Initializes the sum of the overtime salary with 0
	for i in range(len(employee_names)): # Creates a for loop to iterate through lists
		employee_name = employee_names[i]
		hours_worked = hours_workeds[i]
		pay_rate = pay_rates[i]
		x = fPayroll(employee_name, hours_worked, pay_rate) # Calls fPayroll function with appropriate name, hours worked, and pay rate
		sum_regular_salary = x[0] + sum_regular_salary # Adds the value of regular salary returned by the fPayroll function to the value of the sum regular salary
		sum_overtime_salary = x[1] + sum_overtime_salary # Adds the value of the overtime salary returned by the fPayroll function ot the value of the sum overtime salary
	print('-'*90) # Prints the second dotted line
	print(f'Sum Regular Pay: ${sum_regular_salary:.2f}') # Prints the sum regular pay
	print(f'Sum Overtime Pay: ${sum_overtime_salary:.2f}') # Prints the sum overtime pay



def fPayroll(employee_name, hours_worked, pay_rate): # Intializes function fPayroll with parameters employee_name, hours_worked, and pay_rate which are appropriate elements within the lists created in main() function
	regular_salary = 0 # Initializes regular salary with 0
	overtime_salary = 0 #Initializes overtime_salary with 0
	if hours_worked <= 40: # If the number of hours worked is less than or equal to 40, then program enters if statment 
		salary = pay_rate * hours_worked #Salary is equal to the pay per hours times the number of hours worked
		regular_salary = (pay_rate * hours_worked) + regular_salary # Regular salary is modified to match salary value
		overtime_salary = overtime_salary + 0 # Overtime salary is still 0
	else: # If number of hours worked is greater than 0, enters else statment 
		overtime_hours = hours_worked - 40 # Overtime hours is the number of hours after 40
		salary = (pay_rate * 40) + ((pay_rate*1.5) * overtime_hours) # Salary is computed by the pay rate * 40 hours, plus the new pay rate for overtime * the number of overtime hours worked
		overtime_salary = (((pay_rate * 1.5)) * overtime_hours) + overtime_salary # Overtime salary is computed by the number of overtime hours * the product of the pay_rate * 1.5
		regular_salary = (pay_rate * 40) + regular_salary # Regular salary is computed by the pay_rate * 40 plus the regular_salary
	if len(employee_name) <= 4: # If the employees name is less than 4 characters, add an extra tab for spacing purposes
		print(f'Employee: {employee_name}\t\tHours worked: {hours_worked:.2f}\tPay per hour: ${pay_rate:.2f}\tSalary: ${salary:.2f}')
	else: # Otherwise print just one tab between employee name and hours worked
		print(f'Employee: {employee_name}\tHours worked: {hours_worked:.2f}\tPay per hour: ${pay_rate:.2f}\tSalary: ${salary:.2f}')

	return regular_salary, overtime_salary # Returns regular_salary and overtime_salary

main() # Calls main function


