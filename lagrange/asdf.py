from scipy.interpolate import lagrange

x = [16,16.8,17.6,18.4]
y = [3062.5,3052.5,3042.5,3032.5]
p = lagrange(x,y)

print(p)

print(p(0))