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

# getting input from the user
user_input = input("Please enter the hours worked: ")

try:
    hours_worked = float(user_input)
    weekly_salary = hourly_wage * hours_worked

    if hours_worked < min_working_hours or hours_worked > max_working_hours:
        print(f"Weekly hours must be between {min_working_hours} and {max_working_hours}.")
    else:
        if hours_worked <= normal_work_hours:
            print(f"Your weekly salary for {hours_worked} hours is {weekly_salary} FCFA.")
            print(f"You did not have any bonus this week.")
        if hours_worked > normal_work_hours:
            bonus_hours = hours_worked - normal_work_hours
            bonus_wage = bonus_hours * bonus_per_extra_hour
            gross_salay_with_bonus = weekly_salary + bonus_wage
            print(f"Your weekly salary for {hours_worked} hours is {gross_salay_with_bonus} FCFA.")
            print(f"You had a bonus of {bonus_wage} FCFA for the {bonus_hours} worked.")
except Exception as ve:
    print(f"ERROR occured [{ve}]")
