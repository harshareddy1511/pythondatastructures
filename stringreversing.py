#python program to reverse a string
a = "The Sky is Blue"
words = a.split() #splitting the words in the sentence
reverse = words[::-1] #reversing the  words in the sentence
result = " ".join(reverse) #joining the reversed words again
print(result) #printing the result
