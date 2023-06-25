import matplotlib.pyplot as plt

corna = 10
cornb = 15
side = 23

xvalues =[]
yvalues =[]
colors =[]

for i in range(1, 201):
  for j in range(1, 201):
    x = corna + i * side/100
    y =  cornb + j * side/100
    c = int(x**2 + y**2)
    if c % 3 == 0:
      xvalues.append(x)
      yvalues.append(y)
      colors.append('pink')
    elif int(c % 3) == 1:
      xvalues.append(x)
      yvalues.append(y)
      colors.append('purple')
    else:
      xvalues.append(x)
      yvalues.append(y)
      colors.append('yellow')

plt.scatter(xvalues, yvalues, c=colors, marker= '+')
plt.axis("off")
plt.show()
