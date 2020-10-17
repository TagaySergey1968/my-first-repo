a=int(input("Enter the fist number:"))
op=input"Enter the operation"
b=int(input("Enter the second number:"))
if op=="+":
result=a+b
elif op=="/":
result=a/b
elif op=="-":
result=a-b
elif op=="*":
result=a*b
print("Result{:.2f}".format(result))