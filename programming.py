#Maia Reynolds
#Calculus Final

#Limit

#Derivative at a point
y=str(input("Enter an equation: y="))
x=str(input("Enter a x value: "))
x1=str(int(x)-.0000000000000000000000000000001)
x2=str(int(x)+.0000000000000000000000000000001)
y1=y.replace(x,x1)
y2=y.replace(x,x2)
derivative=((int(y2)-int(y1))/(int(x2)-int(x1)))
print(derivative)


#RAM

#Newton's Method

#Euler's

#Length of a Curve

#Taylor Polynomial

#Convergence/Divergence Tests