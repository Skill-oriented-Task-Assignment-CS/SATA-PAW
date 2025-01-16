import matplotlib.pyplot as plt
import numpy as np
# Data for the plot
theta_values = [0.0,0.2,0.4,0.6,0.8,1]
retained_workers = [0,104,200,297,395, 420]

plt.figure(figsize=(8, 6))
plt.plot(theta_values, retained_workers, 'o-',color='blue')

plt.xlabel('Willingness Score', fontsize=20, fontweight='bold')
plt.ylabel('Net Utility', fontsize=20, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.7)

# plt.xticks(theta_values)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)


# Save the figure
plt.savefig('pmc-plots/util.eps', format='eps', dpi=300)

# Show the plot
plt.show()




# Data
pot_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
utilities = [170, 187, 261, 394, 401, 432]

# Grouping the potential levels
groups = ['Low' if pot <= 0.2 else 'Medium' if pot <= 0.4 else 'High' for pot in pot_levels]

# Calculate the average utility for each group
grouped_utilities = {
    'Low': np.mean([utilities[i] for i in range(len(pot_levels)) if groups[i] == 'Low']),
    'Medium': np.mean([utilities[i] for i in range(len(pot_levels)) if groups[i] == 'Medium']),
    'High': np.mean([utilities[i] for i in range(len(pot_levels)) if groups[i] == 'High']),
}

# Extract data for plotting
categories = list(grouped_utilities.keys())
avg_utilities = list(grouped_utilities.values())

# Set the width of the bars
bar_width = 0.5

# Calculate bar positions
index = np.arange(len(categories))

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Create bar plot with custom settings
ax.bar(index, avg_utilities, bar_width, color=['brown', 'green', 'orange'], alpha=0.7, edgecolor='black')

# Set the labels for the x and y axis with increased font size
ax.set_xlabel('Potential Level Group', fontsize=20, fontweight='bold')
ax.set_ylabel('Average Utility', fontsize=20, fontweight='bold')

# Set the x-axis ticks and labels
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=16)
ax.tick_params(axis='y', labelsize=16)

# Add grid with a MATLAB-like appearance
ax.grid(True, linestyle='--', alpha=0.7)

# Add title
# ax.set_title('Utility vs Potential Level Groups', fontsize=18, fontweight='bold')

# Save the plot with high resolution
plt.savefig('pmc-plots/pot.eps', format='eps', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Data
pot_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
dropouts = [1555, 1038, 440, 214, 171, 152]

# Grouping the potential levels
groups = ['Low' if pot <= 0.2 else 'Medium' if pot <= 0.4 else 'High' for pot in pot_levels]

# Calculate the average dropouts for each group
grouped_dropouts = {
    'Low': np.mean([dropouts[i] for i in range(len(pot_levels)) if groups[i] == 'Low']),
    'Medium': np.mean([dropouts[i] for i in range(len(pot_levels)) if groups[i] == 'Medium']),
    'High': np.mean([dropouts[i] for i in range(len(pot_levels)) if groups[i] == 'High']),
}

# Extract data for plotting
categories = list(grouped_dropouts.keys())
avg_dropouts = list(grouped_dropouts.values())

# Set the width of the bars
bar_width = 0.5

# Calculate bar positions
index = np.arange(len(categories))

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Create bar plot with custom settings
ax.bar(index, avg_dropouts, bar_width, color=['brown', 'green', 'orange'], alpha=0.7, edgecolor='black')

# Set the labels for the x and y axis with increased font size
ax.set_xlabel('Potential Level Group', fontsize=20, fontweight='bold')
ax.set_ylabel('Average Dropouts', fontsize=20, fontweight='bold')

# Set the x-axis ticks and labels
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=16)
ax.tick_params(axis='y', labelsize=16)

# Add grid with a MATLAB-like appearance
ax.grid(True, linestyle='--', alpha=0.7)

# Save the plot with high resolution
plt.savefig('pmc-plots/drop-pot.eps', format='eps', dpi=300, bbox_inches='tight')

# Show the plot

plt.show()

