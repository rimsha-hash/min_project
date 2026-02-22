import matplotlib.pyplot as plt

# Step 1: Prepare the data
x = [1, 2, 3, 4, 5]    # x-axis points
y = [2, 4, 6, 8, 10]   # y-axis points

# Step 2: Create the plot
plt.plot(x, y)

# Step 3: Add title and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Step 4: Show the plot
plt.show()