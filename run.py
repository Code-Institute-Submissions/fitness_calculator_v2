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


def get_height_and_weight_value(height_units, weight_units):
    """
    gets height and weight value input from the user.
    uses the user defined height and weight units.
    returns values in a dict for clear access in other functions.
    """

    if (height_units):
        height_in_ft = get_int_value(
            "(you will be asked to add inches in the next question) what is your height in ft?: ", 1, 9)
        height_in_ft_add_inches = get_int_value(
            "add inches to your current height: ", 0, 12)
        height_in_cm = ((height_in_ft * 12) + height_in_ft_add_inches) * 2.54

    else:
        height_in_cm = get_int_value(
            "what is your height in cm?: ", 25, 275)

    if (weight_units):
        weight_in_lb = get_int_value(
            "what is your weight in lb?: ", 40, 600)
        weight_in_kg = float(weight_in_lb * 0.45359237)

    else:
        weight_in_kg = get_int_value(
            "what is your weight in kg?: ", 25, 300)

    global h_w
    h_w = [height_in_cm, weight_in_kg]

    return h_w


def get_gender():
    """
    gets a gender value from the user.
    """
    global gender
    gender = a_or_b("are you male or female?", ["m", "male", "man", "ma", "mal"], [
        "f", "female", "femal", "fema", "fem", "fe"])

    return gender


def get_age():
    """
    gets an age value from the user in a predefined range.
    """
    age = get_int_value("what is your age?: ", 18, 140)

    return age


def gap():
    """
    prints a line gap.
    """
    print('                                         ')
    print('-----------------------------------------')
    print('                                         ')



def opener():
    """
    opening statement and questions of the program.
    prints a welcome message and then asks which parts of the program the user would like to use.
    asks which height and weight units the user would like to input there values in.
    returns answer values in a dict.
    """
    gap()
    print("Welcome to fitness_calculator. this calculator can be used for bmi,calories,macros and fibre using industry standard calculations.\n")

    bmi_bool = yes_no(
        "would you like to calculate your bmi and healthy weight range?")
    calorie_bool = yes_no("would you like to calculate your calories?")
    macro_bool = yes_no("would you like to calculate your macros?")
    weight_units = a_or_b("would you like to use lb or kg for weight measurements?", [
        "lb", "l"], ["kg", "k"])
    height_units = a_or_b("would you like to use ft or cm for height measurements?", [
        "ft", "f"], ["cm", "c"])

    opening_answers_dict = {
        "bmi": bmi_bool,
        "calorie": calorie_bool,
        "macro": macro_bool,
        "h_w_units": [height_units, weight_units]
    }

    return opening_answers_dict


def calculate_bmi(weight, height):
    """
    calculates the users bmi from the height and weight values.
    based on the range of the bmi value returns the category and value to the user.
    """

    bmi = (weight / height / height) * 1000
    bmi = round(bmi, 1)

    if(bmi <= 16):
        bmi_msg = f"Your bmi is {bmi}. this is considered very underweight\n"

    elif(bmi <= 18.5):
        bmi_msg = f"Your bmi is {bmi}. this is considered underweight\n"

    elif(bmi <= 25):
        bmi_msg = f"Your bmi is {bmi}. this is considered Healthy\n"

    elif(bmi <= 30):
        bmi_msg = f"Your bmi is {bmi}. this is considered overweight\n"

    else:
        bmi_msg = f"Your bmi is {bmi}. this is considered very overweight\n"

    print(f"\n{bmi_msg}")

    return bmi_msg


def print_bmi_opener():
    """
    prints the opening statement of the bmi calculator.
    """
    gap()
    print("This bmi calculator will ask you a few simple questions and return your bmi and healthy weight range\n")
    print("""this bmi value is not to be taken as an exact science and is only an approxmation of your healthy weight range.
    if you are concerned about the value you receive consult a medical professional for further steps.\n""")


