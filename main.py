def Factorial(a):
  b=1
  for i in range(1,(a+1)):
    b*=i
  return(b)
print(Factorial(2))