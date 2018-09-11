#1
students = [
   { 'name': 'Paul', 'age': 14 },
   { 'name': 'Mischa', 'age': 6 },
   { 'name': 'Hunor', 'age': 29 },
   { 'name': 'Indre', 'age': 21 },
   { 'name': 'Ragnar', 'age': 10 },
]

# Find how many are older than 18
count = 0


#2
# Given the following list, square the numbers
for i in students:
    if i['age'] <= 18:
        count+=1
print("#1")
print(count)


numbers = [4,5,3,4,2]

print("#2")
for i in numbers:
        print(i*i)

