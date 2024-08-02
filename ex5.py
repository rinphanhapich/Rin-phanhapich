user_input=int(input("Enter the number:"))
userMessage=" "
if user_input <=0:
    userMessage="Negative Number!"
else:
    userMessage="Positive Number"
print(userMessage)