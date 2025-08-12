#python program to dind duplicates in an array
numbers = [1,3,4,2,2]
emps = set()
duplicate = -1
for num in numbers:
    if num in emps:
        duplicate = num
        break
    emps.add(num)

print(duplicate)
