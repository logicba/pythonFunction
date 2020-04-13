# buil function without return
def hello(name):
    print("Hello %s" %name)


# hello("ddd")

# build function with return value
def areas(width, height):
    return width*height


# print(areas(10, 30))

def area_circle(pir = 10):
    return pir**2


# print(area_circle(2))

def showinfor(name, salary=0.00, lang="not define"):
    print("Name : ", name)
    print("Salary : ", salary)
    print("Language : ", lang)


showinfor("bank")