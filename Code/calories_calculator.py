def bmi(weight, height):
    bmi = float(f"{weight / height ** 2 * 10000:.1f}")
    under_or_overweight = ""
    if bmi < 18.5:
        under_or_overweight = "underweight"
    elif 18.5 <= bmi <= 24.9:
        under_or_overweight = "normal"
    else:
        under_or_overweight = "overweight"
    return f"Your BMI is {bmi} which is considered {under_or_overweight}"


def suggested_weight(height, gender):
    male = height - 100
    female = height - 110
    if gender == "male":
        return f"Suggested weight is around {male} kg"
    else:
        return f"Suggested weight is around {female} kg"


weight = int(input("Weight in kilograms: "))
height = int(input("Height in centimeters: "))
gender = input("Gender: ")

print(bmi(weight, height))
print(suggested_weight(height, gender))
