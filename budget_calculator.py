income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

balance = income - expenses

print("Your remaining balance is:", balance)

if balance > 0:
    print("Good job! You are saving money.")
else:
    print("Warning: You are spending more than you earn.")