# StandardPlot Package - Testing Version

This is a local testing version of the StandardPlot package that provides consistent plotting configuration for data analysis.

## Your Custom Configuration

- **Figure size**: 14 × 10.5 cm (5.51 × 4.13 inches)
- **Font**: Bitstream Vera Sans Mono (monospace), size 11 for labels, size 9 for legends
- **Background**: #b0d8e3 (light blue-green)
- **Borders**: Full border around plots (all spines visible)
- **Ticks**: Only on labeled axes (bottom and left)
- **Grid**: Disabled
- **Colors**: 
  - Primary: #0e3768 (dark blue)
  - Highlight: #f1f2f6 (light gray)
  - Dark: #555555 (medium gray)  
  - Other: #efe897 (light yellow)

## Testing Instructions

### 1. Setup Dependencies
```bash
cd C:\Users\steve\claude\standardplot
python setup_test.py
```

### 2. Run Tests
```bash
python test_standardplot.py
```
This will:
- Test package imports
- Verify configuration is applied correctly
- Test all plotting functions
- Create sample plots in `./figures/test_output/`
- Check font availability
- Verify style consistency

### 3. Try Examples
```bash
python example_usage.py
```
This will:
- Create various example plots demonstrating the package
- Show different plot types (line, bar, scatter, histograms, subplots)
- Demonstrate color usage
- Save examples to `./figures/examples/`

## Usage Examples

```python
# Import the package
from standardplot import StandardPlots, plot_saver, plot_config

# Create a line plot with automatic styling
fig, ax = StandardPlots.line_plot(
    data=df, x='time', y='value',
    xlabel='Time (hours)', ylabel='Temperature (°C)'
)

# Save with consistent settings
plot_saver.save_plot(fig, 'temperature_analysis', subfolder='results')

# Access colors from your palette
primary_color = plot_config.get_color('primary')  # #0e3768
colors = plot_config.get_palette(4)  # Get 4 colors from palette
```

## File Structure

```
standardplot/
├── __init__.py           # Package initialization and imports
├── config.py            # Configuration management and matplotlib settings
├── utils.py             # Plotting utility functions and PlotSaver
├── test_standardplot.py # Comprehensive test suite
├── example_usage.py     # Usage examples and demonstrations
├── setup_test.py        # Dependency setup for testing
└── README.md           # This file
```

## Expected Test Results

When you run the tests, you should see:
- ✅ All imports work correctly
- ✅ Configuration is applied (figure size, colors, font, etc.)
- ✅ Basic plotting functions create properly styled plots
- ✅ Color system works
- ✅ Subplot functionality works
- ⚠️ Font warning (if Bitstream Vera Sans Mono isn't available - this is OK)

## Troubleshooting

**Font Issues**: If you don't have Bitstream Vera Sans Mono installed, the system will fall back to the default monospace font. This is expected and won't break functionality.

**Import Errors**: Run `setup_test.py` to install missing dependencies.

**Permission Errors**: Make sure you have write permissions in the directory for creating the `figures/` folder.

## Global Installation

Once testing is successful, you can install globally using the quick_install.py script that will make this available in all Python environments.

## What Makes This Different

Unlike standard matplotlib, this package:
- Automatically applies your exact specifications
- Provides consistent color management
- Includes utility functions for common plot types
- Handles file saving with organized folder structure
- Works the same way across all your projects

The goal is to eliminate the repetitive formatting work while maintaining full flexibility when you need it.
