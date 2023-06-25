import matplotlib.pyplot as plt
import random

corna = 10
cornb = 10
side = 20

xvalues =[]
yvalues =[]
colors = []
color =['blueviolet', 'chocolate', 'coral', 'cornflowerblue', 'crimson', 'cyan', 'darkmagenta', 'darkorchid', 'darkviolet', 'deeppink', 'gold', 'hotpink', 'lavendarblush', 'lightcoral', 'lightpink', 'mediumorchid', 'mediumvioletred', 'mistyrose', 'pink', 'plum', 'purple', 'red', 'yellow', 'green', 'orange', 'blue', 'salmon', 'silver']

for i in range(1, 101):
  for j in range(1, 101):
    x = corna + i * side/100
    y =  cornb + j * side/100
    c = int(x**2 + y**2)
    if c % 3 == 0:
      xvalues.append(x)
      yvalues.append(y)
      colors.append(color[random.randint(1, 3)])
    elif int(c % 3) == 1:
      xvalues.append(x)
      yvalues.append(y)
      colors.append(color[random.randint(1, 3)])
    else:
      xvalues.append(x)
      yvalues.append(y)
      colors.append(color[random.randint(1, 3)])

plt.scatter(xvalues, yvalues, c=colors, marker= 'o')
plt.axis("off")
plt.show()


