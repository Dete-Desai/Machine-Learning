## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'x': [1,2,4,5],
    'y': [1,1,3,4]
})


np.random.seed(200)
k = 3
# centroids[i] = [x, y]
centroids = {
    i+1: [np.random.randint(0, 5), np.random.randint(0, 5)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()