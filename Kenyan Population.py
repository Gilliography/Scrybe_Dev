import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hypothetical data for 5 regions and 2 genders (Male = 1, Female = 2)
regions = np.array([1, 2, 3, 4, 5])  # Region codes (e.g., counties)
genders = np.array([1, 2])  # Gender (1 = Male, 2 = Female)

# Population density for each region and gender (hypothetical values)
population_density = np.array([
    [1000, 950],  # Region 1: Male, Female
    [1100, 1050],  # Region 2: Male, Female
    [1200, 1150],  # Region 3: Male, Female
    [1300, 1250],  # Region 4: Male, Female
    [1400, 1350]   # Region 5: Male, Female
])

# Create the meshgrid for the X (regions) and Y (genders)
X, Y = np.meshgrid(regions, genders)

# Transpose Z data to fit the meshgrid (population density by gender)
Z = population_density.T  # Ensure the shape matches the grid

# Create the figure and axis for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D contour
ax.contour3D(X, Y, Z, 50, cmap='coolwarm')

# Add labels
ax.set_xlabel('Regions')
ax.set_ylabel('Gender (1=Male, 2=Female)')
ax.set_zlabel('Population Density')

# Add title
ax.set_title('Kenyan Population Density by Region and Gender')

# Show the plot
plt.show()
