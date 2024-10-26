import matplotlib.pyplot as plt

# Generate SIMD Optimization diagram
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_title("SIMD Optimization Example", fontsize=16, weight='bold')
ax.text(0.5, 0.9, "Single Instruction", ha='center', fontsize=14, color='purple', weight='bold')
ax.arrow(0.5, 0.8, 0, -0.1, head_width=0.05, head_length=0.05, color="purple")

# Data processed in parallel
positions = [0.2, 0.35, 0.5, 0.65, 0.8]
for i, pos in enumerate(positions):
    ax.text(pos, 0.6, f"Data {i+1}", ha='center', fontsize=12)
    ax.add_patch(plt.Rectangle((pos - 0.05, 0.4), 0.1, 0.2, color="lightgreen"))

# Labels and clean-up
ax.text(0.5, 0.1, "SIMD processes multiple data points simultaneously", ha='center', fontsize=12)
ax.axis('off')
plt.savefig('simd_optimization.png')  # Saves the image in the current directory
plt.show()
