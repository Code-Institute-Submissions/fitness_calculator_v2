# temporary global functions
bmi_bool = None
calorie_bool = None
macro_bool = None
weight_units = None
height_units = None
bmi = None

def a_or_b(answer, a, b):
    """
    gets option a or b from user.
    checks to see if the input is in the list of acceptable answers for either option.
    returns True or False if option a or b is picked.
    """

    while True:
        choice = input(f"\n{answer} {a[0]} / {b[0]}: \n").lower()

        if choice in a:
            return True

        elif choice in b:
            return False

        else:
            print(f"\nPlease respond with {a[0]} or {b[0]}\n")

def yes_no(answer):
    """
    function to get a yes or no answer from the user.
    defines the acceptable values for yes and no and calls a_or_b using them.
    """
    yes = ['yes', 'y', 'ye']
    no = ['no', 'n']

    return a_or_b(answer, yes, no)

def get_int_value(answer, low, high):
    """
    gets an int value input from the user within a defined low and high range.
    """

    while True:

        try:
            input_int = int(input(f"\n{answer}\n"))

            if input_int in range(low, high + 1):

                return input_int

            else:

                return ValueError

        except ValueError:
            print(
                f"\ninvalid answer. please respond with a integer in the range {low} to {high}")

def get_float_value(answer, low, high):
    """
    gets a float value input from the user within a defined low and high range.
    """

    while True:

        try:
            input_float = float(input(f"\n{answer}\n"))
            float_to_int = int(input_float * 10)

            if float_to_int in range(low * 10, high * 10 + 1):

                return input_float

            else:

                return ValueError

        except ValueError:
            print(
                f"\ninvalid answer. please respond with a integer in the range {low} to {high}")


# opening questions function to deter
def opener():
    print("Welcome to fitness_calculator v3. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")
    global bmi_bool
    global calorie_bool
    global macro_bool
    global weight_units
    global height_units
    bmi_bool = yes_no(
        "would you like to calculate your bmi and healthy weight range?")
    calorie_bool = yes_no("would you like to calculate your calories?")
    macro_bool = yes_no("would you like to calculate your macros?")

    weight_units = a_or_b("would you like to use lb or kg for weight measurements?", [
                          "lb", "l"], ["kg", "k"])
    height_units = a_or_b("would you like to use ft or cm for height measurements?", [
                          "ft", "f"], ["cm", "c"])


def bmi_calculation_start():
    print("This bmi calculator will ask you a few simple questions and return your bmi and healthy weight range\n")
    global height_in_cm
    global weight_in_kg

    if (height_units):
        height_in_ft = get_int_value(
            "(you will be asked to add inches in the next question) what is your height in ft?: ", 1, 9)
        height_in_ft_add_inches = get_int_value(
            "add inches to your current height: ", 0, 12)
        height_in_cm = ((height_in_ft * 12) + height_in_ft_add_inches) * 2.54
    else:
        height_in_cm = get_int_value(
            "what is your height in cm: ", 25, 275)

    if (weight_units):
        weight_in_lb = get_int_value(
            "what is your weight in lb?: ", 40, 600)
    else:
        weight_in_kg = get_int_value(
            "what is your weight in kg?: ", 25, 300)

    weight_in_kg = float(weight_in_lb * 0.45359237)
    global bmi
    bmi = (weight_in_kg / height_in_cm / height_in_cm) * 10000
    bmi = round(bmi, 1)

    print("""this bmi value is not to be taken as an exact science and is only an approxmation of your healthy weight range.
    if you are concerned about the value you receive consult a medical professional for further steps.\n""")
    if(bmi <= 16):
        print(f"Your bmi is {bmi}. this is considered very underweight\n")
    elif(bmi <= 18.5):
        print(f"Your bmi is {bmi}.this is considered underweight\n")
    elif(bmi <= 25):
        print(f"Your bmi is {bmi}. this is considered Healthy\n")
    elif(bmi <= 30):
        print(f"Your bmi is {bmi}. this is considered overweight\n")
    else:
        print(f"Your bmi is {bmi}. this is considered very overweight\n")


