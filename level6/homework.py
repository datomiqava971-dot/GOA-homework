# 2) კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

# 3) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.

# 4) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

# 5) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

# 6) მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.

# 7) მომხმარებელს შემოატანინეთ 5 რიცხვი სხვადასხვა დამოუკიდებელი input-ების სახით, თქვენი დავალებაა დაბეჭდოთ მათი საშუალო არითმეტიკული.

# 8) მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.

#input არის მოწყობილობები რომლებსაც ვიყენებტ რაიმე სიგნალის გასაგზავნად, მაგალითად კლავიატურის ღილაკზე დაკლიკება. output კი არის ისეთი მოწყობილებები რომლებიც გამოსახავს მიღებულ სიგნალს, მაგალითად მონიტორზე გამოისახება კლავიატურიდან მიღებული სიგნალი.

index = input()
print(type(index))

#string
city = 'tbilisi'
country = 'georgia'
car_brand = 'kia'
actor = 'Dwayne Johnson'
chanel = 'GDS'

# integer
age = 43
year = 2026
weight = 55
quantity = 8
cost = 17

#float
height = 1.72
temperature = 98.6
pi = 3.14159
price = 19.99
gravity = 9.81


chanel = 'ბასტი-ბუბუ'
temperature = 98.6
weight = 55
print(type(chanel))
print(type(weight))
print(type(temperature))


name = input('your name: ')
age = input('your age: ')
height = input('your height: ')
print(name + ', ' + age + ', ' + height + '.')


num1 = int(input('enter any numer: '))
num2 = int(input('enter any numer: '))
num3 = int(input('enter any numer: '))
num4 = int(input('enter any numer: '))
num5 = int(input('enter any numer: '))
print((num1 + num2 + num3 + num4 + num5) // 5)


name = input('შემოიყვანეთ თქვენი სახელი: ')
last_name = input('შემოიყვანეთ თქვენი გვარი: ')
age = input('შემოიყვანეთ თქვენი ასაკი: ')
height = input('შემოიყვანეთ თქვენი სიმაღლე: ')
weight = input('შემოიყვანეთ თქვენი წონა: ')
print('my name is ' + name + ' and last name is ' + last_name + '. i am ' + age + ' years old. my height is ' + height + ' and i am ' + weight + ' kilo.')