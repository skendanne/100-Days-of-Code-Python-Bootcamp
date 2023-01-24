def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Exercise:

# In the starting code you'll find the solution from the leap Year challenge.
# First, convert this functions is_leap() so that instead of printing
# "Leap year." or "Not leap year." it should return True if it is a
# leap year and return False if it is not a leap year.

# You are going to create a function called days_in_month() which will
# take a year and a month as inputs.

# And it will use this information to work out tue number of days in the
# month, then return thas as the output

# The list month_days contains the number of days in a month from January
# to December for a non-leap year. A leap year has 29 days in February

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29
 
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)