def calorie_calculation_start():
    print("this calorie calculator will ask you a few simple questions and return your recomended daily calorie intake.\n")

    gender = a_or_b("are you male or female?", ["m", "male", "man", "ma", "mal"], [
                    "f", "female", "femal", "fema", "fem", "fe"])

    age = get_int_value("what is your age?: ", 18, 140)

    if gender:
        bmr = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5
    else:
        bmr = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161

    print(
        f"your BMR (basal metabolic rate) is {bmr}\n this is an approximation of how many calories your body burns without any additional energy expenditure apart from breathing.")

    print("""this table will demonstrate examples to help you pick an activity level multiplies to calculate your calories.\n
    LIFESTYLE & TRAINING FREQUENCY-----EXAMPLE-----ACTIVITY MULTIPLIER\n
    Sedentary + Training 3-6x/wk-----Works a desk jobvery little activity outside of lifting-----1.2 - 1.5\n
    Lightly Active + Training 3-6x/wk-----Works a desk job, takes pet for a walk most days in addition to lifting-----1.5 - 1.8\n
    Moderately Active + Training 3-6x/wk-----Works as a full-time waitress, occasionally plays tennis in addition tolifting-----1.8 - 2.0\n
    Highly Active + Training 3-6x/wk-----Works as a construction worker, regular hiking in addition to lifting-----2.0 - 2.2\n""")
    activity_level = get_float_value(
        "what is your estimated activity level multiplier?: ", 1, 2)
    maintance_calories = bmr * activity_level

    print(
        f"your calculated  daily calories to maintain your current weight is {round(maintance_calories)}")

    training_experience = get_int_value(
        """what is your level of training experience?
    1.Beginner(0-2 years)------ 2.Intermediate(2-4 years)-----3.Advanced(4+ years)
    pick 1,2 or 3: """, 1, 3)

    user_goal = get_int_value(
        """what is your primary goal?
    1.Lose Weight(Cut)-----2.Maintain current weight-----3.Gain Weight(Bulk)
    pick 1,2 or 3""", 1, 3)

    if user_goal == 1:
        change_cals_percentage = yes_no("""the default calorie deficit is 20% below maintance. We redomend this value for most
        people unless your are an experienced lifter with an already low body fat %. would you like to change this percentage?""")

        if change_cals_percentage:
            cals_percentage = get_int_value(
                "enter your preferred deficit %: ", 0, 75)
        else:
            cals_percentage = 20

    elif user_goal == 2:
        cals = maintance_calories
        print(
            f"to maintain your current weight you shoud use your maitaince calories which is {cals}")

    else:
        if training_experience == 1:
            change_cals_percentage = yes_no("""the recomended calorie surplus for your experience level is 25% to maximise muscle building potential
            in your early trainging career. would you like to change this percentage?"""

            if change_cals_percentage:
                cals_percentage=get_int_value(
                    "enter your preferred surplus %: ", 0, 75)
            else:
                cals_percentage=25

        if training_experience == 2:
            change_cals_percentage=yes_no("""the recomended calorie surplus for your experience level is 20% to maximise muscle building potential
            . would you like to change this percentage?"""
            if change_cals_percentage:
                cals_percentage=get_int_value(
                    "enter your preferred surplus %: ", 0, 75)
            else:
                cals_percentage=20

        else:
            change_cals_percentage=yes_no("""the recomended calorie surplus for your experience level is 15% to maximise muscle building potential
            . would you like to change this percentage?"""
            if change_cals_percentage:
                cals_percentage=get_int_value(
                    "enter your preferred surplus %: ", 0, 75)
            else:
                cals_percentage=15


    cal_multiplier=(cals_percentage / 100) + 1
    cals=maintance_calories * cal_multiplier
    print(f"your recomended daily calorie intake is {cals}")







def main():

    opener()
    bmi_calculation_start()
    calorie_calculation_start()

    # if bmi_bool and calorie_bool and macro_bool:
    #     bmi_calculation_start()
    #     calorie_calculation_start()
    #     macro_calculation_start()
    #     end_program()
    # elif bmi_bool and calorie_bool:
    #     pass
    # elif bmi_bool and macro_bool:
    #     pass
    # elif macro_bool
    #     pass
    # elif calorie_bool and macro_bool:
    #     pass
    # elif calorie_bool:
    #     pass
    # elif macro_bool:
    #     pass
    # else:


main()
