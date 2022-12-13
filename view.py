from fractions import Fraction
def view_data(result,b,number_type):
    if number_type=="1":
        if result[1]=="/" and b==float(0):
            print("Division by zero is not possible")
        else:
            if result[0].numerator>result[0].denominator:
                print(f"result = {result[0].numerator//result[0].denominator} {result[0].numerator%result[0].denominator}/{result[0].denominator}")
            else:
                print(f"result = {result[0]}")
    else:
                print(f"result = {result[0]}")
    


def get_value(number_type):
    if number_type=="1":
        return Fraction(input("value = "))
    elif number_type=="2":
        return complex(input("value = "))