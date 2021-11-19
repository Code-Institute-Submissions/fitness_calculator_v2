# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high




# Function for a Yes/No result based on the answer provided as an arguement
def a_or_b(answer,a,b):
    while True:
        choice = input(answer).lower()
        if choice in a:
           return True
        elif choice in b:
           return False
        else:
           print(f"Please respond with {a[0]} or '{b[0]}'\n")


def yes_no(answer):
    yes = set(['yes','y', 'ye'])
    no = set(['no','n'])
    return a_or_b(answer,yes,no)


     


def main():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no("would you like to calculate your BMI and healthy weight range? y/n: \n")
    calorie_bool = yes_no("would you like to calculate your calories? y/n: \n")
    macro_bool = yes_no("would you like to calculate your macros? y/n: \n")

    if bmi_bool && calorie_bool && macro_bool = False:
        # end_program()

    units = a_or_b("would you like to use lb or kg for measurements? type lb or kg: \n","lb","kg" ) 



main()