def calorie_calculation_start(height, weight, gender, age):
    """
    calorie calculation function.
    contains functions to calculate bmr,maintance calories, and surplus/deficit percentage.
    contains functions to get user activity level, user  goals and triaining experience.
    returns recommended calories from the last calorie calculation function which takes the user values from the prior functions.
    """

    def calculate_bmr(height, weight, gender, age):
        """
        takes user height, weight, gender and age and returns bmr.
        """
        if gender:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5

        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        gap()
        print(
            f"your BMR (basal metabolic rate) is {round(bmr)}\n this is an approximation of how many calories your body burns without any additional energy expenditure apart from breathing.")

        return bmr

    def get_activity_level():
        """
        prints an example table of values and
        gets the users activity levels.
        """
        gap()
        table = [["Sedentary + Training 3-6x/wk", "Works a desk job  very little activity outside of lifting", "1.2 - 1.5"],
                 ["Lightly Active + Training 3-6x/wk",
                     "Works a desk job, takes pet for a walk most days in addition to lifting", "1.5 - 1.8"],
                 ["Moderately Active + Training 3-6x/wk",
                     "Works as a full-time waitress, occasionally plays tennis in addition tolifting", "1.8 - 2.0"],
                 ["Highly Active + Training 3-6x/wk", "Works as a construction worker, regular hiking in addition to lifting", "2.0 - 2.2"]]

        print(tabulate(table, headers=[
              "LIFESTYLE & TRAINING FREQUENCY", "EXAMPLE", "ACTIVITY MULTIPLIER"]))

        activity_level = get_float_value(
            "what is your estimated activity level multiplier?: ", 1, 2)

        return activity_level

    def calculate_maintance(bmr, activity_level):
        """
        calculates the users maintance calories from  bmr and activity level.
        """

        maintance_calories = bmr * activity_level
        gap()
        print(
            f"your calculated  daily calories to maintain your current weight is {round(maintance_calories)}")

        return maintance_calories

    def get_training_experience():
        """"
        gets the users training experience in an int value.
        """
        gap()
        table = [["Beginner(0-2 years))", "1"],
                 ["Intermediate(2-4 years)", "2"], ["Advanced(4+ years)", "3"]]
        print(tabulate(table))
        training_experience = get_int_value(
            "what is your level of training experience?: ", 1, 3)

        return training_experience

    def get_user_goal():
        """
        gets the users goal (lose weight, gain weight or maintain) in an int value.
        """
        table = [["Lose Weight(Cut)", "1"], ["Maintain current weight", "2"], [
            "Gain Weight(Bulk)", "3"]]
        print(tabulate(table))
        user_goal = get_int_value("what is your goal?: ", 1, 3)

        return user_goal

    def deficit_percentage_calculation(maintance_calories):
        """
        calculates the percentage calorie deficit.
        ask the user if they want to use the suggested value or adjust it themselves.
        """
        change_cals_percentage = yes_no("""the default calorie deficit is 20% below maintance. We redomend this value for most
        people unless your are an experienced lifter with an already low body fat %. would you like to change this percentage?""")

        if change_cals_percentage:
            defecit = get_int_value(
                "enter your preferred deficit %: ", 0, 75)
        else:
            defecit = 20

        defecit_cals = maintance_calories * float(defecit) / 100

        return defecit_cals

    def surplus_percentage_calculation(training_experience, maintance_calories):
        """
        calculates the percentage calorie surplus.
        ask the user if they want to use the suggested value based on training experience
        or adjust it themselves.
        """
        if training_experience == 1:
            change_cals_percentage = yes_no("""the recomended calorie surplus for your experience level is 25% to maximise muscle building potential
            in your early trainging career. would you like to change this percentage?""")

            if change_cals_percentage:
                surplus = get_int_value(
                    "enter your preferred surplus %: ", 0, 75)
            else:
                surplus = 25

        if training_experience == 2:
            change_cals_percentage = yes_no("""the recomended calorie surplus for your experience level is 20% to maximise muscle building potential
            . would you like to change this percentage?""")

            if change_cals_percentage:
                surplus = get_int_value(
                    "enter your preferred surplus %: ", 0, 75)
            else:
                surplus = 20

        else:
            change_cals_percentage = yes_no("""the recomended calorie surplus for your experience level is 15% to maximise muscle building potential
            . would you like to change this percentage?""")

            if change_cals_percentage:
                surplus = get_int_value(
                    "enter your preferred surplus %: ", 0, 75)

            else:
                surplus = 15

        surplus_cals = maintance_calories * float(surplus) / 100

        return surplus_cals

    def calculate_cals(user_goal, maintance_calories, training_exp):
        """
        calculate recomended daily caloric intake.
        maintance calories + % surplus or deficit.
        """

        if user_goal == 1:
            defecit_calories = deficit_percentage_calculation(
                maintance_calories)
            calories = maintance_calories - defecit_calories

        elif user_goal == 2:

            calories = maintance_calories

        else:
            surplus_calories = surplus_percentage_calculation(
                training_exp, maintance_calories)
            calories = maintance_calories + surplus_calories

        return calories

    # chain of functions to get the final daily caloric intake value.
    bmr = calculate_bmr(height, weight, gender, age)

    activity_level = get_activity_level()

    maintance_calories = calculate_maintance(bmr, activity_level)

    user_goal = get_user_goal()

    training_exp = get_training_experience()

    global cals

    cals = calculate_cals(user_goal, maintance_calories, training_exp)

    user_cals_msg = f"your recomended daily caloric intake is {round(cals)}cal"

    gap()
    print(user_cals_msg)

    return user_cals_msg


