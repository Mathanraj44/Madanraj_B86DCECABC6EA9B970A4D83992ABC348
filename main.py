

def fact_rec(n):
  if n==0:
    return 1
  else:
    return n*fact_rec(n-1)
    
number=int(input("enter the value"))
res=fact_rec(number)

print("the factorial of {}.".format(number,res))