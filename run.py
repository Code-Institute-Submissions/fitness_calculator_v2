
# Function for a 2 option selection
def a_or_b(answer, a, b):
    while True:
        choice = input(f"{answer} {a[0]}/{b[0]}: \n").lower()
        if choice in a:
            return True
        elif choice in b:
            return False
        else:
            print(f"Please respond with {a[0]} or {b[0]}\n")


def yes_no(answer):
    yes = ['yes', 'y', 'ye']
    no = ['no', 'n']
    return a_or_b(answer, yes, no)


def get_value(answer, x, y):
    while True:
        try:
            value_answer = int(input(answer) in range(x, y))
            return value_answer
        except ValueError:
            print("incorrect input. please try again")


# def bmi_calculation_start():


def main():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no(
        "would you like to calculate your BMI and healthy weight range?")
    calorie_bool = yes_no("would you like to calculate your calories?")
    macro_bool = yes_no("would you like to calculate your macros?")

    # if bmi_bool and calorie_bool and macro_bool is False:
    #     # end_program()

    weight_units = a_or_b("would you like to use lb or kg for weight measurements?", [
                          "lb", "l"], ["kg", "k"])
    height_units = a_or_b("would you like to use lb or kg for height measurements?", [
                          "ft", "f"], ["cm", "c"])


main()
