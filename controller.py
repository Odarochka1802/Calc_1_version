import model_sum as model
import view
from fractions import Fraction


def button_click():
    number_type = input("1. Fraction  2. Complex: ")
    value_a = view.get_value(number_type)
    value_b = view.get_value(number_type)
    model.init(value_a,value_b)
    result = model.do_it()
    view.view_data(result,value_b,number_type)

    with open('file.txt','a') as f:
        if value_b==float(0) and result[1]=="/":
            f.write(f'Division by zero is not possible for "{value_a}" and "{value_b}"\n')
        else:
            f.write(f"{value_a} {result[1]} {value_b} = {result[0].numerator//result[0].denominator} {result[0].numerator%result[0].denominator}/{result[0].denominator}\n")
