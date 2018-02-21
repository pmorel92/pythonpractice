def add(a, b):
    print("ADDING {} + {}".format(a, b))
    return a + b

def subtract(a,b):
    print("SUBTRACTING {} - {}".format(a, b))
    return a - b

def multiply(a,b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

def divide(a,b):
    print("DIVIDING {0} / {1}".format(a, b))
    return a / b

print("Let's do some math wiht just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, height: {}, weight: {}, IQ: {}".format(age, height, weight, iq))

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
