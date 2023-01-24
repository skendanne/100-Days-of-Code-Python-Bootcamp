# Functions

# def my_function():
#     do this
#     then do this
#     finally do this

# my_function()

# Functions with inputs

# def my_function(something):
#     do this with something
#     then do this
#     finally do this

# my_function(123)

# Functions with outputs

# def my_function(something):
#     result = 3 * 2
#     return result

# output = my_function()

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("matheus", "FaRnEtAnI"))