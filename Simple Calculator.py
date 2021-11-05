n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("""Please select from the following:
1. Divide
2. Multiply
3. Add
4. Substract""")
print("\n")

select = int(input("Enter the option number: "))

if select == 1:
	print("=", n1/n2)
elif select == 2:
	print("=", n1*n2)
elif select == 3:
	print("=", n1+n2)
elif select == 4:
	print("=", n1-n2)