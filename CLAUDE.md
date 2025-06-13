# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

StandardPlot is a Python package that provides consistent plotting configuration for data analysis. It automatically applies standardized styling to matplotlib plots with a custom color palette, specific fonts, and layout configurations.

## Key Architecture

### Core Components

- **config.py**: Contains `PlotConfig` class that manages all styling configurations via matplotlib rcParams. Features both legacy blue palette and synthesized optimal palette with colorblind accessibility.
- **utils.py**: Contains `StandardPlots` class with plotting utilities and `PlotSaver` for consistent file management. Handles font application specifically for Bitstream Vera Sans Mono.
- **__init__.py**: Package entry point that auto-applies global configuration on import.

### Configuration System

The package uses a hierarchical configuration system:
1. Base configuration defined in `PlotConfig.base_config` 
2. Custom JSON configs can override defaults
3. Two palette modes: legacy blue (`#b0d8e3` background) and synthesized optimal (`#fafafa` background)
4. Global rcParams applied automatically on import

### Color Palette Integration

The package includes a sophisticated color system:
- **Synthesized Optimal Palette**: Default 6-color palette optimized for colorblind accessibility and perceptual separation
- **Legacy Blue Palette**: Original blue-based theme for backward compatibility  
- Palette switching methods: `switch_to_synthesized_palette()` and `switch_to_legacy_palette()`

## Common Development Commands

### Setup and Testing
```bash
# Install dependencies for local testing
python setup_test.py

# Run comprehensive test suite
python test_standardplot.py

# Run usage examples  
python example_usage.py
```

### Package Installation
```bash
# Install package locally for development
pip install -e .

# Build and install from setup.py
python setup.py install
```

## Font Handling

The package is configured for Bitstream Vera Sans Mono font with fallback to system monospace. Font path is hardcoded to Windows location: `C:\Users\steve\AppData\Local\Microsoft\Windows\Fonts\VeraMono.ttf`

Font application is handled by `apply_vera_font_to_axes()` function which manually applies font properties to all text elements (labels, ticks, legends).

## File Structure Patterns

- Main package files are in root directory
- Test outputs save to `./figures/` with organized subfolders
- Multiple demonstration scripts show different aspects (palette comparison, integration demos)
- Color palette development files (`*palette*.py`) contain experimental and showcase functionality

## Configuration Specifications

- Figure size: 14 × 10.5 cm (converted to inches in config)
- DPI: 300 for high-quality output
- Full border styling (all spines visible)
- Ticks only on bottom and left axes, pointing inward
- Grid disabled by default
- Consistent color cycling through palette arrays