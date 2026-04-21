# True
print(10 > 5)
print(7 == 7)
print(5 != 3)
print(10 > 2 and 5 < 8)
print(10 > 20 or 5 == 5)

# False
print(10 < 5)
print(8 == 8)
print(15 <= 10)
print(True and False)
print(False and False)

# Sequencing არის კოდის ინსტრუქციების ზემოდან ქვემოთ, ზუსტად იმ თანმიმდევრობით შესრულება, როგორც წერია.
# Iteration არის პროცესის განმეორება.
# Selection არის გადაწყვეტილების მიღება კოდში. 

name = "ნიკა"
age = 25
print(name + " არის " + str(age) + " წლის.")


# for loop არის ციკლი, რომელიც გვეხმარება მრავალხაზიანი კოდის 2 ხაზში დაწერაში


# range() ფუნქციას გადაეცემა მნიშვნელობები range(start, stop, step) და fro loop ქმნის ციკლს ამ მონაცემებით.

for i in range(1, 5):
  print('GTR R34')

for i in range(1, 101):
  print('მიქავა')

for i in range(1, 47):
  print('blue')

for i in range(1, 33):
  print('D')

name=input('შემოიყვანეთ თქვენი სახელი: ')
last_name=input('შემოიყვანეთ თქვენი გვარი: ')
nickname=input('შემოიყვანეთ თქვენი მეტსახელი: ')
age=int(input('შემოიყვანეთ თქვენი ასაკი: '))
print(name+last_name+nickname+str(age))

word='tree'
num1=12
num2=2.7
answer=True
print(type(word))
print(type(num1))
print(type(num2))
print(type(answer))

num1=int(input('ჩაიფიქრე რიცხვი: '))
num2=int(input('ჩაიფიქრე რიცხვი: '))
num3=int(input('ჩაიფიქრე რიცხვი: '))
num4=int(input('ჩაიფიქრე რიცხვი: '))
print(num1+num2+num3+num4)