import numpy


x= [1]*10000
y=[0.5]*10000
z=[None] *10000

for i in range(10000):
    z[i] = x[i] * y[i]
    
print(z)