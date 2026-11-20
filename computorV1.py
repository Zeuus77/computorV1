import sys

def abss(x):
    if x < 0:
        return -x
    else:
        return x
    

def parsing(side):
    terms = {}
    side = side.replace(" ", "")

    if side == "0":
        return terms

    current = ""
    sign = 1

    for char in side:
        if char == "+" or char == "-":
            if current:
                coefficient, power = current.split("*X^")
                coefficient = float(coefficient)
                power = int(power)

                terms[power] = terms.get(power, 0) + sign * coefficient

            current = ""
            sign = 1 if char == "+" else -1

        else:
            current += char

    if current:
        coefficient, power = current.split("*X^")
        coefficient = float(coefficient)
        power = int(power)

        terms[power] = terms.get(power, 0) + sign * coefficient

    return terms


def print_reduced_form(terms):
    print("Reduced form: ", end="")
    if not terms or all(value == 0 for value in terms.values()):
        print("0 * X^0 = 0")
        return

    powers = sorted(terms.keys())
    first = True

    for power in powers:
        coefficient = terms[power]

        if first:
            print(f"{coefficient:g} * X^{power}", end="")
            first = False
        elif coefficient >= 0:
            print(f" + {coefficient:g} * X^{power}", end="")
        else:
            print(f" - {abss(coefficient):g} * X^{power}", end="")

    print(" = 0")
    
    
def parse_equation(equation):
    sides = equation.split("=")

    if len(sides) != 2:
        raise ValueError("Invalid equation")

    left = parsing(sides[0])
    right = parsing(sides[1])

    terms = {}

    for power in left:
        terms[power] = left[power]

    for power in right:
        terms[power] = terms.get(power, 0) - right[power]

    return terms


def degree_and_solution(terms):
    degree = 0
    for power in terms:
        mo3amile = terms[power]
        if mo3amile != 0 and power > degree:
            degree = power
    print(f"Polynomial degree: {degree}")

    if degree == -1:
        print("No solution")
        return
    if degree == 0:
        if terms.get(0,0) == 0:
            print("Any real number is a solution.")
            return
    elif degree == 1:
        b = terms.get(1,0)
        c = terms.get(0,0)
        res = -c /b
        print(f"The solution is:\n{res}")
    elif degree == 2:
        a = terms.get(2,0)
        b = terms.get(1,0)
        c = terms.get(0,0)
        delta = (b*b) - (4*a*c)
        if delta > 0:
            res1 = (-b + delta**0.5) / (2*a)
            res2 = (-b - delta**0.5) / (2*a)
            print(f"The discriminant is strictly positive, the two solutions are:\n{res1}\n{res2}")
        elif delta == 0:
            res = -b / (2*a)
            print(f"The discriminant is zero, the solution is:\n{res}")
        elif delta < 0:
            res1 = (-b + (abss(delta)**0.5) * 1j) / (2*a)
            res2 = (-b - (abss(delta)**0.5) * 1j) / (2*a)
            print(f"The discriminant is strictly negative, the two complex solutions are:\n{res1}\n{res2}")
    elif degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")

def main():
    if len(sys.argv) != 2:
        print("error : they are more or less argv")
        return
    
    equation = sys.argv[1]
    try:
        terms = parse_equation(equation)
        print_reduced_form(terms)
        degree_and_solution(terms)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
