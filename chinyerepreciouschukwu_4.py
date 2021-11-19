data = ("John", "Doe", 53.44)
format_string = "Hello"

#print(format_string % data)

#SOLUTION 
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
