import matplotlib.pyplot as plt
import prtools as pr
from cWeek1 import Week1

# Make 1D array of 10 objects with 3 random values each

new_week1 = Week1()
new_week1.exc1_9()

new_boomerangs = +pr.boomerangs(100)
print(new_boomerangs)


plt.figure()
plt.scatter(new_boomerangs[:,1], new_boomerangs[:,2])
plt.show()
