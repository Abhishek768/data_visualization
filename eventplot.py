import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)


# create random data
data1 = np.random.random([6, 50])

# set different colors for each set of positions
colors1 = ['C{}'.format(i) for i in range(6)]

# set different line properties for each set of positions
# note that some overlap	
lineoffsets1 = np.array([-15, -3, 1, 1.5, 6, 10])
linelengths1 = [5, 2, 1, 1, 3, 1.5]

fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (10,6))

# create a horizontal plot
axs[0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)

axs[0].set_title('Normal Distribution')

data2 = np.random.gamma(4, size=[60, 50])
colors2 = 'black'
lineoffsets2 = 1
linelengths2 = 1

axs[1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
                    linelengths=linelengths2)

axs[1].set_title('Gamma Distribution')

plt.show()