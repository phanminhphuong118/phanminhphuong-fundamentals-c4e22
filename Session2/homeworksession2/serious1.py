height=int(input("how tall are you(cm)"))
h=height/100
w=int(input("what is your weight(kg)"))
BMI=w/(h*h)
if BMI < 16:
    print("Severely underweight")
elif BMI <18.5:
    print("Underweight")
elif BMI <25:
    print("Normal")
elif BMI <30:
    print("Overweight")
else :
    print("Obese")