def macro_calculation_start(gender, weight_in_kg):
    """
    calculates the values of daily intake for protein,carbs and fats using multiple functions to ask the user for values and calculate the % of the total diet each macro should be.
    """

    def get_bodyfat_percentage():
        """
        gets the user to input rough bodyfat percentage in int form.
        """
        print("""please enter your bodyfat percentage.
        this does not have to be exact and an estimation will do.
        """)

        bodyfat_percentage = get_int_value(
            "please enter your bodyfat percentage: ", 4, 60)

        return bodyfat_percentage

    def calculate_lbm(bf):
        """
        calculates lean body mass(lbm).
        using weight and bodyfat percentage
        """
        global h_w
        weight_lb = h_w[1] * 2.2046
        fatmass = weight_lb * (bf / 100)
        lbm = weight_lb - fatmass

        return lbm

    def calculate_protein(bf, lbm):
        """
        calculates daily protein intake.
        takes bf, lbm and gender and determines what protein percentage of total cals should be applied.
        """
        protein_multiplier = 1.6
        global gender
        if gender:

            if bf > 5:
                percent_above_5 = bf - 5

                for i in range(percent_above_5):
                    protein_multiplier -= 0.016

                    if protein_multiplier <= 1.2:
                        pass

        else:

            if bf < 8:
                percent_above_8 = bf - 8

                for i in range(percent_above_8):
                    protein_multiplier -= 0.0125

                    if protein_multiplier <= 1.2:
                        pass

        daily_protein = lbm * protein_multiplier

        return daily_protein

    def calculate_fat(bf):
        """
        calculates daily fat intake.
        takes bf and determines what fat percentage of total cals should be applied.
        """

        global gender
        global cals
        fat_percent = 20
        if gender:

            if bf > 5:
                percent_above_5 = bf - 5

                for i in range(percent_above_5):
                    fat_percent += 0.75

                    if fat_percent >= 35:
                        pass

        else:

            if bf > 10:
                percent_above_10 = bf - 10

                for i in range(percent_above_10):
                    fat_percent += 0.5

                    if fat_percent >= 35:
                        pass

        fat_multiplier = fat_percent / 100
        fats = (cals * fat_multiplier) / 9

        return fats

    def calculate_carbs(daily_protein, daily_fats):
        """
        calculates carbs by subtracting protein/fat cals from total cals 
        carbs is remainder
        """
        global cals
        remaining_cals = cals - ((daily_protein * 4) + (daily_fats * 9))
        daily_carbs = remaining_cals / 4

        return daily_carbs

    # chain of variables and functions to determine final macro values

    user_bf = get_bodyfat_percentage()

    lbm = calculate_lbm(user_bf)

    daily_protein = calculate_protein(user_bf, lbm)

    daily_fats = calculate_fat(user_bf)

    daily_carbs = calculate_carbs(daily_protein, daily_fats)

    macros = f"{round(daily_protein)}G protein {round(daily_fats)}G Fat {round(daily_carbs)}G Carbs"
    user_macro_msg = f"your daily macro intake is {macros}"
    gap()
    print(user_macro_msg)
    gap()

    return user_macro_msg


def main():


main()
