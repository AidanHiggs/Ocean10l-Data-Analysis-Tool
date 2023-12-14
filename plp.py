import matplotlib.pyplot as plt

categories = ['Surface Turbidity', 'Mid Turbidity', 'Deep Turbidity']
percent_decreases = [-48.16, -48.35, -38.59]
colors = ['skyblue', 'lightgreen', 'salmon']

plt.figure(figsize=(10, 6))
bars = plt.barh(categories, percent_decreases, color=colors)

for bar, percent in zip(bars, percent_decreases):
    # Adjusting text position to avoid overlap
    text_position = bar.get_width() - 5 if bar.get_width() > 0 else bar.get_width() + 5
    plt.text(text_position, bar.get_y() + bar.get_height()/2, f'{percent}%', 
             va='center', ha='right' if bar.get_width() > 0 else 'left', color='white', fontsize=12)

plt.title('Percent Decrease in Turbidity from Spring to Fall')
plt.xlabel('Percent Decrease (%)')
plt.ylabel('Turbidity Type')

plt.gca().invert_yaxis()

plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.legend(bars, categories, title='Turbidity Type')

plt.tight_layout()
plt.savefig('percent_decrease_turbidity.png')
