import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Define the proportions and colors
flag_width = 12
flag_height = 6
black_color = "#000000"
white_color = "#FFFFFF"
green_color = "#00A859"
red_color = "#EE3344"

# Draw the black 
ax.add_patch(patches.Rectangle((0, flag_height * 2 / 3), flag_width, flag_height / 3, facecolor=black_color))

# Draw the white stripe 
ax.add_patch(patches.Rectangle((0, flag_height / 3), flag_width, flag_height / 3, facecolor=white_color))

# Draw the green stripe 
ax.add_patch(patches.Rectangle((0, 0), flag_width, flag_height / 3, facecolor=green_color))

# Draw the red triangle 
red_triangle = plt.Polygon([
    (0, 0), (0, flag_height), (flag_width / 3, flag_height / 2)
], closed=True, edgecolor='none', facecolor=red_color)
ax.add_patch(red_triangle)

# Set axis limits and aspect ratio
ax.set_xlim(0, flag_width)
ax.set_ylim(0, flag_height)
ax.set_aspect('equal')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])

# Show  the flag
plt.show()
