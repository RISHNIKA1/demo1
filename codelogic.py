def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cant divided by Zero"


print(divide(6,2))