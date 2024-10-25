def mul(a,b):
    try:
        return a//b
    except ZeroDivisionError:
        raise "Error: Denominator must not be zero!!"

a=int(input())
b=int(input())

result = mul(a,b)