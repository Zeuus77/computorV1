import sys

def abss(x):
    if x < 0:
        return -x
    else:
        return x

def degree_and_solution(terms):
    degree = 0
    for power in terms:
        coefficient = terms[power]
        if coefficient != 0 and power > degree:
            degree = power
    print(f"Polynomial degree: {degree}")

    if degree == -1:
        print("Any real number is a solution.")
        return
    if degree == 0:
        if terms.get(0,0) == 0:
            print("No solution")
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
        delta = b*b - 4*a*c
        if delta > 0:
            res1 = (-b + delta**0.5 ) / (2*a)
            res2 = (-b - delta**0.5) / (2*a)
            print(f"The discriminant is strictly positive, the two solutions are:\n{res1}\n{res2}")
        elif delta == 0:
            res = -b / (2*a)
            print(f"The discriminant is zero, the solution is:\n{res}")
        elif delta < 0:
            res1 = (-b + (abss(delta)**0.5) * 1j) / (2*a)
            res2 = (-b + (abss(delta)**0.5) * 1j) / (2*a)
            print(f"The discriminant is strictly negative, the two complex solutions are:\n{res1}\n{res2}")
    elif degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")

def main():
    if len(sys.argv) != 2:
        print("error : they are more or less argv")
        return
    
    equation = sys.argv[1]

    terms = {
        0: 1,
        1: 5,
        2: 2
    }

    degree_and_solution(terms)


if __name__ == "__main__":
    main()
