
# Function for a Yes/No result based on the answer provided as an arguement
def a_or_b(answer, a, b):
    while True:
        choice = input(answer).lower()
        if choice in a:
            return True
        elif choice in b:
            return False
        else:
            print(f"Please respond with {a[0]} or '{b[0]}'\n")


def yes_no(answer):
    yes = set(['yes', 'y', 'ye'])
    no = set(['no', 'n'])
    return a_or_b(answer, yes, no)

def get_value(answer, x, y):
    while True:
        try:
            value_answer = int(input(answer) in range(x, y))
            return value_answer
        except ValueError:
            print("incorrect input. please try again")
            


def bmi_calculation_start():
    

def main():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no("would you like to calculate your BMI and healthy weight range? y/n: \n")
    calorie_bool = yes_no("would you like to calculate your calories? y/n: \n")
    macro_bool = yes_no("would you like to calculate your macros? y/n: \n")

    if bmi_bool and calorie_bool and macro_bool is False:
        # end_program()

    units = a_or_b("would you like to use lb or kg for measurements? type lb or kg: \n", "lb", "kg")


main()
