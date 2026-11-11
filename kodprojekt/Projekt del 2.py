# Uppgift 1
# Vi ska göra min - och max
import numpy as np
import math

#Detta är den givna listan av tal

y = [2,4,7,5,3,6,9,8,4,5,3]

# Skapar en tom lista som sedan ska fyllas i

lok_max_lista = []

# Går igenom alla element i listan (utom första och sista).
# Därefter undersöks om element i är större än föregående och efterföljande elemt

for i in range (1, len(y) - 1):
    if y[i-1] < y[i] > y[i+1]:
        lok_max_lista.append(i)
print(lok_max_lista)

#Uppgift 2

vektor_x = []
N = 1000
for N in range (1, N+1):
    vektor_x.append(N)

vektor_y = []
for c in vektor_x:
        vektor_y.append(2*c+1)

norm_y = []
for b in vektor_y:
    norm_y.append(b**2)
print(math.sqrt(sum(norm_y)))

#Uppgift 3
v_x = np.arange(1, 1001, 1)
v_y = 2*v_x +1
n_y = np.sqrt(np.sum((v_y)**2))
print(n_y)

# Python-listor är varje element ett objekt som sparas separat i datorn minne. Numpy-array lagras tillsammans i en sammanhängade mängd i minnet. Det går snabbare för datorn att utföra beräkningar med arrayer.

#Uppgift 4
import matplotlib.pyplot as plt
plt.plot(v_x,v_y) 
plt.grid()
plt.xlabel(r"$\vec{X}$")
plt.ylabel(r"$\vec{Y}$")
plt.title(r"Graf över $\vec{Y} = 2\vec{X}+1$")

#Uppgift 5
N = 1000000 # Enligt prövning noterar vi att stabilt värde på 3.14 ges av N av storleksordnng 1 miljon
y = np.random.rand(N)
x = np.random.rand(N)

innanför = np.sqrt(x**2 + y**2) < 1
N_in = np.sum(innanför)
pi = 4*N_in / N
pi = round(pi,2)
print(pi)

#Uppgift 6
x = [-3, 2, 5, -1, 4, 0, 7]
summa = 1
antal = 0

for i in range(len(x) - 1):
    if x[i] >= 0:
        summa = x[i]^2
    antal += 1

medel = summa/len(x)
avrundning = round(medel,2)
print("Medelvärdet är:", avrundning)

#1. x[i] anger index och inte värde från en lista.
#2. Svaret ska avrundas till en decimal. 


