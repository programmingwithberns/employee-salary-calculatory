# Simple program to calculate employee salary
"""
The management of Longho Investing Ltd is paying its employees on an hourly basis. The base hourly
wage is 2000 FCFA. The normal working hours at Longho Investing is 40 hours per week. For any
additional hour that the employee works, they get a bonus of 100 FCFA. An employee can work for a
maximum of 50 hours a week and must work for at least one hour every week.
"""

# input
hourly_wage = 2000

normal_work_hours = 40

max_working_hours = 50

min_working_hours = 1 

bonus_per_extra_hour = 100

hours_worked = 0 

user_input = input("Please enter the hours worked: ")

hours_worked = float(user_input)

weekly_salary = hourly_wage * hours_worked 

print(f"Your weekly salary for {hours_worked} hours is {weekly_salary} FCFA.")

if hours_worked > normal_work_hours: 
    bonus_hours =  hours_worked - normal_work_hours
    bonus_wage = bonus_hours * bonus_per_extra_hour
    gross_salay_with_bonus = weekly_salary + bonus_wage
    print(f"You had a bonus of {bonus_wage} FCFA for the {bonus_hours} worked.")