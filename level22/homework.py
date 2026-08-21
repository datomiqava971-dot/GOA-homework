# .append() — ამატებს ახალ ელემენტს სიის სულ ბოლოში
# .insert() — ამატებს ელემენტს სიის კონკრეტულ ინდექსზე
# .pop() — შლის ელემენტს სიიდან



fruits = ["apple", "banana", "cherry", "orange"]
print(len(fruits))



numbers = []

for i in range(5):
    user_num = int(input("შემოიტანეთ რიცხვი: "))
    numbers.append(user_num)
print(numbers)




colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)






animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey")
print(animals)





students = []

for i in range(3):
    name = input("შემოიყვანეთ სტუდენტის სახელი: ")
    students.append(name)
students.insert(0, "Teacher")

students.pop()
print(len(students))
print(students)