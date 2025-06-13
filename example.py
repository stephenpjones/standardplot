"""
Simple example showcasing StandardPlot with dark grey styling
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import pandas as pd
from utils import StandardPlots, plot_saver

# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 50)
y1 = 2 * x + 1 + np.random.normal(0, 2, 50)
y2 = -0.5 * x + 8 + np.random.normal(0, 1.5, 50)
y3 = np.sin(x) * 3 + 5 + np.random.normal(0, 0.5, 50)

# Create DataFrame
df = pd.DataFrame({
    'x': np.tile(x, 3),
    'y': np.concatenate([y1, y2, y3]),
    'series': ['Linear Trend'] * 50 + ['Negative Trend'] * 50 + ['Sine Wave'] * 50
})

# Create line plot with multiple series
fig, ax = StandardPlots.line_plot(
    data=df, 
    x='x', 
    y='y', 
    hue='series',
    xlabel='Time (hours)',
    ylabel='Temperature (°C)'
)

# Create figures directory if it doesn't exist
import os
os.makedirs('figures', exist_ok=True)

# Save the plot
plot_saver.save_plot(fig, 'example_showcase')

print("Example plot saved to figures/example_showcase.png")
print("This showcases:")
print("- Dark grey (#4a4a4a) for all text and axes")
print("- Synthesized optimal color palette for data")
print("- Warm white (#fafafa) background")
print("- Professional styling with full borders and internal ticks")