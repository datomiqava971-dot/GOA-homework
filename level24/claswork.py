def greet(name):
    print("Hello World!")
    print(f"Hello {name}")

greet("გიორგი")



def double(number):
    return number * number

print(double(5))



def checkOdd(number):
    if number % 2 == 0:
       print("ლუწი")
    else:
       print("კენტი")



def BMI(height, weight):
    return weight / (height * height)

print(BMI)




def getNameByUpper(username):
    return username.upper()

user_input = input("შეიყვანეთ თქვენი სახელი: ")
upper_name = getNameByUpper(user_input)

print(upper_name)
