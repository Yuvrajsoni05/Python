students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([score, name])

students.sort()
studentsCopy = []
for i in range(len(students)):
    studentsCopy.append(students[i][0])

arr = list(dict.fromkeys(studentsCopy))

for i in range(len(students)):
    if students[i][0] == arr[1]:
        print(students[i][1])