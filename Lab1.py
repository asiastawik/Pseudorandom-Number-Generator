import numpy as np
import matplotlib.pyplot as plt
import random as rnd

# TASK 1 - PRNG
# magic numbers
a = 230  # the bigger, the better - generating numbers is more pseudorandom
c = 0
m = 10**8 + 1

N = 1000  # how many numbers we want to generate

# generating pseudorandom numbers
X_n = 2
U_list = []

X_n_str = X_n

for i in range(N):
    X_n_1 = (a * X_n + c) % m
    X_n = X_n_1

    U = X_n_1/m
    U_list.append(U)


# saving file
file = "LCG1-N" + str(N) + "U" + str(X_n_str) + ".txt"

with open(str(file), 'w') as f:
    for index in U_list:
        f.write(str(index))
        f.write('\n')

# opening/using saved file
U_list_f = []
with open(str(file)) as file:
    for line in file:
        line = line.strip()
        U_list_f.append(float(line))

# plot 1
plt.plot(U_list_f)
plt.show()

'''
Observations: If the number "a" is decreasing e.g. to 10, we can observe some repetitive parts on the graph - patterns.
If "a" is increasing - the numbers is more pseudorandom.
If we increase "N" to e.g. 10000, we can also see some patterns, but it not that visible at first sight.
'''

# plot 2
U_roll = np.roll(U_list_f, 1)
plt.plot(U_roll, U_list_f, '.')
plt.show()

# plot 3D
U_roll_2 = np.roll(U_roll, 1)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(U_roll_2, U_roll, U_list_f, 'g.')
plt.show()


# TASK 2 - RANDU
a_2 = 2**16 + 3
c_2 = 0
m_2 = 2**31

# Repeat everything from TASK 1
N_2 = 1000  # how many numbers we want to generate

# generating pseudorandom numbers
X_n = 2
U_list = []

X_n_str = X_n

for i in range(N_2):
    X_n_1 = (a_2 * X_n + c_2) % m_2
    X_n = X_n_1

    U = X_n_1/m
    U_list.append(U)


# saving file
file = "RANDU-N" + str(N) + "U" + str(X_n_str) + ".txt"

with open(str(file), 'w') as f:
    for index in U_list:
        f.write(str(index))
        f.write('\n')

# opening/using saved file
U_list_f = []
with open(str(file)) as file:
    for line in file:
        line = line.strip()
        U_list_f.append(float(line))

# plot 1
plt.plot(U_list_f)
plt.show()

# plot 2
U_roll = np.roll(U_list_f, 1)
plt.plot(U_roll, U_list_f, '.')
plt.show()

# plot 3D
U_roll_2 = np.roll(U_roll, 1)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(U_roll_2, U_roll, U_list_f, 'g.')
plt.show()

# TASK 3

'''
Python uses the Mersenne Twister as the core generator. 
It produces 53-bit precision floats and has a period of 2**19937-1. 
The Mersenne Twister is one of the most extensively tested random number generators in existence. 
However, being completely deterministic, it is not suitable for all purposes, and is completely 
unsuitable for cryptographic purposes.
Source: https://docs.python.org/3/library/random.html
'''

'''
To generate random number in Python, randint() function is used. This function is defined in random module.
'''

rnd.seed(1)

# Repeat everything from TASK 1
N_3 = 1000  # how many numbers we want to generate

# generating pseudorandom numbers
X_n = 2
U_list = []

X_n_str = X_n

for i in range(N_3):
    X_n_1 = rnd.random()
    U_list.append(X_n_1)

# saving file
file = "MersenneTwister-N" + str(N) + "U" + str(X_n_str) + ".txt"

with open(str(file), 'w') as f:
    for index in U_list:
        f.write(str(index))
        f.write('\n')

# opening/using saved file
U_list_f = []
with open(str(file)) as file:
    for line in file:
        line = line.strip()
        U_list_f.append(float(line))

# plot 1
plt.plot(U_list_f)
plt.show()

# plot 2
U_roll = np.roll(U_list_f, 1)
plt.plot(U_roll, U_list_f, '.')
plt.show()

# plot 3D
U_roll_2 = np.roll(U_roll, 1)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(U_roll_2, U_roll, U_list_f, 'g.')
plt.show()

'''
What are the advantages of random() function?
Random function is used in many applications: simulations, games, statistical analysis, 
password generator, randomizing data for testing, generate cryptographic keys, salt (cybersecurity).
Doesn't take any parameters - it's simple!
Return a pseudorandom float number between 0 and 1.
'''