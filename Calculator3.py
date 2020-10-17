a=float(input("Enter the fist number:"))
op=input"Enter the operation"
b=float(input("Enter the second number:"))
if op=="+":
result=a+b
elif op=="/":
result=a/b
elif op=="-":
result=a-b
elif op=="*":
result=a*b
elif op=="pow":
result=pow(a,b)
if not result:
  print("invalid input")
print("Result{:.2f}".format(result))
