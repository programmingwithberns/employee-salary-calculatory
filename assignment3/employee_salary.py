# Simple program to calculate employee salary
"""
Problem statement
The management of Longho Investing Ltd is paying its employees on an hourly basis. 
The base hourly wage is 2000 FCFA.  The normal working hours at Longho Investing 
is 40 hours per week. For any additional hour that the employee works, they get 
a bonus of 100 FCFA. An employee can work for a maximum of 50 hours a week and 
must work for at least one hour every week. 

Task
The management of Longho Investing Ltd has contacted you to help them automate 
the calculation of the salaries for their employees. Write a program to help the 
management of Longho Investing Ltd calculate an employee’s weekly salary.

There are 10 employees working for Longho Investing Ltd and the management wants
to print the total money that they pay the employees per week (i.e the sum of the
 weekly payments). 
Also present the average salary per employee. 

"""

# input
hourly_wage = 2000

normal_work_hours = 40

max_working_hours = 50

min_working_hours = 1

bonus_per_extra_hour = 100

hours_worked = 0

max_employees = 10

count = 1

salary_sum = 0

while(count <= max_employees):
    # getting input from the user
    user_input = input(f"\nPlease enter the hours worked for employee #{count}: ")

    try:
        hours_worked = float(user_input)
        weekly_salary = hourly_wage * hours_worked

        if hours_worked < min_working_hours or hours_worked > max_working_hours:
            print(f"Weekly hours must be between {min_working_hours} and {max_working_hours}.")
        else:
            if hours_worked <= normal_work_hours:
                print(f"Your weekly salary for {hours_worked} hours is {weekly_salary} FCFA.")
                print(f"You did not have any bonus this week.")

                # Add this salary to the sum
                salary_sum += weekly_salary
                
            if hours_worked > normal_work_hours:
                bonus_hours = hours_worked - normal_work_hours
                bonus_wage = bonus_hours * bonus_per_extra_hour
                gross_salay_with_bonus = weekly_salary + bonus_wage
                print(f"Your weekly salary for {hours_worked} hours is {gross_salay_with_bonus} FCFA.")
                print(f"You had a bonus of {bonus_wage} FCFA for the {bonus_hours} worked.")

                # Add this salary to the sum
                salary_sum += gross_salay_with_bonus

            # increment the count
            count += 1
    except Exception as ve:
        print(f"ERROR occured [{ve}]")

# Calculate the average 
average_salaries = salary_sum / max_employees

print(f"\nThe total salary paid for all {max_employees} employees is {salary_sum} FCFA with an average of {average_salaries} FCFA.")
