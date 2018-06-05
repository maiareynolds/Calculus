#Finding the slope, tangent line and normal line of y=x^2 at x=-2:
x=-2
y=x**2
x1=x+.0000000000001
x2=x-.0000000000001
y1=x1**2
y2=x2**2
m=((y1)-(y2))//(2*.0000000000001)
t=m*(0-x)+y
n=(-1/m)*(0-x)+y
print("Slope =",m)
print("Tangent equation is y=",m,"(x)+",t)
print("Normal equation is y=",(-1/m),"(x)+",n)