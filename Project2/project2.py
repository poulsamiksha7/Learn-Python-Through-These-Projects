def get_number(number):

    while True:
        operand= input(f"Number :"+ str(number)+": ")
        try:
            return float(operand)
        except:
            print("Invalid Number, try again")


operand=get_number(1)
operand2=get_number(2)
sign=input("Sign: ")

result=0
if sign=="+":
    result= operand+operand2
elif sign=="-":
    result= operand-operand2
elif sign=="/":
    if float(operand2)!=0:
        result= operand/operand2
    else:
        print("Division by 0")
elif sign=="*":
    result= operand*operand2
else:
    print("Invalid Sign")

print(result)

