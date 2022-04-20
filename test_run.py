# import unittest
# from run import a_or_b


# class TestOptionQuestions(unittest.TestCase):
#     def test_a_or_b_is_true(self):
#         print("test_a_or_b_is_true")
#         A = ["a", "b", "c"]
#         B = ["x", "y", "z"]
#         self.assertTrue(a_or_b("", A, B))

#     def test_a_or_b_is_false(self):
#         print("test_a_or_b_is_false")
#         A = ["a", "b", "c"]
#         B = ["x", "y", "z"]
#         c
#         self.assertFalse(a_or_b("", A, B))

#     if __name__ == "__main__":
#         unittest.main()


def calculate_bmi(weight, height):
    """
    calculates the users bmi from the height and weight values.
    based on the range of the bmi value returns the category
    and value to the user.
    """

    bmi = (weight / height / height) * 10000
    bmi = round(bmi, 1)

    if bmi <= 16:
        bmi_msg = f"Your bmi is {bmi}. this is considered very underweight\n"

    elif bmi <= 18.5:
        bmi_msg = f"Your bmi is {bmi}. this is considered underweight\n"

    elif bmi <= 25:
        bmi_msg = f"Your bmi is {bmi}. this is considered Healthy\n"

    elif bmi <= 30:
        bmi_msg = f"Your bmi is {bmi}. this is considered overweight\n"

    else:
        bmi_msg = f"Your bmi is {bmi}. this is considered very overweight\n"

    print(f"\n{bmi_msg}")

    return bmi_msg


answer = calculate_bmi(52, 167)
print(answer)
