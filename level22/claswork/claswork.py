my_list=['ვაშლი', 'მსხალი', 'ატამი', 24, 56]
print(len(my_list))

my_list.append('apple')
my_list.insert(2, 'banana')
my_list.pop(0)
print(my_list)


students = ["გიორგი", "ანა", "ლუკა", "მარიამი"]


print(students)
students.append("დავითი")
students.append("ნინო")
students.insert(0, "ზაირა მასწავლებელი")
students.insert(3, "ნიკოლოზი")
print(students)



data = [15, 40.2, 15, 5, 7, 10, 23, 15]
print("თავდაპირველი სია:", data)
count_15 = data.count(15)

print("რიცხვი 15 მეორდება:", count_15, "-ჯერ")
data.sort()

print("ზრდადობით:", data)
data.sort(reverse=True)

print("კლებადობით:", data)
print("უკუღმა ამოტრიალებული:", data[::-1])  
