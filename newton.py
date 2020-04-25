def sqrt(x):
    y=x
    while abs(y*y-x)>10**-6:
        y=(y+x/y)/2
    return y
print(sqrt(1702944000))