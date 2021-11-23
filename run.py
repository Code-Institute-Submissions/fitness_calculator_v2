weight_units = None
height_units = None

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


def get_value(answer, low, high):
    while True:
        input_str = input(f"{answer}\n")
        input_int = int(input_str)
        if input_int in range(low, high):
            return input_int
        else:
            print(
                f"invalid answer. please respond with a integer in the range {low} to {high}")


def bmi_calculation_start():
    print("This BMI calculator will ask you a few simple questions and return your BMI and healthy weight range")

    age = get_value("what is your age?: ", 18, 140)

    if (height_units):
        height_in_ft = get_value(
            "(you will be asked to add inches in the next question) what is your height in ft?: ", 1, 9)
        height_in_inches = get_value(
            "add inches to your current height: ", 0, 12)
    else:
        height_in_cm = get_value(
            "what is your height in cm: ", 25, 275)

    if (weight_units):
        weight_in_lb = get_value(
            "what is your weight in lb?: ", 40, 600)
    else:
        weight_in_kg = get_value(
            "what is your weight in kg?: ", 25, 300)


def main():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no(
        "would you like to calculate your BMI and healthy weight range?")
    calorie_bool = yes_no("would you like to calculate your calories?")
    macro_bool = yes_no("would you like to calculate your macros?")

    weight_units = a_or_b("would you like to use lb or kg for weight measurements?", [
                          "lb", "l"], ["kg", "k"])
    height_units = a_or_b("would you like to use ft or cm for height measurements?", [
                          "ft", "f"], ["cm", "c"])

    # if (bmi_bool):
    #     bmi_calculation_start()
    # elif (calorie_bool):
    #     calorie_calculation_start()
    # elif (macro_bool):
    #     macro_calculation_start()
    # else:
    #     end_program()


main()
