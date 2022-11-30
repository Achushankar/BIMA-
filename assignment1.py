#Program for calculating different geometrical characteristics of a polygon shape

#Inputting information

n = int(input("Enter the number of Polygon points.."))
print("Enter the x and y coordinates of each of the polygon points..")

xs = []
ys = []

for i in range(0,n):
    x = float(input(f"x[{i+1}]: "))
    y = float(input(f"y[{i+1}]: "))
    xs.append(x)
    ys.append(y)

#Calculating Values
a=0
s1=0
s2=0
i1=0
i2=0
i3=0

for i in range(0,n):
    a = a + (xs[i] + xs[i-1]) * (ys[i] - ys[i-1]) 
    s1 = s1 + (xs[i]-xs[i-1]) * ( (ys[i]* ys[i]) + (ys[i-1] * ys[i]) + (ys[i-1] * ys[i-1] ) )
    s2 = s2 + (ys[i]-ys[i-1]) * ( (xs[i]**2) + (xs[i-1] * xs[i]) + (xs[i-1] **2) )
    i1 = i1 + (xs[i]-xs[i-1]) * ( (ys[i]**3) + (ys[i]**2 * ys[i-1]) + (ys[i] * ys[i-1]**2) + ys[i-1]**3 )
    i2 = i2 + (ys[i]-ys[i-1]) * ( (xs[i]**3) + (xs[i]**2 * xs[i-1]) + (xs[i] * xs[i-1]**2) + xs[i-1]**3 )
    i3 = i3 + (ys[i]-ys[i-1]) * (ys[i] * ((3* xs[i]**2 + 2*xs[i] * xs[i-1] + xs[i-1]**2)) + ys[i-1]*((3*xs[i-1]**2 + 2*xs[i]*xs[i-1]+xs[i]**2 )))

Ax = (1/2 *a)
Sx = -(1/6 * s1)
Sy = (1/6 * s2)
Ix = (-1/12 * i1)
Iy = (1/12 * i2)
Ixy = (-1/24 * i3)
Xt = Sy/Ax
Yt = Sx/Ax
Ixt = Ix - Yt**2*Ax
Iyt = Iy - Xt**2*Ax
Ixyt = Ixy+ Xt*Yt*Ax

#Printing Results

print("\n Point\t|\t  x\t|\t  y")
print("-" *40)
for i in range(0,n):
    print(" ",i+1,"\t|\t",xs[i],"\t|\t",ys[i])
print (f"\nAx:  \t {Ax}\nSx:  \t {Sx}\nSy:  \t {Sy}\nIx: \t {Ix:.2f}\nIy: \t {Iy:.2f}\nIxy: \t{Ixy:.2f}")
print (f"xt: \t {Xt}\nyt: \t {Yt:.2f}\nIxt: \t {Ixt:.2f}\nIyt: \t {Iyt:.2f}\nIxyt: \t {Ixyt:.2f}")






