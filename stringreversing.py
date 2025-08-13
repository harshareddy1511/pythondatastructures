#python program to reverse a string
a = "The Sky is Blue"
words = a.split()
reverse = words[::-1]
result = " ".join(reverse)
print(result)
